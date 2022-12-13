# pylint: disable=missing-docstring

def find_elf_with_most_calories():
    elf_calories = get_calorie_group_list()
    print(max(elf_calories))


def get_calorie_group_list():
    lines = open("input", encoding="utf-8").read().split("\n\n")
    elf_calories = list(map(calculate_calories, lines))
    return elf_calories


def calculate_calories(calories_string):
    calories = list(map(int, calories_string.splitlines()))
    return sum(calories)


if __name__ == '__main__':
    find_elf_with_most_calories()
