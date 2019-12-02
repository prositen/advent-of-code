import re
import string
from collections import Counter

re_ROOM = re.compile(r"((?:\w+\-)+)(\d+)\[(\w+)\]")


def valid_room(name, checksum):
    char_count = Counter(name)
    del char_count['-']
    most_common = "".join(x[0] for x in sorted(char_count.items(), key=lambda x: (-x[1], x[0])))
    return checksum == most_common[:5]


def valid_rooms(rooms):
    split_room_info = [x.groups(1) for x in map(re_ROOM.match, rooms)]
    return list((x[0][:-1], int(x[1]), x[2])
                for x in filter(lambda x: valid_room(x[0], x[2]), split_room_info))


def sum_valid_sector_ids(rooms):
    return sum([int(x[1]) for x in valid_rooms(rooms)])


def decrypt_name(name, sector_id):
    rotate = sector_id % 26
    translate_table = str.maketrans(string.ascii_lowercase + '-',
                                    string.ascii_lowercase[rotate:]
                                    + string.ascii_lowercase[:rotate] + ' ')
    return name.translate(translate_table)


def find_northpole(rooms):
    for name, sector, _ in valid_rooms(rooms):
        if 'northpole' in (decrypt_name(name, sector)):
            print(decrypt_name(name, sector))
            return sector


if __name__ == '__main__':
    with open('../../../data/2016/input.4.txt', 'r') as fh:
        rooms = fh.readlines()
        print("Sum of valid sector IDS: ", sum_valid_sector_ids(rooms))
        print("North Pole objects are in sector", find_northpole(rooms))
