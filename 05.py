import re
from math import ceil


def part1(data):
    rows, seats = get_seat_positions_from_raw_data(data)

    seat_ids = set([get_seat_id(rows[i], seats[i]) for i in range(len(rows))])

    return max(seat_ids)


def part2(data):
    rows, seats = get_seat_positions_from_raw_data(data)

    seat_ids = [get_seat_id(rows[i], seats[i]) for i in range(len(rows))]
    seat_ids.sort()

    for i in range(len(seat_ids)):
        if seat_ids[i + 1] - seat_ids[i] == 2:
            return seat_ids[i]

    raise Exception('No free seat found!')


def get_seat_positions_from_raw_data(data):
    boarding_passes = data.split()

    seat_regex = r'^([BF]{7})([RL]{3})$'
    row_range = [0, 127]
    seat_range = [0, 7]

    seat_pos = [[], []]

    for bp in boarding_passes:
        match = re.match(seat_regex, bp)

        if match:
            seat_pos[0].append(
                binary_space_partition(row_range, match.group(1), 'B', 'F'))
            seat_pos[1].append(
                binary_space_partition(seat_range, match.group(2), 'R', 'L'))

    return seat_pos


def binary_space_partition(p_range, step_string, up_symbol, down_symbol):
    current_partition = p_range.copy()

    for letter in step_string:
        if letter == up_symbol:
            current_partition[0] += ceil(
                (current_partition[1] - current_partition[0]) / 2)
        elif letter == down_symbol:
            current_partition[1] -= ceil(
                (current_partition[1] - current_partition[0]) / 2)

    return current_partition[0]


def get_seat_id(row, seat):
    return row * 8 + seat


def test_BSP():
    row = binary_space_partition([0, 127], 'BFFFBBFRRR', 'B', 'F')
    seat = binary_space_partition([0, 7], 'BFFFBBFRRR', 'R', 'L')
    seat_id = get_seat_id(row, seat)

    assert row == 70, row
    assert seat == 7, seat
    assert seat_id == 567, seat_id


test_BSP()
