def part_one(configurations):
    tokens = 0

    for configuration in configurations:
        count = 100

        a_press_count = 0
        b_press_count = 0

        x_a = configuration[0][0]
        x_b = configuration[1][0]
        x_prize = configuration[2][0]
        y_a = configuration[0][1]
        y_b = configuration[1][1]
        y_prize = configuration[2][1]

        while x_b * count > x_prize and y_b * count > y_prize:
            count -= 1

        while count > 0:
            diff_x = x_prize - (x_b * count)
            diff_y = y_prize - (y_b * count)
            if diff_x < 0 or diff_y < 0:
                count -= 1
                continue

            if diff_x % x_a == 0 and diff_y % y_a == 0:
                b_press_count = count
                a_press_count = diff_x // x_a
                if b_press_count * x_b + a_press_count * x_a == x_prize and b_press_count * y_b + a_press_count * y_a == y_prize:
                    break
                else:
                    b_press_count = 0
                    a_press_count = 0
            count -= 1

        if a_press_count > 100:
            a_press_count = 0
            b_press_count = 0

        if a_press_count != 0 and b_press_count != 0:
            print(f"A:{(x_a, y_a)} B:{(x_b, y_b)} {a_press_count} {b_press_count} Prize:{(x_prize, y_prize)} Calculate prize: {(a_press_count*x_a + b_press_count*x_b, a_press_count*y_a + b_press_count*y_b) == (x_prize, y_prize)}")

        tokens += 3 * a_press_count + b_press_count

    return tokens


def part_two(configurations):
    pass


if __name__ == '__main__':
    configurations = []

    with open('input.txt') as f:
        configuration = []
        for line in f:
            if line == '\n':
                configurations.append(configuration)
                configuration = []
                continue
            _, coords = line.split(':')
            x, y = coords.replace(" ", "").split(',')
            configuration.append((int(x[2:]), int(y[2:])))

    print(configurations)
    print(part_one(configurations))
    # print(part_two(configurations))
