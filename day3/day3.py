import re

def part_one(multiplications):
    result = 0
    for multiplication in multiplications:
        multiplication = multiplication.lstrip('mul(').rstrip(')')
        left, right = multiplication.split(',')
        result += int(left) * int(right)
    return result


def part_two(multiplications):
    result = 0
    do_not_flag = False

    for multiplication in multiplications:

        if multiplication.startswith("don't"):
            do_not_flag = True
            continue
        elif multiplication.startswith("do"):
            do_not_flag = False
            continue

        if do_not_flag:
            continue

        multiplication = multiplication.lstrip('mul(').rstrip(')')
        left, right = multiplication.split(',')
        result += int(left) * int(right)
    return result


if __name__ == '__main__':
    
    with open('input.txt') as f:
        memory = f.read().replace("\n", "")

    regex_one = r"mul\(\d{1,3},\d{1,3}\)"
    matches_one = re.findall(regex_one, memory)

    regex_two = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
    matches_two = re.findall(regex_two, memory)

    print(part_one(matches_one))
    print(part_two(matches_two))
