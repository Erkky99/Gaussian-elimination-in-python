a = []
a.append(2)
a.append(3)
a.append(4)

print(a)

aNew = [i * 2 for i in a]

print(aNew)

row1 = [1, 1, 1, 4]
row2 = [2, -1, 3, 16]
row3 = [8, -9, -1, 4]

matrix = [row1, row2, row3]

matrix[0], matrix[1] = matrix[1], matrix[0]

print(matrix)

print("Yadda yadda d({}, {})".format(1, 2))

t = j = k = 0

print(t)
print(j)
print(k)

#b = []
#for x in range(0, 3):
#    d = int(input("Värde: "))
#    b.append(d)

#print(b)