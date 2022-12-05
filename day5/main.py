import re

def initialize_boat(data):
    boat = {str(i): [] for i in range(1, 10)}
    for row in data[::-1]:
        for i, char in enumerate(row[1::4], 1):
            if char != ' ':
                boat[str(i)].append(char)
    return boat


def move_crates_9000(boat, num, old, new):
    for _ in range(int(num)):
        boat[new].append(boat[old].pop())


def move_crates_9001(boat, num, old, new):
    boat[new].extend(boat[old][-int(num)::-1])
    boat[old] = boat[old][:-int(num)]
    

def part_one(boat, instructions):
    for line in instructions:
        s = r"move (\d+) from (\d) to (\d)"
        num, old, new = re.search(s, line).group(1, 2, 3)
        move_crates_9000(boat, num, old, new)
    s = ""
    for i in range(1, 10):
        s += boat[str(i)][-1]
    return s


def part_two(boat, instructions):
    for line in instructions:
        s = r"move (\d+) from (\d) to (\d)"
        num, old, new = re.search(s, line).group(1, 2, 3)
        move_crates_9001(boat, num, old, new)
    s = ""
    for i in range(1, 10):
        s += boat[str(i)][-1]
    return s



if __name__ == "__main__":
    with open("puzzle_input.txt") as f:
        data = f.read().splitlines()
    boat1 = initialize_boat(data[:8])
    boat2 = initialize_boat(data[:8])
    print(boat1)
    print(boat2)
    data = data[10:]
    print(part_one(boat1, data))
    print(part_two(boat2, data))