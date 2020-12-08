aoc_txt = 'puzzle_input.txt'


def aoc_day1_1():
    with open(aoc_txt, 'r') as puzzle:
        lines = puzzle.readlines()
        for line in lines:
            for _ in lines:
                if int(line) + int(_) == 2020:
                    aoc_result = int(line) * int(_)
                    print(f'Challenge 1.1 Multiplied: {aoc_result}')
                    return


def aoc_day1_2():
    with open(aoc_txt, 'r') as puzzle:
        lines = puzzle.readlines()
        for line1 in lines:
            for line2 in lines:
                if int(line1) + int(line2) < 2020:
                    for line3 in lines:
                        if int(line1) + int(line2) + int(line3) == 2020:
                            aoc_result = int(line1) * int(line2) * int(line3)
                            print(f'Challenge 1.2 Multiplied: {aoc_result}')
                            return


aoc_day1_1()
aoc_day1_2()