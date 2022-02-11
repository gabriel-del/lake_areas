matrix = [
    [1, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

class Solution:
  def lake_areas(self, matrix):
    self.X = len(matrix)
    self.Y = len(matrix[0])
    sizes = []
    for x in range(self.X):
      for y in range(self.Y):
        # print(f'[{x}][{y}]={matrix[x][y]}')
        if matrix[x][y] == 1:
          self.total = 0
          self.neighbors(matrix, x, y)
          sizes += [self.total]
    sizes.sort()
    return sizes
  def neighbors(self, matrix, x, y):
    self.total += 1
    matrix[x][y] = 0
    if x > 0 and matrix[x - 1][y] == 1:
      self.neighbors(matrix, x - 1, y)
    if y > 0 and matrix[x][y - 1] == 1:
      self.neighbors(matrix, x, y - 1)
    if x + 1 < self.X and matrix[x + 1][y] == 1:
      self.neighbors(matrix, x + 1, y)
    if y + 1 < self.Y and matrix[x][y + 1] == 1:
      self.neighbors(matrix, x, y + 1)
print(Solution().lake_areas(matrix))

