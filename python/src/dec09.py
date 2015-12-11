import re

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


def shortest_path(distances):
    location_graph = dict()
    for distance in distances:
        parse_distance(location_graph, distance)

    shortest_found = None

    print(location_graph)
    return 0