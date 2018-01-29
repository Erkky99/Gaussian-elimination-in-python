from operator import add


row = 4
col = 5

row1 = [2, 65, 32, 16, 3]
row2 = [8, 95, 2, 3, 7]
row3 = [56, 87, 0, 0, 5]
row4 = [9, 12, 23, 32, 2]

"""row1 = [0, 0, 1, 4]
row2 = [2, 0, 3, 16]
row3 = [8, -9, 0, 4]"""

matrix = [row1, row2, row3, row4]

#k = -1*(row2[0]/row1[0])

#[IMP]k = -1*(matrix[1][0]/matrix[0][0])

#[IMP]row1Temp = [i * k for i in matrix[0]]

#print(k)
#print(matrix[0])
#print(row1Temp)

#print(matrix[1])

#[IMP]matrix[1] = list(map(add, row2, row1Temp))

#print(matrix[1])

j = 0
while j != row:
    if matrix[j][j] == 0:
        print("Zero detected! Row-swap")
        matrix[j-1], matrix[j] = matrix[j], matrix[j-1]
    else:
        print("No zero detected")
        j+=1
    

"""Gaussing downwards"""
t = 0 #Counter for while loop
j = 1
l = 0
for x in range(0, row-1):
    while t != row-1:
        print(matrix)
        k = -1*(matrix[j][l]/matrix[l][l]) #Defintion of k that is needed for operation 3
        print(k)
        prevRowTemp = [i * k for i in matrix[l]] #The list of numbers that are going to be added to said row
        print(prevRowTemp)
        matrix[j] = list(map(add, matrix[j], prevRowTemp)) #(Old Row) - prevRowTemp = (new row)
        print(matrix[j])

        t+=1
        j+=1
        print("t = {}, j = {}".format(t, j))
        print("-------------")
    t-=1
    j-=1
    l+=1

print("Slutmatris (Ner): {}".format(matrix))

"""Guassing upwards"""
t = row-1
j = row-2
l = row-1
for x in range(row-1, 0, -1):
    print("Hello, World!")
    while t != 0:
        print(matrix)
        k = -1*(matrix[j][l]/matrix[l][l])
        print(k)
        prevRowTemp = [i * k for i in matrix[l]]
        print(prevRowTemp)
        matrix[j] = list(map(add, matrix[j], prevRowTemp))
        print(matrix[j])

        j-=1
        t-=1
        print("t = {}, j = {}".format(t, j))
        print("-------------")
    t+=1
    j+=1
    l-=1

print("Slutmatris (Upp): {}".format(matrix))

"""Fine tuning"""
j = 0
for x in range(0, row):
    if matrix[j][j] != 1:
        print("Something else")
        matrix[j][:] = [i/matrix[j][j] for i in matrix[j]]
        print(matrix[j][j])
    else:
        print("One")
    j+=1
    print(j)
    #print(matrix[j][j])
    print("-------------")
    
print("Slutmatris (FT): {}".format(matrix))

for x in range(0, row):
    map(int, matrix[x])

print("Den radkanoniska matrisen är:")
for x in range(0, row):
    print(matrix[x])

"""[DONE]Ought to change the 1s and 0s to variables and add one for
each iteration in a for-loop OR while-loop (matrix[i] where i
is getting added by 1 at the end of a for-loop OR while-loop).
i/t must be counted to the same value as the number of rows,
meaning that the while-loop has to be valid while i/t != row - 1
while i/t != row-1"""

"""[FALSE]If there are more than 2 rows, a new flow of intructions
are probalby needed"""

"""[DONE]If d(11) for example is 0 --> check if element is 0 
BEFORE doing any Gaussing. If the elemtent in question is 
zero a row-swap is needed!""" 