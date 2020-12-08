aoc_txt3 = 'puzzle_input.txt'


def count_trees_on_slope(lines, right, down):
    trees = 0
    move_right = right
    move_down = down
    try:
        while True:
            if lines[move_down][move_right] == '#':
                trees += 1
            move_down += down
            move_right += right
            if move_right >= len(lines[move_down]):
                move_right = (move_right % len(
                    lines[move_down]))  # modulo resets index to 0 if bigger/equals to max line length
    except IndexError:
        return trees


def read_puzzle(puzzle_file, puzzle_part):
    with open(puzzle_file, 'r') as puzzle:
        lines = puzzle.read().splitlines()  # removes \n at the end
        if puzzle_part == 1:
            print(f'Challenge 3.{puzzle_part}: {count_trees_on_slope(lines, 3, 1)}')

        if puzzle_part == 2:
            slope1 = count_trees_on_slope(lines, 1, 1)
            slope2 = count_trees_on_slope(lines, 3, 1)
            slope3 = count_trees_on_slope(lines, 5, 1)
            slope4 = count_trees_on_slope(lines, 7, 1)
            slope5 = count_trees_on_slope(lines, 1, 2)
            print(f'Challenge 3.{puzzle_part}: {slope1 * slope2 * slope3 * slope4 *slope5}')


read_puzzle(aoc_txt3, 1)
read_puzzle(aoc_txt3, 2)
