def spiral(m, start_r, start_c, end_r, end_c):

    if start_r > end_r or start_c > end_c:
        return

    for j in range(start_c, end_c):
        print(m[start_r][j])

    for i in range(start_r, end_r-1):
        print(m[i+1][end_c-1])

    if start_r != end_r-1:
        for j in range(end_c-2, start_c-1, -1):
            print(m[end_r-1][j])

    if start_c != end_c-1:
        for i in range(end_r-2, start_r, -1):
            print(m[i][start_c])

    spiral(m, start_r+1, start_c+1, end_r-1, end_c-1)


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
        ]

print(spiral(matrix, 0, 0, len(matrix), len(matrix[0])))

## How to store in array, with a recursive function?