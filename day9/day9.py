def part_one(disk_map):
    check_sum = 0

    blocks = create_blocks(disk_map)

    k = len(blocks) - 1

    for i in range(len(blocks)):
        if blocks[i] == '.':
            while blocks[k] == '.':
                k -= 1
            if i >= k:
                break
            blocks[i], blocks[k] = blocks[k], blocks[i]

    for i, id_ in enumerate(blocks):
        if id_ == '.':
            break
        check_sum += i * id_
        
    return check_sum


def part_two(disk_map):
    check_sum = 0

    blocks = create_blocks(disk_map)

    k = len(blocks) - 1

    spaces = []

    start = None

    for i, block in enumerate(blocks):
        if block == '.' and not start:
            start = i
        if block != '.' and start:
            spaces.append((start, i - 1, i - start))
            start = None

    i = 0

    while spaces[0][0] <= k:
        while blocks[k] == '.':
            k -= 1
        current_id = blocks[k]
        start_current_id = k
        length_of_current_ids = 1
        k -= 1

        while blocks[k] == current_id:
            k -= 1
            length_of_current_ids += 1

        for space in spaces:
            if space[2] >= length_of_current_ids:
                if space[0] <= k:
                    for j in range(length_of_current_ids):
                        blocks[space[0] + j], blocks[start_current_id - j] = blocks[start_current_id - j], blocks[space[0] + j]
                    spaces.remove(space)
                    break

        spaces = []
        start = None
        for i, block in enumerate(blocks):
            if block == '.' and not start:
                start = i
            if block != '.' and start:
                spaces.append((start, i - 1, i - start))
                start = None

    for i, id_ in enumerate(blocks):
        if id_ == '.':
            continue
        check_sum += i * id_

    return check_sum


def create_blocks(disk_map):
    blocks_ = []
    id_ = 0

    for i, sign in enumerate(disk_map):
        if i % 2 == 0:
            for _ in range(int(sign)):
                blocks_.append(id_)
            id_ += 1
        else:
            for _ in range(int(sign)):
                blocks_.append('.')

    return blocks_


if __name__ == '__main__':
    with open('input.txt') as f:
        disk_map = f.read().strip()

    print(part_one(disk_map))
    print(part_two(disk_map))
