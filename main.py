from operator import add
import sys
#Dim-Input from user
row = int(input("Enter the number of rows to the matrix: "))
col = int(input("Enter the number of columns to the matrix: "))

#Check for invalid dimensions
if row > col:
    sys.exit("ERROR: Invalid dimension")
else:
    print("Valid dimension:")

#Element-Input from user
matrix = []
r = 1
c = 1
for x in range(0, row):
    tempRowList = []
    for y in range(0, col):
        d = float(input("Enter a value for d({}, {}): ".format(r,c)))
        tempRowList.append(d)
        c+=1
    matrix.append(tempRowList)
    r+=1
    c = 1

#Checking for Zeros; if there is a zero where there should be piv-element, it performs a row-swap
j = 0
while j != row:
    if matrix[j][j] == 0:
        matrix[j-1], matrix[j] = matrix[j], matrix[j-1]
    else:
        j+=1

#"Gaussing" downwards
for x in range(0, row):
    for t in range(x+1, row):
        k = -1*(matrix[t][x]/matrix[x][x])
        prevRowTemp = [i * k for i in matrix[x]]
        matrix[t] = list(map(add, matrix[t], prevRowTemp))

#"Gaussing" upwards
j = row - 2
for x in range(row-1, 0, -1):
    for t in range(j, -1, -1):
        k = -1*(matrix[t][x]/matrix[x][x])
        prevRowTemp = [i * k for i in matrix[x]]
        matrix[t] = list(map(add, matrix[t], prevRowTemp))
    j-=1

#Fine tuning. Making sure that the pivot elements are equal to one
for x in range(0, row):
    if matrix[x][x] != 1:    
        matrix[x][:] = [i/matrix[x][x] for i in matrix[x]]    

map(int, matrix)

print("The matrix' reduced row echelon form is:")
for x in range(0, row):
    print(matrix[x])
