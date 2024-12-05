def part_one(page_ordering, updates):
    result = 0

    for update in updates:
        pages_dict = {}
        for rule in page_ordering:
            pages_dict.setdefault(rule[0], set()).add(rule[1])
        if is_correct(pages_dict, update):
            result += update[len(update) // 2]

    return result


def part_two():
    pass


def is_correct(pages_dict, update):
    for i in range(1, len((update))):
        if update[i] in pages_dict[update[i - 1]]:
            if i == len(update) - 1:
                continue
            if update[i] not in pages_dict:
                return False
        else:
            return False
    return True


if __name__ == '__main__':
    page_ordering = []
    updates = []

    with open('example.txt') as f:
        for line in f:
            if '|' in line:
                x, y = line.split('|')
                page_ordering.append((int(x), int(y)))
            elif ',' in line:
                update = line.split(',')
                update = [int(x) for x in update]
                updates.append(update)

    print(part_one(page_ordering, updates))
    print(part_two(page_ordering, updates))
