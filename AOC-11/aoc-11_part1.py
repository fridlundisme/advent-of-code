import numpy as np
import re

# Translation from char to value {'#' = 1, '.' = 0,'L' = 0}
seat_translation = {35:'1',46:'0',76:'0'}

def update_dyn_matrix(values_matrix, dyn_matrix):
    dyn_matrix.append([0]*len(values_matrix))
    for i in range(1,len(values_matrix)-1):
        dyn_row = []
        for j in range(1,len(values_matrix)-1):
            dyn_row.append(check_surrounding(i,j,values_matrix))
        dyn_matrix.append([0] + dyn_row + [0])
    dyn_matrix.append([0]*len(values_matrix))

def check_surrounding(i,j, values_matrix):
    surrounding_sum = 0
    for k in range(-1,2):
        for l in range(-1,2):
            if k == 0 and l == 0:
                continue
            seat_value = int(values_matrix[i+k][j+l].translate(seat_translation))
            seat_type = values_matrix[i+k][j+l]
            surrounding_sum += seat_value
    return surrounding_sum

def update_seats(seat_matrix, dyn_matrix):
    changes = 0
    for i in range(len(seat_matrix)):
        for j in range(len(seat_matrix)):
            if seat_matrix[i][j] == 'L' and dyn_matrix[i][j] == 0:
                changes += 1
                seat_matrix[i][j] = '#'
            elif seat_matrix[i][j] == '#' and dyn_matrix[i][j] >= 4:
                changes += 1
                seat_matrix[i][j] = 'L'
            
    # for row in seat_matrix:
    #     for c in row:
    #         print(c,end='')
    #     print()
    # print("/"*len(seat_matrix))
    return False if changes > 0 else True, seat_matrix

def main():
    seat_matrix_chars = []
    zero_line = []
    floor_line = []
    floor = [int('.'.translate(seat_translation))]
    with open("input.in") as input_file:
        for line in input_file.readlines():
            if len(seat_matrix_chars) == 0:
                floor_line = ['.']*(len(line)+1)
                seat_matrix_chars.append(floor_line)
            seat_matrix_chars.append(['.'] + [c for c in line if c != '\n'] + ['.'])
    seat_matrix_chars.append(floor_line)

    no_seat_change = False
    while not no_seat_change:
        dyn_matrix = []
        # Reset dyn_matrix
        update_dyn_matrix(seat_matrix_chars,dyn_matrix)
        no_seat_change, seat_matrix_chars = update_seats(seat_matrix_chars, dyn_matrix)
        pass
    os = 0
    for row in seat_matrix_chars:
        # Sum up all of the '#' (1 occupied seat) in each line/row
        os += sum(1 if re.match('#',x) else 0 for x in row)
    print("Occupied seats: ",os)

if __name__ == "__main__":
    main()