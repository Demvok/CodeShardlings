def transpose(mat1):
  pi, pj = len(mat1), len(mat1[0])
  mat2 = [[0 for _ in range(pi)] for _ in range(pj)]
  for i in range(pi):
      for j in range(pj):
          mat2[pj-j-1][i] = mat1[i][j]
  return mat2

def printMatrix(mat):
  res = ''
  for row in mat:
    res += ''.join([str(elem).ljust(3) for elem in row])
    if n > 1:
      res += '\n'
  print(res)

n, m = 7, 7
#n, m = [int(elem) for elem in input().split()]
matrix = [[0 for _ in range(m)] for _ in range(n)]
dig = list(range(1, n*m + 1))

while len(dig) > 1:
  shift = 0  
  while matrix[shift].count(0) >= 1:
    if len(dig) == 1:
      break
    l = len(matrix[shift])-1-shift*2
    for i in range(l):
      if dig == []:
        break
      matrix[shift][i+shift] = dig.pop(0)
    matrix = transpose(matrix)
    if 0 not in matrix[shift]:
      shift += 1

if len(dig) == 1:
  for row in matrix:
    if 0 in row:
      row[row.index(0)] = dig.pop(0)
      break
    
while matrix[0][0] != 1:
  matrix = transpose(matrix)
printMatrix(matrix)