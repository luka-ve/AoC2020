import re

no_bag = 'None'
target_bag = 'shiny gold'


def part1(data):
    bags = get_bag_structure(data)

    bags_containing_target_bag = set()
    
    for bag_key in bags.keys():
        if target_bag in bags[bag_key].keys():
            bags_containing_target_bag.add(bag_key)

    return len(bags_containing_target_bag)


def get_bag_structure(data):
    bag_regex = r'^([\w ]+(?= bags contain )).*?(\d[\w\s,]+|no)'
    inner_bags_regex = r'(\d) ([\w ]+(?= bag))|(^no$)'

    all_bags = re.findall(bag_regex, data, re.MULTILINE)

    outermost_bags = [bag[0] for bag in all_bags]
    inner_bags = [re.findall(inner_bags_regex, bag[1]) for bag in all_bags]

    bags = dict()

    for i, bag in enumerate(outermost_bags):
        bags[bag] = dict(
            [[inner_bag[1], inner_bag[0]] for inner_bag in inner_bags[i]])
        if bags[bag] == {'': ''}:
            bags[bag] = {no_bag: '0'}

    return bags


def find_all_super_bags(bags, bag_keys_so_far):
    for bag_key in bags.keys():
        if target_bag in bags[bag_key].keys() and bag_key not in bag_keys_so_far:
            bag_keys_so_far.add(bag_key)

    


def bag_test(data):
    pass
