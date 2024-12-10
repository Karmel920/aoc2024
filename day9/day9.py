def part_one(disk_map):
    check_sum = 0
    blocks = []
    id_ = 0

    for i, sign in enumerate(disk_map):
        if i % 2 == 0:
            for _ in range(int(sign)):
                blocks.append(id_)
            id_ += 1
        else:
            for _ in range(int(sign)):
                blocks.append('.')

    print(blocks[:200])

    k = len(blocks) - 1

    for i in range(len(blocks)):
        if i >= k:
            print(i, k)
            break
        if blocks[i] == '.':
            while blocks[k] == '.':
                k -= 1
            if i >= k:
                break
            blocks[i], blocks[k] = blocks[k], blocks[i]


    print(blocks[49797: 49805])


    for i, id_ in enumerate(blocks):
        if id_ == '.':
            break
        check_sum += i * id_
        
    return check_sum


def part_two():
    pass

if __name__ == '__main__':
    disk_map = ''

    with open('input.txt') as f:
        disk_map = f.read().strip()

    # print(disk_map)
    print(part_one(disk_map))
    # print(part_two())
