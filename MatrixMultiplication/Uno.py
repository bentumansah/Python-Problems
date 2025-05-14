def array_mult(A, B):
    # Get the number of rows and columns for the resulting matrix
    rows_A = len(A)
    cols_A = len(A[0]) if rows_A > 0 else 0
    rows_B = len(B)
    cols_B = len(B[0]) if rows_B > 0 else 0

    # Initialize the result matrix with zeros
    result = []
    for i in range(rows_A):
        result_row = []
        for j in range(cols_B):
            sum_product = 0
            for k in range(cols_A):
                sum_product += A[i][k] * B[k][j]
            result_row.append(sum_product)
        result.append(result_row)
    return result