def part1(data):
    data = data.strip('\n')[:-1]
    numbers = [int(number.strip()) for number in data]

    target = 2020

    for number in numbers:
        current_target = target - number

        for j in numbers:
            if current_target == j:
                return current_target * number


def part2(data):
    from itertools import combinations
    from math import prod

    data = data.strip('\n')[:-1]

    numbers = [int(number.strip()) for number in data]

    target = 2020

    # Remove all numbers that are larger than the sum of two the smallest numbers
    # Those will not be considered

    largest_possible_num = target - sum(sorted(numbers)[:2])
    numbers_smaller = [i for (i, v) in zip(numbers, [x <= largest_possible_num for x in numbers]) if v]

    # Find combinations

    combos = combinations(numbers_smaller, 3)

    return prod([x for x in combos if sum(x) == target][0])
