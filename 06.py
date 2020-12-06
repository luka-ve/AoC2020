# Concatenate every group's individual strings and convert to set
def part1(data):
    groups = data.split('\n\n')

    groups = [group.split('\n') for group in groups]

    n_different_questions_per_group = [len(set(''.join(group))) for group in groups]

    return sum(n_different_questions_per_group)

def part2(data):
    pass
