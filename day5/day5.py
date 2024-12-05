def part_one(page_ordering, updates):
    result = 0

    for update in updates:
        pages_dict = {}
        for rule in page_ordering:
            pages_dict.setdefault(rule[0], set()).add(rule[1])
        if is_correct(pages_dict, update):
            result += update[len(update) // 2]

    return result


def part_two(page_ordering, updates):
    result = 0

    for update in updates:
        pages_dict = {}
        for rule in page_ordering:
            pages_dict.setdefault(rule[0], set()).add(rule[1])
        if not is_correct(pages_dict, update):
            make_correct_order(pages_dict, update)
            result += update[len(update) // 2]

    return result


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


def make_correct_order(pages_dict, update):
    for i in range(1, len((update))):
        if update[i - 1] in pages_dict and update[i] in pages_dict[update[i - 1]]:
            if i == len(update) - 1:
                continue
        else:
            update[i], update[i - 1] = update[i - 1], update[i]
            k = i - 1
            while k > 0:
                if update[k] in pages_dict[update[k - 1]]:
                    break
                else:
                    update[k], update[k - 1] = update[k - 1], update[k]
                    k -= 1


if __name__ == '__main__':
    page_ordering = []
    updates = []

    with open('input.txt') as f:
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
