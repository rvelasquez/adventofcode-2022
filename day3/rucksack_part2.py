# pylint: disable=missing-docstring
import numpy as np
import os
file_path = os.path.dirname(os.path.realpath(__file__)) + "/input"


def find_common_items(rucksack1, rucksack2, rucksack3):
    rucksack1_item_types = set(list(rucksack1))
    rucksack2_item_types = set(list(rucksack2))
    rucksack3_item_types = set(list(rucksack3))

    return rucksack3_item_types.intersection(rucksack2_item_types).intersection(rucksack1_item_types)


def get_value(item):
    item_value = ord(item)
    if ord('A') <= item_value <= ord('Z'):
        return item_value - 38
    elif ord('a') <= item_value <= ord('z'):
        return item_value - 96
    else:
        return 0


def total_priorities():
    rucksacks = open(file_path, encoding="utf-8").read().splitlines()
    rucksack_groups = np.array_split(rucksacks, len(rucksacks) / 3)
    badges = []
    for rucksack_group in rucksack_groups:
        badges.append(find_common_items(rucksack_group[0], rucksack_group[1], rucksack_group[2]))

    sum_priorities = 0
    for badge in badges:
        for common_item in badge:
            sum_priorities += get_value(common_item)

    print(sum_priorities)


if __name__ == '__main__':
    total_priorities()
