def analyze_rucksack(rucksack):
    left = set(rucksack[:len(rucksack) // 2])
    right = set(rucksack[len(rucksack) // 2:])
    return tuple(left & right)[0]


def prioritize(char):
    if char == char.upper():
        return ord(char) - 38
    else:
        return ord(char) - 96


def analyze_group(group):
    left, middle, right = (set(rucksack) for rucksack in group)
    return tuple(left & middle & right)[0]

def part_one(rucksacks):
    total = 0
    for rucksack in rucksacks:
        total += prioritize(analyze_rucksack(rucksack))
    return total


def part_two(rucksacks):
    total = 0
    group = []
    for i, rucksack in enumerate(rucksacks, 1):
        group.append(rucksack)
        if not i % 3:
            total += prioritize(analyze_group(group))
            group = []
    return total


if __name__ == "__main__":
    with open('puzzle_input.txt') as f:
        rucksacks = f.read().splitlines()
    print(part_one(rucksacks))
    print(part_two(rucksacks))