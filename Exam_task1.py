A = []
variants = [1] * 10
for i in range(9):
    A.append(input())
x, y = int(input()), int(input())
for i in range(9):
    if variants[int(A[i][y])] == 1:
        variants[int(A[i][y])] = 0
for i in range(9):
    if variants[int(A[x][i])] == 1:
        variants[int(A[x][i])] = 0

if x % 3 == 0:
    x1, x2 = x + 1, x + 2
elif x % 3 == 1:
    x1, x2 = x - 1, x + 1
else:
    x1, x2 = x - 1, x - 2
if y % 3 == 0:
    y1, y2 = y + 1, y + 2
elif y % 3 == 1:
    y1, y2 = y - 1, y + 1
else:
    y1, y2 = y - 1, y - 2

y0 = [y1, y2, y]
x0 = [x, x1, x2]
x0.sort()
y0.sort()
for i in range(x0[0], x0[2]+1):
    for j in range(y0[0], y0[2]+1):
        if variants[int(A[i][j])] == 1:
            variants[int(A[i][j])] = 0

for i in range(1, 10):
    if variants[i] == 1:
        print(i)
