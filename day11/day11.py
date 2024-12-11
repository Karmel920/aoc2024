from functools import lru_cache

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

        i += 1

    return len(stones)


def part_two(stones, iterations=25):
    return part_one(stones, iterations)


def part_two_recurrence(stones, iterations=25):
    stones_counter = 0

    for stone in stones:
        stones_counter += blink(stone, iterations - 1)

    return stones_counter


@lru_cache(maxsize=None)
def blink(stone, iteration):

    if iteration == -1:
        return 1
    
    if stone == 0:
        return blink(1, iteration - 1)

    elif len(str(stone)) % 2 == 0:
        return blink(int(str(stone)[:len(str(stone)) // 2]), iteration - 1) + blink(int(str(stone)[len(str(stone)) // 2:]), iteration - 1)

    else:
        return blink(stone * 2024, iteration - 1)


if __name__ == '__main__':

    with open('input.txt') as f:
        stones = list(map(int, f.read().strip().split(" ")))

    print(part_one(stones))
    # print(part_two(stones))
    print(part_two_recurrence(stones, iterations=75))