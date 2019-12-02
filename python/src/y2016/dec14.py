from hashlib import md5
import re
from timeit import default_timer as timer

re_TRIPLE = re.compile(r"(\w)\1\1")
re_QUINTUPLE = re.compile(r"(\w)\1{4}")


def hashcode(value):
    value = value.encode('utf-8')
    return md5(value)


def super_hash(value, keystretch):
    for _ in range(keystretch + 1):
        value = hashcode(value).hexdigest()
    return value


def backtrack_from_quintuple(secret, keystretch=None):
    hashes = [(0, "")] * 1000  # Rolling list of the last 1000 hashes found
    index = 0
    keys = []
    cleanup_max = 0
    while len(keys) < 64 or (index < cleanup_max):
        value = ("%s%d" % (secret, index))
        if keystretch:
            hash_value = super_hash(value, keystretch)
        else:
            hash_value = hashcode(value).hexdigest()
        for q in re_QUINTUPLE.findall(hash_value):
            for hash_index, (key_index, key) in enumerate(hashes):
                result = re_TRIPLE.search(key)
                if result and result.group(1) == q:
                    keys.append((key_index, key))
                    hashes[hash_index] = (0, "")

        if cleanup_max:
            hashes[index % 1000] = (0, "")
        else:
            hashes[index % 1000] = (index, hash_value)

        index += 1
        if len(keys) >= 64 and cleanup_max == 0:
            # We've found 64 keys but in the last 1000 hashes there may still be
            # more keys to consider. Go another 1001 laps to verify.
            cleanup_max = index + 1001

    return [x[0] for x in sorted(keys)]


def pre_compute_future_hashes(secret, keystretch=None):
    keys = []
    future_hashes = [(0, "")] * 1000
    index = 0
    while len(keys) < 64:
        value = ("%s%d" % (secret, index))
        if keystretch:
            hash_value = super_hash(value, keystretch)
        else:
            hash_value = hashcode(value).hexdigest()

        future_hashes[-1] = (index, hash_value)
        if index > 999:
            result = re_TRIPLE.search(future_hashes[0][1])
            if result:
                q = result.group(1) * 5
                if any(q in x[1] for x in future_hashes[1:]):
                    keys.append(future_hashes[0])

        future_hashes = future_hashes[1:] + [(0, "")]
        index += 1
    return [x[0] for x in keys]


def store_index_of_hashes(secret, keystretch=None):
    keys = []
    index = 0
    cleanup_max = 0
    hashes = [[] for _ in range(16)]
    while len(keys) < 64 or (index < cleanup_max):
        value = ("%s%d" % (secret, index))
        if keystretch:
            hash_value = super_hash(value, keystretch)
        else:
            hash_value = hashcode(value).hexdigest()

        for q in re_QUINTUPLE.findall(hash_value):
            hexv = int(q, 16)
            keys.extend(i for i in hashes[hexv] if (i + 1000) >= index)
            hashes[hexv] = []
        if cleanup_max == 0:
            result = re_TRIPLE.search(hash_value)
            if result:
                hexv = int(result.group(1), 16)
                hashes[hexv].append(index)
        if len(keys) >= 64 and cleanup_max == 0:
            # We've found 64 keys but in the last 1000 hashes there may still be
            # more keys to consider. Go another 1001 laps to verify.
            cleanup_max = index + 1001

        index += 1
    return sorted(keys)


def get_hash_keys(secret, keystretch=None):
    return store_index_of_hashes(secret, keystretch)


if __name__ == '__main__':
    hash_keys = get_hash_keys("ngcjuoqr")
    print("The 64th key index is", hash_keys[63])
    for fn in backtrack_from_quintuple, pre_compute_future_hashes, store_index_of_hashes:
        start = timer()
        hash_keys = fn("ngcjuoqr", keystretch=2016)
        end = timer()
        print(fn.__name__, end - start)
    print("The 64th key index with super stretching is", hash_keys[63])
