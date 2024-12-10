print ('Transposing a Matrix of values using the ZIP function')

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
transposed = list(zip(*matrix))

print ("Original Matrix:")
for I in range(len(matrix)):
    print (matrix[I])
# output:
# [1,2,3],
# [4,5,6],
# [7,8,9]

print ("Transposed:")
for I in range(len(transposed)):
    print (transposed[I])
# output:
# [1,4,7]
# [2,5,8]
# [7,8,9]


