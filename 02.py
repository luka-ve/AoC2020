import re


def part1(data):

    mins = []
    maxs = []
    letters = []
    passwords = []

    data = data.split('\n')[:-1]

    for line in data:
        mins.append(int(re.search(r'\d+(?=-)', line).group()))
        maxs.append(int(re.search(r'-\d+', line).group()[1:]))
        letters.append(re.search(r'[a-z]:', line).group()[:-1])
        passwords.append(re.search(r': \w+', line).group()[2:])

    def check_password(password, letter, min, max):
        counts = 0

        for l in password:
            if l == letter:
                counts = counts + 1

        if counts >= min and counts <= max:
            return True
        else:
            return False

    n_valid_passwords = 0

    for i in range(0, len(passwords)):
        n_valid_passwords = n_valid_passwords + check_password(
            passwords[i], letters[i], mins[i], maxs[i])

    return n_valid_passwords


def part2(data):

    passwords = []

    data = data.split('\n')[:-1]

    for line in data:
        constraint_positions = [int(pos) for pos in re.findall(r'\d+', line)]
        constraint_letter = re.search(r'[a-z]:', line).group()[:-1]
        password = re.search(r': \w+', line).group()[2:]

        passwords.append(
            Password(
                password,
                constraint_letter=constraint_letter,
                constraint_positions=constraint_positions))

    valid_passwords = [pw.validate() for pw in passwords]

    return valid_passwords.count(True)


class Password:
    def __init__(self,
                 password,
                 constraint_letter=None,
                 constraint_positions=[]):
        self.password = password
        self.constraint_letter = constraint_letter
        self.constraint_positions = constraint_positions

    def validate(self):
        count = 0

        for pos in self.constraint_positions:
            count = count + (self.password[pos - 1] == self.constraint_letter)

        return count == 1
