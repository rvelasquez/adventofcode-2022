# pylint: disable=missing-docstring
import os
file_path = os.path.dirname(os.path.realpath(__file__)) + "/input"


def find_elf_with_most_calories():
    elf_calories = get_calorie_group_list()
    print(max(elf_calories))


def get_calorie_group_list():
    lines = open(file_path, encoding="utf-8").read().split("\n\n")
    elf_calories = list(map(calculate_calories, lines))
    return elf_calories


def calculate_calories(calories_string):
    calories = list(map(int, calories_string.splitlines()))
    return sum(calories)


if __name__ == '__main__':
    find_elf_with_most_calories()
