def assign_section(s):
    start, end = s.split('-')
    return set(range(int(start), int(end) + 1))



def analyze_pair(pair):
    a, b = pair.split(',')
    a = assign_section(a)
    b = assign_section(b)
    return a, b



def part_one(pairs):
    total = 0
    for pair in pairs:
        a, b = analyze_pair(pair)
        total += a.issubset(b) or b.issubset(a)
    return total

def part_two(pairs):
    total = 0
    for pair in pairs:
        a, b = analyze_pair(pair)
        total += not a.isdisjoint(b)
    return total




if __name__ == "__main__":
    with open('puzzle_input.txt') as f:
        pairs = f.read().splitlines()
    print(part_one(pairs))
    print(part_two(pairs))