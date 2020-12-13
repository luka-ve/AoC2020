import itertools


def part1(data):
    numbers = [int(number) for number in data.split()]

    for i in range(25, len(numbers)):
        combos = itertools.combinations(numbers[i - 25:i], 2)

        sums = [sum(combo) for combo in combos]

        number = numbers[i]

        if number not in sums:
            return number

    return 0


def part2(data):
    numbers = [int(number) for number in data.split()]

    part1_solution = part1(data)

    for i in range(len(numbers)):
        num_range = get_all_possible_sums_up_to(numbers[:i], part1_solution)

        if num_range != 0:
            return sum([min(num_range), max(num_range)])


def get_all_possible_sums_up_to(nums, target):
    for i in range(len(nums)):
        if sum(nums[i:]) == target:
            return nums[i:]

    return 0
