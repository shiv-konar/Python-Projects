import numpy as np

mult_table = [[0] * 10 for i in range(10) ]
print np.matrix(mult_table)
for i in range(0, 10):
    for j in range(0, 10):
        mult_table[i][j] = (i + 1) * (j + 1)

print np.matrix(mult_table)