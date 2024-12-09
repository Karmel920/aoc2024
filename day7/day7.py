global_results = []
global_results_part_two = []

def part_one(values, equations):
    total_calibration_result = 0

    global global_results

    for value, numbers in zip(values, equations):
        i = len(numbers) - 1

        check_numbers(i, value, value, numbers)

        if len(global_results) > 0:
            total_calibration_result += global_results[0]
            global_results = []
            
    return total_calibration_result
            

def check_numbers(i, temp_value, value, numbers):
    if i == 0:
        if numbers[0] == temp_value:
            global_results.append(value)
        return
    
    if temp_value % numbers[i] == 0:
        check_numbers(i - 1, temp_value / numbers[i], value, numbers)
    check_numbers(i - 1, temp_value - numbers[i], value, numbers)
    

def part_two(values, equations):
    total_calibration_result = 0

    global global_results_part_two

    for value, numbers in zip(values, equations):
        i = 1

        check_numbers_part_two(i, numbers[0], value, numbers)

        if len(global_results_part_two) > 0:
            total_calibration_result += global_results_part_two[0]
            global_results_part_two = []
            
    return total_calibration_result


def check_numbers_part_two(i, temp_value, value, numbers):
    if i == len(numbers):
        if temp_value == value:
            global_results_part_two.append(value)
        return
    
    check_numbers_part_two(i + 1, temp_value * numbers[i], value, numbers)
    check_numbers_part_two(i + 1, temp_value + numbers[i], value, numbers)
    check_numbers_part_two(i + 1, int(str(temp_value) + str(numbers[i])), value, numbers)


if __name__ == '__main__':
    equations = []
    values = []

    with open('input.txt') as f:
        for line in f:
            value, numbers = line.split(':')
            numbers = numbers.strip().split(' ')
            numbers = [int(x) for x in numbers]
            values.append(int(value))
            equations.append(numbers)

    print(part_one(values, equations))
    print(part_two(values, equations))
