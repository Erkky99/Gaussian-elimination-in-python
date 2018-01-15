from operator import add
import sys
#Dim-Input from user
row = int(input("Number of rows: "))
col = int(input("Number of columns: "))

#Check for invalid dimensions (These shouldn't actually be invalid, with proper functionality)
if row > col:
    sys.exit("ERROR: Invalid dimensions")

#Element-Input from user
matrix = []
r = 1
c = 1
for x in range(0, row):
    tempRowList = []
    for y in range(0, col):
        d = int(input("Value of d({}, {}): ".format(r,c)))
        tempRowList.append(d)
        c += 1
    matrix.append(tempRowList)
    r += 1
    c = 1

oMatrix = list(matrix)

#Checking for Zeroes; if there is a zero where there should be piv-element, it performs a row-swap

j = 0
while j != row:
    if matrix[j][j] == 0:
        matrix[j-1], matrix[j] = matrix[j], matrix[j-1]
    else:
        j+=1

#"Gaussing" downwards
t = 0
j = 1
l = 0

for x in range(0, row - 1):
    while t != row-1:
        k = -matrix[j][l] / matrix[l][l]
        prevRowTemp = [i * k for i in matrix[l]]
        matrix[j] = list(map(add, matrix[j], prevRowTemp))

        t += 1
        j += 1
    t -= 1
    j -= 1
    l += 1

#"Gaussing" upwards
t = row - 1
j = row - 2
l = row - 1
for x in range(row - 1, 0, - 1):
    while t != 0:
        k = -matrix[j][l] / matrix[l][l]
        prevRowTemp = [i * k for i in matrix[l]]
        matrix[j] = list(map(add, matrix[j], prevRowTemp))

        j -= 1
        t -= 1
    t += 1
    j += 1
    l -= 1

#Fine tuning. Making sure that the pivot elements are equal to one
j = 0
for x in range(0, row):
    if matrix[j][j] != 1:    
        matrix[j][:] = [i / matrix[j][j] for i in matrix[j]]
    j + 1    

map(int, matrix)

print("The matrix in row echelon form:")

for x in range(0, row):
    print(matrix[x])
