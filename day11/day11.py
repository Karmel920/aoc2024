stones_counter = 0

def part_one(stones, iterations=25):
    i = 0
    while i < iterations:
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stones.append(int(str(stone)[:len(str(stone)) // 2]))
                new_stones.append(int(str(stone)[len(str(stone)) // 2:]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones

        print(f"koniec iteracji {i + 1}, dlugosc listy: {len(stones)}")

        i += 1

    return len(stones)


def part_two(stones, iterations=30):
    return part_one(stones, iterations)


def part_two_recurrence(stones, iterations=30):
    global stones_counter

    for stone in stones:
        stones_counter += 1
        part_two_recurrence(stone, iterations - 1)

    return stones_counter


def part_two_recurrence(stone, iteration):
    global stones_counter

    if iteration == -1:
        return
    
    if stone == 0:
        part_two_recurrence(1, iteration - 1)

    elif len(str(stone)) % 2 == 0:
        stones_counter += 1
        part_two_recurrence(int(str(stone)[:len(str(stone)) // 2]), iteration - 1)
        part_two_recurrence(int(str(stone)[len(str(stone)) // 2:]), iteration - 1)

    else:
        part_two_recurrence(stone * 2024, iteration - 1)


if __name__ == '__main__':

    with open('example.txt') as f:
        stones = list(map(int, f.read().strip().split(" ")))

    print(part_one(stones))
    print(part_two(stones))