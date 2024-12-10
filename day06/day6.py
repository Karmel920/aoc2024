def part_one(map_guard):
    N = len(map_guard)
    M = len(map_guard[0])

    coords_vertices, x, y = create_coords_vertices_and_start_point(map_guard, N, M)

    direction = 'top'

    while True:
        if direction == 'top':
            if not coords_vertices[(x, y)]:
                coords_vertices[(x, y)] = True
            if not y - 1 >= 0:
                break
            if coords_vertices[(x, y - 1)] == '#':
                direction = 'right'
                continue
            y -= 1
        elif direction == 'right':
            if not coords_vertices[(x, y)]:
                coords_vertices[(x, y)] = True
            if not x + 1 < M:
                break
            if coords_vertices[(x + 1, y)] == '#':
                direction = 'down'
                continue
            x += 1
        elif direction == 'down':
            if not coords_vertices[(x, y)]:
                coords_vertices[(x, y)] = True
            if not y + 1 < N:
                break
            if coords_vertices[(x, y + 1)] == '#':
                direction = 'left'
                continue
            y += 1
        elif direction == 'left':
            if not coords_vertices[(x, y)]:
                coords_vertices[(x, y)] = True
            if not x - 1 >= 0:
                break
            if coords_vertices[(x - 1, y)] == '#':
                direction = 'top'
                continue
            x -= 1

    # for i in range(N):
    #     for j in range(M):
    #         if coords_vertices[(j, i)] is True:
    #             print("X", end='')
    #         elif coords_vertices[(j, i)] == "#":
    #             print("#", end='')
    #         else:
    #             print(".", end='')
    #     print()
    count_visited_coords = sum(1 for value in coords_vertices.values() if value is True)
    return count_visited_coords


def part_two(map_guard):
    N = len(map_guard)
    M = len(map_guard[0])

    coords_vertices, x, y = create_coords_vertices_and_start_point(map_guard, N, M)

    possible_loops = 0
    possible_obstruction_coords = []
    obstruction_queue = []

    direction = 'top'

    while True:
        if direction == 'top':
            if not coords_vertices[(x, y)]:
                coords_vertices[(x, y)] = True
            if not y - 1 >= 0:
                break
            if coords_vertices[(x, y - 1)] == '#':
                direction = 'right'
                if len(obstruction_queue) == 3:
                    obstruction_queue.pop(0)
                obstruction_queue.append((x, y - 1))
                continue
            if len(obstruction_queue) == 3 and obstruction_queue[0][1] == y:
                possible_loops += 1
                possible_obstruction_coords.append((x, y - 1))
                obstruction_queue.pop(0)
            y -= 1

        elif direction == 'right':
            if not coords_vertices[(x, y)]:
                coords_vertices[(x, y)] = True
            if not x + 1 < M:
                break
            if coords_vertices[(x + 1, y)] == '#':
                direction = 'down'
                if len(obstruction_queue) == 3:
                    obstruction_queue.pop(0)
                obstruction_queue.append((x + 1, y))
                continue
            if len(obstruction_queue) == 3 and obstruction_queue[0][0] == x:
                possible_loops += 1
                possible_obstruction_coords.append((x + 1, y))
                obstruction_queue.pop(0)
            x += 1

        elif direction == 'down':
            if not coords_vertices[(x, y)]:
                coords_vertices[(x, y)] = True
            if not y + 1 < N:
                break
            if coords_vertices[(x, y + 1)] == '#':
                direction = 'left'
                if len(obstruction_queue) == 3:
                    obstruction_queue.pop(0)
                obstruction_queue.append((x, y + 1))
                continue
            if len(obstruction_queue) == 3 and obstruction_queue[0][1] == y:
                possible_loops += 1
                possible_obstruction_coords.append((x, y + 1))
                obstruction_queue.pop(0)
            y += 1

        elif direction == 'left':
            if not coords_vertices[(x, y)]:
                coords_vertices[(x, y)] = True
            if not x - 1 >= 0:
                break
            if coords_vertices[(x - 1, y)] == '#':
                direction = 'top'
                if len(obstruction_queue) == 3:
                    obstruction_queue.pop(0)
                obstruction_queue.append((x - 1, y))
                continue
            if len(obstruction_queue) == 3 and obstruction_queue[0][0] == x:
                possible_loops += 1
                possible_obstruction_coords.append((x - 1, y))
                obstruction_queue.pop(0)
            x -= 1

    for i in range(N):
        for j in range(M):
            if coords_vertices[(j, i)] == "#":
                print("#", end='')
            elif (j, i) in possible_obstruction_coords:
                print("O", end='')
            else:
                print(".", end='')
        print()
    return possible_loops, possible_obstruction_coords


def check_x_in_possible_obstruction_coords(possible_obstruction_coords, x):
    for coords in possible_obstruction_coords:
        if coords[0] == x:
            return True
    return False


def check_y_in_possible_obstruction_coords(possible_obstruction_coords, y):
    for coords in possible_obstruction_coords:
        if coords[1] == y:
            return True
    return False


def create_coords_vertices_and_start_point(map_guard, N, M):
    coords_vertices = dict()

    x, y = 0, 0

    for i in range(N):
        for j in range(M):
            if map_guard[i][j] == '.':
                coords_vertices[(j, i)] = False
            elif map_guard[i][j] == '#':
                coords_vertices[(j, i)] = '#'
            elif map_guard[i][j] == '^':
                x, y = j, i
                coords_vertices[(j, i)] = True

    return coords_vertices, x, y


if __name__ == '__main__':
    map_guard = []

    with open("example.txt") as f:
        for line in f:
            map_guard.append(line.strip())

    print(part_one(map_guard))
    print(part_two(map_guard))
