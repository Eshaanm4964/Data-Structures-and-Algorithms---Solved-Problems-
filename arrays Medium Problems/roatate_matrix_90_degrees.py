def rotate_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(i+1,n):
            matrix[i],matrix[j] = matrix[j],matrix[i]
    for i in range(n):
        matrix.reverse(i)