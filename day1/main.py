class Elf:
    def __init__(self):
        self.inventory = []

    @property
    def calories(self):
        return sum(self.inventory)

    def add_snack(self, snack):
        self.inventory.append(snack)


def assemble_elves(file):
    elves = []
    elf = Elf()
    for line in file:
        if not line.strip():
            elves.append(elf)
            elf = Elf()
        else:
            elf.add_snack(int(line.strip()))
    elves.append(elf)
    return elves


def __add__(self, other):
    return self.calories + other.calories


def part_one():
    with open("puzzle_input.txt") as f:
        elves = assemble_elves(f)

    print(max(elves, key=lambda elf: elf.calories).calories)
    return elves


def part_two():
    elves = part_one()
    print(sum(sorted((elf.calories for elf in elves))[-3:]))


if __name__ == "__main__":
    part_two()
