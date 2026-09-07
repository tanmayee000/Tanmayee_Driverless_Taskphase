def multiply(A, B):
    
    if len(A[0]) != len(B):
        print("Matrix multiplication isn't possible.")
        return

    
    C = [[0] * len(B[0]) for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    print(C)


A = [[1, 2],[3, 4]]
B = [[5, 6],[7, 8]]
multiply(A, B)
