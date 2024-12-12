visited_coords = set()

def part_one(gardens):
    global visited_coords

    N = len(gardens)

    for y, row in enumerate(gardens):
        for x, garden in enumerate(row):
            if (x, y) not in visited_coords:
                area = 0
                plant = garden
                area += find_plot(x, y, plant, gardens, N)
                print(f"{x, y} - {plant} area: {area}")


def find_plot(x, y, plant, gardens, N):
    global visited_coords

    area = 1

    if gardens[y][x] != plant:
        return 0

    if x + 1 < N:
        if (x, y) not in visited_coords:
            if gardens[y][x + 1] == plant:
                visited_coords.add((x, y))
                area += find_plot(x + 1, y, plant, gardens, N)
    if x - 1 >= 0:
        if (x, y) not in visited_coords:
            if gardens[y][x - 1] == plant:
                visited_coords.add((x, y))
                area += find_plot(x - 1, y, plant, gardens, N)
    if y + 1 < N:
        if (x, y) not in visited_coords:
            if gardens[y + 1][x] == plant:
                visited_coords.add((x, y))
                area += find_plot(x, y + 1, plant, gardens, N)
    if y - 1 >= 0:
        if (x, y) not in visited_coords:
            if gardens[y - 1][x] == plant:
                visited_coords.add((x, y))
                area += find_plot(x, y - 1, plant, gardens, N)
    return area
        

def part_two():
    pass


if __name__ == '__main__':
    gardens = []

    with open('example.txt') as f:
        for line in f:
            gardens.append(list(line.strip()))

    for row in gardens:
        print(row)

    print(part_one(gardens))
    # print(part_two(stones))