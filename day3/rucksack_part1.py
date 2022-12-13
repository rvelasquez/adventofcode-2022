# pylint: disable=missing-docstring

def find_common_items(rucksack1, rucksack2):
    rucksack1_item_types = set(list(rucksack1))
    rucksack2_item_types = set(list(rucksack2))

    return rucksack2_item_types.intersection(rucksack1_item_types)


def get_value(common_item):
    common_item_value = ord(common_item)
    if ord('A') <= common_item_value <= ord('Z'):
        return common_item_value - 38
    elif ord('a') <= common_item_value <= ord('z'):
        return common_item_value - 96
    else:
        return 0


def total_priorities():
    rucksacks = open("input", encoding="utf-8").read().splitlines()
    common_items_collection = []
    for rucksack in rucksacks:
        compartment1 = rucksack[:len(rucksack) // 2]
        compartment2 = rucksack[len(rucksack) // 2:]
        common_items_collection.append(find_common_items(compartment1, compartment2))

    sum_priorities = 0
    for common_items in common_items_collection:
        for common_item in common_items:
            sum_priorities += get_value(common_item)

    print(sum_priorities)


if __name__ == '__main__':
    total_priorities()
