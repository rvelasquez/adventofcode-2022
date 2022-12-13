# pylint: disable=missing-docstring

from calorie_counting_part1 import get_calorie_group_list


def find_top_3_elves_with_most_calories():
    elf_calories = sorted(get_calorie_group_list(), reverse=True)
    print(sum(elf_calories[0:3]))


def calculate_calories(calories_string):
    calories = list(map(int, calories_string.splitlines()))
    return sum(calories)


if __name__ == '__main__':
    find_top_3_elves_with_most_calories()
