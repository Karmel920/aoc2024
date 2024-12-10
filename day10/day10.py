result_score = 0
starting_coords = None
slopes_set = dict()

result_score_two = 0

def part_one(map_numbers):
    global result_score
    global slopes_set
    global starting_coords

    N = len(map_numbers)
    M = len(map_numbers[0])

    for y, row in enumerate(map_numbers):
        for x, number in enumerate(row):
            if number == 0:
                starting_coords = (x, y)
                find_trail(x, y, map_numbers, N, M)

    return result_score


def find_trail(x, y, map_numbers, N, M):
    global result_score

    if map_numbers[y][x] == 9 and (x, y) not in slopes_set.setdefault(starting_coords, set()):
        result_score += 1
        slopes_set[starting_coords].add((x, y))
        return

    if x + 1 < M:
        if map_numbers[y][x + 1] == map_numbers[y][x] + 1:
            find_trail(x + 1, y, map_numbers, N, M)
    if x - 1 >= 0:
        if map_numbers[y][x - 1] == map_numbers[y][x] + 1:
            find_trail(x - 1, y, map_numbers, N, M)
    if y + 1 < N:
        if map_numbers[y + 1][x] == map_numbers[y][x] + 1:
            find_trail(x, y + 1, map_numbers, N, M)
    if y - 1 >= 0:
        if map_numbers[y - 1][x] == map_numbers[y][x] + 1:
            find_trail(x, y - 1, map_numbers, N, M)


def part_two(map_numbers):
    global result_score_two

    N = len(map_numbers)
    M = len(map_numbers[0])

    for y, row in enumerate(map_numbers):
        for x, number in enumerate(row):
            if number == 0:
                find_trail_two(x, y, map_numbers, N, M)

    return result_score_two


def find_trail_two(x, y, map_numbers, N, M):
    global result_score_two

    if map_numbers[y][x] == 9 :
        result_score_two += 1
        return

    if x + 1 < M:
        if map_numbers[y][x + 1] == map_numbers[y][x] + 1:
            find_trail_two(x + 1, y, map_numbers, N, M)
    if x - 1 >= 0:
        if map_numbers[y][x - 1] == map_numbers[y][x] + 1:
            find_trail_two(x - 1, y, map_numbers, N, M)
    if y + 1 < N:
        if map_numbers[y + 1][x] == map_numbers[y][x] + 1:
            find_trail_two(x, y + 1, map_numbers, N, M)
    if y - 1 >= 0:
        if map_numbers[y - 1][x] == map_numbers[y][x] + 1:
            find_trail_two(x, y - 1, map_numbers, N, M)


if __name__ == '__main__':
    map_numbers = []

    with open('input.txt') as f:
        for line in f:
            numbers = list(line.strip())
            numbers = [int(x) for x in numbers]
            map_numbers.append(numbers)

    print(part_one(map_numbers))
    print(part_two(map_numbers))