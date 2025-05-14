def array_mult(A, B):
    # Transpose B to access columns as rows
    B_T = [list(col) for col in zip(*B)]
    # Compute matrix multiplication using list comprehensions
    return [
        [sum(a * b for a, b in zip(row_A, col_B)) for col_B in B_T] 
        for row_A in A
        ]
    