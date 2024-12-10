result_score = 0

def part_one(map_numbers):
    global result_score
    N = len(map_numbers)
    M = len(map_numbers[0])

    for y, row in enumerate(map_numbers):
        for x, number in enumerate(row):
            if number == 0:
                print(number, (x, y))
                find_trail(number, x, y, map_numbers, N, M)
                print(result_score)

    return result_score


def find_trail(number, x, y, map_numbers, N, M):
    global result_score

    if number == 9:
        result_score += 1
        return

    if x + 1 < M:
        if map_numbers[y][x + 1] == number + 1:
            find_trail(number + 1, x + 1, y, map_numbers, N, M)
    if x - 1 >= 0:
        if map_numbers[y][x - 1] == number + 1:
            find_trail(number + 1, x - 1, y, map_numbers, N, M)
    if y + 1 < N:
        if map_numbers[y + 1][x] == number + 1:
            find_trail(number + 1, x, y + 1, map_numbers, N, M)
    if y - 1 >= 0:
        if map_numbers[y - 1][x] == number + 1:
            find_trail(number + 1, x, y - 1, map_numbers, N, M)


def part_two():
    pass


if __name__ == '__main__':
    map_numbers = []

    with open('example.txt') as f:
        for line in f:
            numbers = list(line.strip())
            numbers = [int(x) for x in numbers]
            map_numbers.append(numbers)

    for line in map_numbers:
        print(line)

    print(part_one(map_numbers))
    # print(part_two())