def part1(data):
    groups = data.split('\n\n')

    groups = [group.split('\n') for group in groups]

    # Concatenate every group's individual strings and convert to set
    n_different_questions_per_group = [len(set(''.join(group))) for group in groups]

    return sum(n_different_questions_per_group)

# Concatenate every group's individual strings and convert to set
# Compare the element count of every group set to the group's size
def part2(data):
    groups = data.split('\n\n')

    groups = [group.split('\n') for group in groups]

    # Group sizes are needed to compare the count of each set element per group to the group size
    group_sizes = [len(group) for group in groups]

    groups_concatenated = [''.join(group) for group in groups]

    # Convert every group string to a tuple, eliminating duplicates
    group_answered_questions = [tuple(set(q)) for q in groups_concatenated]

    total_count = []

    for i, group in enumerate(group_answered_questions):
        group_count = 0

        for question in group:
            if groups_concatenated[i].count(question) == group_sizes[i]:
                group_count += 1
        
        total_count.append(group_count)


    return sum(total_count)
