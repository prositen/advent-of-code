def get_next_row(prev_row):
    row = []
    for i in range(len(prev_row)):
        prev = ('.' + prev_row + '.')[i:i + 3]
        row.append('^' if prev in ['^^.', '.^^', '^..', '..^'] else '.')
    return ''.join(row)


def floor_map(start_row, no_rows):
    rows = [start_row]
    for _ in range(1, no_rows):
        rows.append(get_next_row(rows[-1]))
    return rows


def count_safe_tiles(start_row, no_rows):
    tile_count = start_row.count('.')
    prev_row = start_row
    for _ in range(1, no_rows):
        prev_row = get_next_row(prev_row)
        tile_count += prev_row.count('.')
    return tile_count


if __name__ == '__main__':
    with open('../../../data/2016/input.18.txt', 'r') as fh:
        start = fh.readlines()[0].strip()
        floor = floor_map(start, 40)
        print("Number of safe tiles: ", ''.join(floor).count('.'))
        print("Number of safe tiles after 400000 rows: ", count_safe_tiles(start, 400000))
