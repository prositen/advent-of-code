import re
import itertools
import sys

__author__ = 'anna'

RE_DISTANCE = r'(\w+) to (\w+) = (\d+)'


def parse_distance(location_graph, d):
    result = re.match(RE_DISTANCE, d)
    if result:
        city_1 = result.group(1)
        city_2 = result.group(2)
        distance = int(result.group(3))

        if city_1 not in location_graph:
            location_graph[city_1] = {}
        if city_2 not in location_graph:
            location_graph[city_2] = {}
        location_graph[city_1][city_2] = distance
        location_graph[city_2][city_1] = distance


def longest_path(distances):
    return path(distances, max, 0)


def shortest_path(distances):
    return path(distances, min, sys.maxsize)


def path(distances, method, start_value):
    distance_graph = dict()
    for distance in distances:
        parse_distance(distance_graph, distance)

    locations = distance_graph.keys()
    shortest_distance = start_value
    for order in itertools.permutations(locations):
        distance = 0
        current = order[0]
        for city in order[1:]:
            distance += distance_graph[current][city]
            current = city
        shortest_distance = method(shortest_distance, distance)

    return shortest_distance


if __name__ == '__main__':
    with open('../../../data/2015/input.9.txt', 'r') as fh:
        print("Shortest path: {distance}".format(distance=shortest_path(fh.readlines())))
        fh.seek(0)
        print("Longest path: {distance}".format(distance=longest_path(fh.readlines())))
