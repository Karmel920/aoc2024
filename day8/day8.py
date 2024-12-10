def part_one(antennas_coords, N, M):
    antinodes = set()

    for antenna, coords in antennas_coords.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                diff_x = coords[i][0] - coords[j][0]
                diff_y = coords[i][1] - coords[j][1]

                antinode_position_i = [coords[i][0], coords[i][1]]
                antinode_position_j = [coords[j][0], coords[j][1]]

                #coord[i] on left or right
                antinode_position_i[0] += diff_x
                antinode_position_j[0] -= diff_x

                #coord[i] on top
                if diff_y < 0:
                    antinode_position_i[1] += diff_y
                    antinode_position_j[1] -= diff_y

                #coord[i] on down
                if diff_y > 0:
                    antinode_position_i[1] -= diff_y
                    antinode_position_j[1] += diff_y

                if 0 <= antinode_position_i[0] < N and 0 <= antinode_position_i[1] < M:
                    antinodes.add(tuple(antinode_position_i))
                if 0 <= antinode_position_j[0] < N and 0 <= antinode_position_j[1] < M:
                    antinodes.add(tuple(antinode_position_j))

    return len(antinodes)


def part_two(antennas_coords, N, M):
    antinodes = set()

    for antenna, coords in antennas_coords.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords)):
                diff_x = coords[i][0] - coords[j][0]
                diff_y = coords[i][1] - coords[j][1]

                antinodes.add(coords[i])
                antinodes.add(coords[j])

                antinode_position_i = [coords[i][0], coords[i][1]]
                antinode_position_j = [coords[j][0], coords[j][1]]

                #coord[i] on left or right
                antinode_position_i[0] += diff_x
                antinode_position_j[0] -= diff_x

                #coord[i] on top
                if diff_y < 0:
                    antinode_position_i[1] += diff_y
                    antinode_position_j[1] -= diff_y

                #coord[i] on down
                if diff_y > 0:
                    antinode_position_i[1] -= diff_y
                    antinode_position_j[1] += diff_y

                if 0 <= antinode_position_i[0] < N and 0 <= antinode_position_i[1] < M:
                    antinodes.add(tuple(antinode_position_i))
                if 0 <= antinode_position_j[0] < N and 0 <= antinode_position_j[1] < M:
                    antinodes.add(tuple(antinode_position_j))


                while 0 <= antinode_position_i[0] < N and 0 <= antinode_position_i[1] < M or 0 <= antinode_position_j[0] < N and 0 <= antinode_position_j[1] < M:
                    #coord[i] on left or right
                    antinode_position_i[0] += diff_x
                    antinode_position_j[0] -= diff_x

                    #coord[i] on top
                    if diff_y < 0:
                        antinode_position_i[1] += diff_y
                        antinode_position_j[1] -= diff_y

                    #coord[i] on down
                    if diff_y > 0:
                        antinode_position_i[1] -= diff_y
                        antinode_position_j[1] += diff_y

                    if 0 <= antinode_position_i[0] < N and 0 <= antinode_position_i[1] < M:
                        antinodes.add(tuple(antinode_position_i))
                    if 0 <= antinode_position_j[0] < N and 0 <= antinode_position_j[1] < M:
                        antinodes.add(tuple(antinode_position_j))

    return len(antinodes)


if __name__ == '__main__':
    antennas_coords = {}
    N, M = 0, 0

    with open('input.txt') as f:
        for y, line in enumerate(f):
            N += 1
            M = len(line.strip())
            for x, sign in enumerate(line.strip()):
                if sign != '.':
                    antennas_coords.setdefault(sign, list()).append((x,y))

    print(part_one(antennas_coords, N, M))
    print(part_two(antennas_coords, N, M))
