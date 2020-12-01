#!/usr/bin/env python

__author__ = 'anna'

from python.src.common import input_for


def floor(start=0, instructions=""):
    up = instructions.count('(')
    down = instructions.count(')')
    return start + up - down


def when_on_floor(start=0, instructions="", wanted_floor=0):
    current_floor = start
    for pos, i in enumerate(instructions):
        if i == ')':
            current_floor -= 1
        elif i == '(':
            current_floor += 1
        if wanted_floor == current_floor:
            return pos + 1
    return -1


if __name__ == '__main__':
    with open(input_for(2015, 1)) as fh:
        for no, line in enumerate(fh.readlines()):
            print("Instruction {line}: Floor {floor}".format(line=no, floor=floor(0, line)))
            print("On floor -1: ", when_on_floor(0, line, -1))
