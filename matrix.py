#!/usr/bin/python3

N_ROWS = 100
N_COLS = 100
N_MATS = 100

def init_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(0)
    
    return matrix

def add_matrix(dest, src, rows, cols):
    for i in range(rows):
        for j in range(cols):
            dest[i][j] += src[i][j]

def get_grand_sum(mat, rows, cols):
    # TODO: Write this
    return 0

if __name__ == '__main__':
    mat = init_matrix(N_ROWS, N_COLS)

    for mats in range(N_MATS):
        new_mat = init_matrix(N_ROWS, N_COLS)

        for j in range(N_COLS):
            for i in range(N_ROWS):
                new_mat[i][j] = int(input())
        
        add_matrix(mat, new_mat, N_ROWS, N_COLS)

    print("Grand sum: " + str(get_grand_sum(mat, N_ROWS, N_COLS)))
