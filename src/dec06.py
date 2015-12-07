from collections import defaultdict
import fileinput
import re

__author__ = 'anna'


COMMAND = re.compile('(turn on|turn off|toggle) (\\d+),(\\d+) through (\\d+),(\\d+)')


def iter_pos(start_x, start_y, end_x, end_y):
    """
    Iterate through the coordinates and yield each position in the interval
    """
    for x in range(end_x - start_x + 1):
        for y in range(end_y - start_y + 1):
            pos = (start_x + x, start_y + y)
            yield pos


def iter_instructions(instructions):
    """
    Iterate through instructions and yield parsed info for the valid ones.
    :param instructions:
    :return: command, start_x, start_y, end_x, end_y
    """
    for i in instructions:
        result = re.match(COMMAND, i)
        if result:
            command = result.group(1)
            start_x = int(result.group(2))
            start_y = int(result.group(3))
            end_x = int(result.group(4))
            end_y = int(result.group(5))

            yield command, start_x, start_y, end_x, end_y


def turn_off_lighting(lamps, start_x, start_y, end_x, end_y):
    """
    Turn off all lamps between the coordinates
    """
    for pos in iter_pos(start_x, start_y, end_x, end_y):
        lamps[pos] = False


def turn_on_lighting(lamps, start_x, start_y, end_x, end_y):
    """
    Turn on all lamps between the coordinates
    """
    for pos in iter_pos(start_x, start_y, end_x, end_y):
        lamps[pos] = True


def toggle_lighting(lamps, start_x, start_y, end_x, end_y):
    """
    Toggle all lamps between the coordinates. off->on, on->off
    """
    for pos in iter_pos(start_x, start_y, end_x, end_y):
        lamps[pos] = not lamps[pos]


def lightning(instructions):
    """
    Follow Santa's instructions and calculate how many lamps are lit.
    :param instructions:
    :return: No of lit lamps
    """
    lamps = defaultdict(bool)
    for (command, start_x, start_y, end_x, end_y) in iter_instructions(instructions):
        if command == 'turn off':
            turn_off_lighting(lamps, start_x, start_y, end_x, end_y)
        elif command == 'turn on':
            turn_on_lighting(lamps, start_x, start_y, end_x, end_y)
        elif command == 'toggle':
            toggle_lighting(lamps, start_x, start_y, end_x, end_y)

    return sum(1 for v in lamps.values() if v)


def turn_off_brightness(lamps, start_x, start_y, end_x, end_y):
    """
    Turn down the brightness of the lamp a notch. Min brightness is 0.
    """
    for pos in iter_pos(start_x, start_y, end_x, end_y):
        lamps[pos] -= 1
        if lamps[pos] < 0:
            lamps[pos] = 0


def turn_on_brightness(lamps, start_x, start_y, end_x, end_y):
    """
    Turn up the brightness of the lamp a notch
    """
    for pos in iter_pos(start_x, start_y, end_x, end_y):
        lamps[pos] += 1


def toggle_brightness(lamps, start_x, start_y, end_x, end_y):
    """
    In a new definition of the word 'toggle', turn up the brightness of the lamp two notches.
    """
    for pos in iter_pos(start_x, start_y, end_x, end_y):
        lamps[pos] += 2


def brightness(instructions):
    """
    Follow santa's instructions to turn the lamps on and off.
    :param instructions:
    :return: the total brightness of the lamps
    """
    lamps = defaultdict(int)
    for (command, start_x, start_y, end_x, end_y) in iter_instructions(instructions):
        if command == 'turn off':
            turn_off_brightness(lamps, start_x, start_y, end_x, end_y)
        elif command == 'turn on':
            turn_on_brightness(lamps, start_x, start_y, end_x, end_y)
        elif command == 'toggle':
            toggle_brightness(lamps, start_x, start_y, end_x, end_y)

    return sum(v for v in lamps.values())


if __name__ == '__main__':
    count = lightning(fileinput.input('../data/input.6.txt'))
    total_brightness = brightness(fileinput.input('../data/input.6.txt'))

    print("Lamps lit: {count}. Brightness {brightness}".format(count=count, brightness=total_brightness))
