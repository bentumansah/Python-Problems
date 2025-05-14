## TASK:

Write a function (array_mult) that takes two 2D arrays and performs a matrix multiplication, return a new 2D array. Each array should be represented as a list of lists, i.e., as a list of rows, as discussed earlier.

## EXAMPLE:

> > > M1 = [[1, 2, 3], [-2, 3, 7]]
> > > M2 = [[1,0,0],[0,1,0],[0,0,1]]
> > > array_mult(M1, M2)
> > > [[1, 2, 3], [-2, 3, 7]]

> > > M3 = [[1], [0], [-1]]
> > > array_mult(M1, M3)
> > > [[-2], [-9]]

## BREAKDOWN:

# 1ST APPROACH:

Matrix Dimensions: The first matrix (A) has dimensions m x n, and the second matrix (B) has dimensions n x p. The resulting matrix will have dimensions m x p.

Dot Product Calculation: For each element in the resulting matrix, compute the dot product of the corresponding row from matrix A and column from matrix B. This involves multiplying corresponding elements and summing the products.

Nested Loops: Use nested loops to iterate over each row of matrix A, each column of matrix B, and each element within the rows and columns to compute the dot product.

# MORE INTO IT

Matrix Dimensions: The function first determines the dimensions of the input matrices.The number of rows in the result is the same as the number of rows in matrix A, and the number of columns in the result is the same as the number of columns in matrix B.

Result Initialization: The result matrix is initialized as an empty list. For each row in matrix A, a new row is created in the result matrix.

Dot Product Calculation: For each element in the result matrix (at position [i][j]), the dot product is computed by iterating over the elements of the corresponding row in matrix A and column in matrix B. This is done using a nested loop where the innermost loop calculates the sum of the products of corresponding elements.

# Efficiency:

The time complexity of this approach is O(m*n*p), where m, n, and p are the dimensions of the matrices. This is the standard complexity for matrix multiplication and ensures that each element is processed correctly.

This approach efficiently handles the matrix multiplication using nested loops and dot product calculation, ensuring correctness and clarity.

## DYNAMISM:

# 2ND APPROACH:

Transpose the Second Matrix: Convert the columns of the second matrix (B) into rows using the zip function. This allows us to access columns of B as rows in the transposed matrix (B_T).

Compute Dot Products with List Comprehensions: For each row in the first matrix (A), compute the dot product with each row in the transposed matrix (B_T), which corresponds to the original columns of B. This is done using nested list comprehensions, making the code concise and readable.

# MORE INTO IT

Transposing the Matrix: The zip(\*B) function transposes matrix B, converting its columns into rows. Each resulting tuple from zip is converted to a list to facilitate element-wise operations.

List Comprehensions:

The outer list comprehension iterates over each row in matrix A.

The inner list comprehension iterates over each transposed column (now a row in B_T) of matrix B.

For each pair of rows (from A and B_T), the dot product is calculated using sum(a \* b for a, b in zip(row_A, col_B)), which sums the products of corresponding elements.

This approach efficiently handles the matrix multiplication with a time complexity of O(m*n*p), where m, n, and p are the dimensions of the matrices involved. The use of list comprehensions and transposing makes the code concise and leverages Python's capabilities for clean and readable implementations.
