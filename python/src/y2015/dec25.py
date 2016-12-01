__author__ = 'anna'

""" To continue, please consult the code grid in the manual.  Enter the code at row 2947, column 3029. """


def next_cell():
    row = 0
    while True:
        row += 1
        for col in range(1, row+1):
            yield row - col + 1, col


def code(row_index, col_index):
    the_code = 20151125
    for row, col in next_cell():
        if row == row_index and col == col_index:
            break
        the_code = divmod(the_code * 252533, 33554393)[1]
    return the_code


def main():
    print(code(2947, 3029))

if __name__ == '__main__':
    main()


