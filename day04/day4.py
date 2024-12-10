def part_one(word_search):
    result = 0

    N = len(word_search)
    M = len(word_search[0])

    for i in range(N):
        for j in range(M):
            if word_search[i][j] != 'X':
                continue

            # to left
            if j - 3 >= 0:
                if word_search[i][j - 1] == 'M' and word_search[i][j - 2] == 'A' and word_search[i][j - 3] == 'S':
                    result += 1

            # to right
            if j + 3 < M:
                if word_search[i][j + 1] == 'M' and word_search[i][j + 2] == 'A' and word_search[i][j + 3] == 'S':
                    result += 1

            # to up
            if i - 3 >= 0:
                if word_search[i - 1][j] == 'M' and word_search[i - 2][j] == 'A' and word_search[i - 3][j] == 'S':
                    result += 1

            # to down
            if i + 3 < N:
                if word_search[i + 1][j] == 'M' and word_search[i + 2][j] == 'A' and word_search[i + 3][j] == 'S': 
                    result += 1

            # to up left
            if i - 3 >= 0 and j - 3 >= 0:
                if word_search[i - 1][j - 1] == 'M' and word_search[i - 2][j - 2] == 'A' and word_search[i - 3][j - 3] == 'S':
                    result += 1

            # to up right
            if i - 3 >= 0 and j + 3 < M:
                if word_search[i - 1][j + 1] == 'M' and word_search[i - 2][j + 2] == 'A' and word_search[i - 3][j + 3] == 'S':
                    result += 1

            # to down left
            if j - 3 >= 0 and i + 3 < N:
                if word_search[i + 1][j - 1] == 'M' and word_search[i + 2][j - 2] == 'A' and word_search[i + 3][j - 3] == 'S':
                    result += 1

            # to down right
            if i + 3 < N and j + 3 < M:
                if word_search[i + 1][j + 1] == 'M' and word_search[i + 2][j + 2] == 'A' and word_search[i + 3][j + 3] == 'S':
                    result += 1

    return result


def part_two(word_search):
    result = 0

    N = len(word_search)
    M = len(word_search[0])

    for i in range(N):
        for j in range(M):
            if word_search[i][j] != 'A':
                continue

            if i - 1 >= 0 and j - 1 >= 0 and i + 1 < N and j + 1 < M:
                if ((word_search[i - 1][j - 1] == 'M' and word_search[i + 1][j + 1] == 'S') or (word_search[i - 1][j - 1] == 'S' and word_search[i + 1][j + 1] == 'M')) and \
                    ((word_search[i - 1][j + 1] == 'M' and word_search[i + 1][j - 1] == 'S') or (word_search[i - 1][j + 1] == 'S' and word_search[i + 1][j - 1] == 'M')):
                    result += 1

    return result


if __name__ == '__main__':
    
    word_search = []
    with open('input.txt') as f:
        for line in f:
            row = list(line.strip())
            word_search.append(row)

    print(part_one(word_search))
    print(part_two(word_search))
