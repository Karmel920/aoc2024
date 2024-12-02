from collections import Counter

def part_one(left, right):
    left.sort()
    right.sort()

    distances_sum = 0
    i = 0
    while i < len(left):
        distances_sum += abs(left[i] - right[i])
        i += 1
    return distances_sum


def part_two(left, right):
    right_counter = Counter(right)
    similarity_score = 0
    for id in left:
        similarity_score += id * right_counter[id]
    return similarity_score


if __name__ == '__main__':

    left, right = [], []
    with open('input.txt') as f:
        for line in f:
            left_id, right_id = line.split('   ')
            left.append(int(left_id))
            right.append(int(right_id))

    print(part_one(left, right))
    print(part_two(left, right))