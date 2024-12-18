visited_coords = set()
perimeter_coords = list()

def part_one(gardens):
    global visited_coords

    price = 0

    N = len(gardens)

    for y, row in enumerate(gardens):
        for x, garden in enumerate(row):
            if (y, x) not in visited_coords:
                plant = garden
                area, perimeter = find_plot(x, y, plant, gardens, N)
                # print(f"{y, x} - {plant} area: {area} perimeter: {perimeter}")
                price += area * perimeter
    return price


def find_plot(x, y, plant, gardens, N):
    global visited_coords

    if gardens[y][x] != plant:
        return 0
    else:
        visited_coords.add((y, x))
    
    area = 1
    perimeter = 0

    if x + 1 < N:
        if (y, x + 1) not in visited_coords or ((y, x + 1) in visited_coords and gardens[y][x + 1] != plant):
            if gardens[y][x + 1] == plant:
                area_, perimeter_ = find_plot(x + 1, y, plant, gardens, N)
                area += area_
                perimeter += perimeter_
            else:
                perimeter += 1
    else:
        perimeter += 1
    if x - 1 >= 0:
        if (y, x - 1) not in visited_coords or ((y, x - 1) in visited_coords and gardens[y][x - 1] != plant):
            if gardens[y][x - 1] == plant:
                area_, perimeter_ = find_plot(x - 1, y, plant, gardens, N)
                area += area_
                perimeter += perimeter_
            else:
                perimeter += 1
    else:
        perimeter += 1
    if y + 1 < N:
        if (y + 1, x) not in visited_coords or ((y + 1, x) in visited_coords and gardens[y + 1][x] != plant):
            if gardens[y + 1][x] == plant:
                area_, perimeter_ = find_plot(x, y + 1, plant, gardens, N)
                area += area_
                perimeter += perimeter_
            else:
                perimeter += 1
    else:
        perimeter += 1
    if y - 1 >= 0:
        if (y - 1, x) not in visited_coords or ((y - 1, x) in visited_coords and gardens[y - 1][x] != plant):
            if gardens[y - 1][x] == plant:
                area_, perimeter_ = find_plot(x, y - 1, plant, gardens, N)
                area += area_
                perimeter += perimeter_
            else:
                perimeter += 1
    else:
        perimeter += 1

    return area, perimeter
        

# def part_two(gardens):
#     global visited_coords
#     global perimeter_coords

#     price = 0

#     N = len(gardens)

#     for y, row in enumerate(gardens):
#         for x, garden in enumerate(row):
#             if (y, x) not in visited_coords:
#                 plant = garden
#                 area, perimeter = find_plot_two(x, y, plant, gardens, N)
#                 sides_number = calculate_sides_number(perimeter_coords)
#                 print(f"{y, x} - {plant} area: {area} sides: {sides_number}    perimeter_coords: {perimeter_coords}")
#                 # price += area * perimeter
#                 perimeter_coords = []
#     # return price


# def calculate_sides_number(perimeter_coords):
#     already_visited = set()
#     count = 0
#     for i in range(len(perimeter_coords)):
#         if i in already_visited:
#             continue
#         current_y, current_x = perimeter_coords[i][0], perimeter_coords[i][1]
#         count += 1

#         for j in range(i + 1, len(perimeter_coords)):
#             temp_y, temp_x = perimeter_coords[j][0], perimeter_coords[j][1]
#             if current_x == temp_x and current_y != temp_y:
#                 already_visited.add(j)
#                 continue
#             elif current_x != temp_x and current_y == temp_y:
#                 already_visited.add(j)
#                 continue
#             elif current_x == temp_x and current_y == temp_y:
#                 already_visited.add(j)
#                 count += 1
#     return count


# def find_plot_two(x, y, plant, gardens, N):
#     global visited_coords
#     global perimeter_coords

#     if gardens[y][x] != plant:
#         return 0
#     else:
#         visited_coords.add((y, x))
    
#     area = 1
#     perimeter = 0

#     if x + 1 < N:
#         if (y, x + 1) not in visited_coords or ((y, x + 1) in visited_coords and gardens[y][x + 1] != plant):
#             if gardens[y][x + 1] == plant:
#                 area_, perimeter_ = find_plot_two(x + 1, y, plant, gardens, N)
#                 area += area_
#                 perimeter += perimeter_
#             else:
#                 perimeter += 1
#                 perimeter_coords.append((y, x + 1))
#     else:
#         perimeter += 1
#         perimeter_coords.append((y, x + 1))
#     if x - 1 >= 0:
#         if (y, x - 1) not in visited_coords or ((y, x - 1) in visited_coords and gardens[y][x - 1] != plant):
#             if gardens[y][x - 1] == plant:
#                 area_, perimeter_ = find_plot_two(x - 1, y, plant, gardens, N)
#                 area += area_
#                 perimeter += perimeter_
#             else:
#                 perimeter += 1
#                 perimeter_coords.append((y, x - 1))
#     else:
#         perimeter += 1
#         perimeter_coords.append((y, x - 1))
#     if y + 1 < N:
#         if (y + 1, x) not in visited_coords or ((y + 1, x) in visited_coords and gardens[y + 1][x] != plant):
#             if gardens[y + 1][x] == plant:
#                 area_, perimeter_ = find_plot_two(x, y + 1, plant, gardens, N)
#                 area += area_
#                 perimeter += perimeter_
#             else:
#                 perimeter += 1
#                 perimeter_coords.append((y + 1, x))
#     else:
#         perimeter += 1
#         perimeter_coords.append((y + 1, x))
#     if y - 1 >= 0:
#         if (y - 1, x) not in visited_coords or ((y - 1, x) in visited_coords and gardens[y - 1][x] != plant):
#             if gardens[y - 1][x] == plant:
#                 area_, perimeter_ = find_plot_two(x, y - 1, plant, gardens, N)
#                 area += area_
#                 perimeter += perimeter_
#             else:
#                 perimeter += 1
#                 perimeter_coords.append((y - 1, x))
#     else:
#         perimeter += 1
#         perimeter_coords.append((y - 1, x))

#     return area, perimeter


if __name__ == '__main__':
    gardens = []

    with open('input.txt') as f:
        for line in f:
            gardens.append(list(line.strip()))

    # for row in gardens:
    #     print(row)

    print(part_one(gardens))
    # print(part_two(gardens))