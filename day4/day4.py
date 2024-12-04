def part_one(word_search):
    result = 0

    N = len(word_search)
    M = len(word_search[0])

    for i in range(N):
        for j in range(M):
            if word_search[i][j] != 'X':
                continue

            letters_set = set()

            # to left
            if j - 3 >= 0:
                if word_search[i][j - 1] == 'M' and word_search[i][j - 2] == 'A' and word_search[i][j - 3] == 'S':
                    result += 1

            # for k in range(j - 1, -1, -1):
            #     if word_search[i][k] == 'M' and len(letters_set) == 0:
            #         letters_set.add('M')
            #     elif word_search[i][k] == 'A' and len(letters_set) == 1:
            #         letters_set.add('A')
            #     elif word_search[i][k] == 'S' and len(letters_set) == 2:
            #         result += 1
            #         letters_set.clear()
            #         break

            # to right
            if j + 3 < M:
                if word_search[i][j + 1] == 'M' and word_search[i][j + 2] == 'A' and word_search[i][j + 3] == 'S':
                    result += 1

            # for k in range(j + 1, M, 1):
            #     if word_search[i][k] == 'M' and len(letters_set) == 0:
            #         letters_set.add('M')
            #     elif word_search[i][k] == 'A' and len(letters_set) == 1:
            #         letters_set.add('A')
            #     elif word_search[i][k] == 'S' and len(letters_set) == 2:
            #         result += 1
            #         letters_set.clear()
            #         break

            # to up
            if i - 3 >= 0:
                if word_search[i - 1][j] == 'M' and word_search[i - 2][j] == 'A' and word_search[i - 3][j] == 'S':
                    result += 1

            # for k in range(i - 1, -1, -1):
            #     if word_search[k][j] == 'M' and len(letters_set) == 0:
            #         letters_set.add('M')
            #     elif word_search[k][j] == 'A' and len(letters_set) == 1:
            #         letters_set.add('A')
            #     elif word_search[k][j] == 'S' and len(letters_set) == 2:
            #         result += 1
            #         letters_set.clear()
            #         break

            # to down
            if i + 3 < N:
                if word_search[i + 1][j] == 'M' and word_search[i + 2][j] == 'A' and word_search[i + 3][j] == 'S': 
                    result += 1

            # for k in range(i + 1, N, 1):
            #     if word_search[k][j] == 'M' and len(letters_set) == 0:
            #         letters_set.add('M')
            #     elif word_search[k][j] == 'A' and len(letters_set) == 1:
            #         letters_set.add('A')
            #     elif word_search[k][j] == 'S' and len(letters_set) == 2:
            #         result += 1
            #         letters_set.clear()
            #         break

            # to up left
            if i - 3 >= 0:
                if word_search[i - 1][i - 1] == 'M' and word_search[i - 2][i - 2] == 'A' and word_search[i - 3][i - 3] == 'S':
                    result += 1

            # for k in range(i - 1, -1, -1):
            #     if word_search[k][k] == 'M' and len(letters_set) == 0:
            #         letters_set.add('M')
            #     elif word_search[k][k] == 'A' and len(letters_set) == 1:
            #         letters_set.add('A')
            #     elif word_search[k][k] == 'S' and len(letters_set) == 2:
            #         letters_set.add('S')
            #         result += 1
            #         letters_set.clear()
            #         break

            # to up right
            if i - 3 >= 0 and M - i - 4 < M:
                if word_search[i - 1][M - 1 - i - 1] == 'M' and word_search[i - 2][M - i - 3] == 'A' and word_search[i - 3][M - i - 4] == 'S':
                    result += 1

            # for k in range(i - 1, -1, -1):
            #     if word_search[k][M - 1 - k] == 'M' and len(letters_set) == 0:
            #         letters_set.add('M')
            #     elif word_search[k][M - 1 - k] == 'A' and len(letters_set) == 1:
            #         letters_set.add('A')
            #     elif word_search[k][M - 1 - k] == 'S' and len(letters_set) == 2:
            #         letters_set.add('S')
            #         result += 1
            #         letters_set.clear()
            #         break

            # to down left
            if j - 3 >= 0 and N - j - 4 < N:
                if word_search[N - j - 2][j - 1] == 'M' and word_search[N - j - 3][j - 2] == 'A' and word_search[N - j - 4][j - 3] == 'S':
                    result += 1

            # for k in range(j - 1, -1, -1):
            #     if word_search[N - 1 - k][k] == 'M' and len(letters_set) == 0:
            #         letters_set.add('M')
            #     elif word_search[N - 1 - k][k] == 'A' and len(letters_set) == 1:
            #         letters_set.add('A')
            #     elif word_search[N - 1 - k][k] == 'S' and len(letters_set) == 2:
            #         letters_set.add('S')
            #         result += 1
            #         letters_set.clear()
            #         break

            # to down right
            if i + 3 < N:
                if word_search[i + 1][i + 1] == 'M' and word_search[i + 2][i + 2] == 'A' and word_search[i + 3][i + 3] == 'S':
                    result += 1

            # for k in range(i + 1, N, 1):
            #     if word_search[k][k] == 'M' and len(letters_set) == 0:
            #         letters_set.add('M')
            #     elif word_search[k][k] == 'A' and len(letters_set) == 1:
            #         letters_set.add('A')
            #     elif word_search[k][k] == 'S' and len(letters_set) == 2:
            #         letters_set.add('S')
            #         result += 1
            #         letters_set.clear()
            #         break

    return result


def part_two():
    pass


if __name__ == '__main__':
    
    word_search = []
    with open('example.txt') as f:
        for line in f:
            row = list(line.strip())
            word_search.append(row)
    print(len(word_search), len(word_search[0]))

    print(part_one(word_search))
    # print(part_two())
