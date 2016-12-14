from functools import lru_cache
from hashlib import md5
import re

re_TRIPLE = re.compile(r"(\w)\1\1")
re_QUINTUPLE = re.compile(r"(\w)\1{4}")


@lru_cache(maxsize=None)
def hashcode(value):
    value = value.encode('utf-8')
    return md5(value)


@lru_cache(maxsize=None)
def super_hash(value, keystretch):
    for _ in range(keystretch + 1):
        value = hashcode(value).hexdigest()
    return value


def get_hash_keys(secret, keystretch=None):
    with open("hashes.txt", 'w') as fh, open("keys.txt", "w") as kh:
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


if __name__ == '__main__':
    keys = get_hash_keys("ngcjuoqr")
    print("The 64th key index is", keys[63])
    keys = get_hash_keys("ngcjuoqr", keystretch=2016)
    print("The 64th key index with super stretching is", keys[63])
