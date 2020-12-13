import numpy as np
import re

# Translation from char to value {'#' = 1, '.' = 0,'L' = 0}
seat_translation = {35:'1',46:'0',76:'0'}

def update_dyn_matrix(char_matrix, dyn_matrix):
    dyn_matrix.append([0]*len(char_matrix))
    for i in range(1,len(char_matrix)-1):
        dyn_row = []
        for j in range(1,len(char_matrix)-1):
            dyn_row.append(check_surrounding(i,j,char_matrix))
        dyn_matrix.append([0] + dyn_row + [0])
    dyn_matrix.append([0]*len(char_matrix))

def check_row(i,start,stop,char_matrix,direction):
    surrounding_sum =0
    for k in range(start,stop,direction):
        char = char_matrix[i][k]
        if char == '.': 
            continue
        if char == '#':
            surrounding_sum += 1
            break
        if char == 'L':
            break
    return surrounding_sum

def check_column(j,start,stop,char_matrix,direction):
    surrounding_sum =0
    for k in range(start,stop,direction):
        char = char_matrix[k][j]
        if char == '.': 
            continue
        if char == '#':
            surrounding_sum += 1
            break
        if char == 'L':
            break
    return surrounding_sum

def check_diagonal(starti,startj,stopi,stopj,char_matrix,directioni,directionj):
    surrounding_sum =0
    k = starti
    l = startj
    while True:
        if k == 0 or l == 0 or k == stopi or l == stopj:
            return surrounding_sum
        char = char_matrix[k][l]
        if char == '.':
            k += 1*directioni
            l += 1*directionj
            continue
        if char == '#':
            surrounding_sum += 1
            return surrounding_sum
        if char == 'L':
            return surrounding_sum
    return surrounding_sum


def check_surrounding(i,j, char_matrix):
    surrounding_sum = 0
    seat = char_matrix[i][j]
    if seat == '.':
        return 0

    # West row
    surrounding_sum += check_row(i,j-1,0,char_matrix,-1)

    # East row
    surrounding_sum += check_row(i,j+1,len(char_matrix[i]),char_matrix,1)

    # North column
    surrounding_sum += check_column(j,i-1,0,char_matrix,-1)
    
    # South column
    surrounding_sum += check_column(j,i+1,len(char_matrix),char_matrix,1)

    # North west diagonal
    surrounding_sum += check_diagonal(i-1,j-1,0,0,char_matrix,-1,-1)

    # North east diagonal
    surrounding_sum += check_diagonal(i-1,j+1,0,len(char_matrix[i]),char_matrix,-1,1)

    # South east diagonal
    surrounding_sum += check_diagonal(i+1,j+1,len(char_matrix),len(char_matrix[i]),char_matrix,1,1)

    # South west diagonal
    surrounding_sum += check_diagonal(i+1,j-1,len(char_matrix),0,char_matrix,1,-1)

    return surrounding_sum

def update_seats(seat_matrix, dyn_matrix):
    changes = 0
    for i in range(len(seat_matrix)):
        for j in range(len(seat_matrix)):
            if seat_matrix[i][j] == 'L' and dyn_matrix[i][j] == 0:
                changes += 1
                seat_matrix[i][j] = '#'
            elif seat_matrix[i][j] == '#' and dyn_matrix[i][j] >= 5:
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