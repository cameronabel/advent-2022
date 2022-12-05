def part_one():
    points_dict = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6,
    }
    score = 0
    with open('puzzle_input.txt') as f:
        for line in f:
            score += points_dict[line.strip()]
    
    print(score)


def part_two():
    points_dict = {
        'A X': 3, 
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7,
    }
    score = 0
    with open('puzzle_input.txt') as f:
        for line in f:
            score += points_dict[line.strip()]
    
    print(score)



if __name__ == '__main__':
    part_one()
    part_two()