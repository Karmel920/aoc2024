def part_one(reports):
    safe_count = 0

    for report in reports:
        if is_safe(report):
            safe_count += 1

    return safe_count


def is_safe(report):
    is_increasing = False

    if report[0] < report[1]:
        is_increasing = True

    if is_increasing:
        for i in range(len(report) - 1):
            if not 1 <= (report[i + 1] - report[i]) <= 3:
                return False
    else:
        for i in range(len(report) - 1):
            if not 1 <= (report[i] - report[i + 1]) <= 3:
                return False
    return True


def part_two(reports):
    safe_count = 0

    for report in reports:
        for i in range(0, len(report)):
            sliced_report = report[:i] + report[i + 1:]
            if is_safe(sliced_report):
                safe_count += 1
                break

    return safe_count


if __name__ == '__main__':
    reports = []
    with open('input.txt') as f:
        for line in f:
            levels = line.split(' ')
            levels = [int(x) for x in levels]
            reports.append(levels)

    print(part_one(reports))
    print(part_two(reports))