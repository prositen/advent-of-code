import json

__author__ = 'Anna'


def sum_numbers(json_raw, skip_red=False):
    json_tree = json.loads(json_raw)

    return sum_subtree(json_tree, skip_red)


def sum_subtree(json_data, skip_red):
    local_sum = 0
    if isinstance(json_data, dict):
        if not (skip_red and 'red' in json_data.values()):
            for n,v in json_data.items():
                local_sum += sum_subtree(v, skip_red)
    elif isinstance(json_data, list):
        for i in json_data:
            local_sum += sum_subtree(i, skip_red)
    else:
        try:
            local_sum += int(json_data)
        except ValueError:
            pass
    return local_sum


if __name__ == '__main__':
    with open('../../../data/2015/input.12.txt', 'r') as fh:
        print("The sum is {sum}".format(sum=sum_numbers(fh.readline())))
        fh.seek(0)
        print("Not counting red objects, the sum is {sum}".format(sum=sum_numbers(fh.readline(), skip_red=True)))