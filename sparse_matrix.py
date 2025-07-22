# sparse-matrix
import numpy as np
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
elements = list(map(int, input("Enter the elements row-wise: ").split()))
np_matrix = np.array(elements).reshape(rows, cols)
print(np_matrix)
c=0
for element in np_matrix.flat:
  if element==0:
    c+=1
if c > rows*cols/2:
  print("Sparse Matrix")
else: print("Not A Sparse Matrix")
