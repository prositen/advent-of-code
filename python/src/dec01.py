#!/usr/bin/env python
import fileinput
import sys

__author__ = 'anna'


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
            return pos+1
    return -1


if __name__ == '__main__':
    for no, line in enumerate(fileinput.input('../../data/input.1.txt')):
        print("Instruction {line}: Floor {floor}".format(line=no, floor=floor(0, line)))
        print("On floor -1: ", when_on_floor(0, line, -1))
