class SudokuRuleKeeper:

  def __init__(self):
    pass
  
  def main(self, strArr):
    grids = self._make_grids(strArr)

    errors = []
    for x in range(9):
      for y in range(9):
        if grids[x][y] == 'x':
          continue
        if self._is_include_horizontal(grids, grids[x][y], x):
          errors.append([x, y])
        if self._is_include_vertical(grids, grids[x][y], y):
          errors.append([x, y])
        if self._is_include_subgrid(grids, grids[x][y], x, y):
          errors.append([x, y])
  #  print(errors)

    group1 = [0, 1, 2]
    group2 = [3, 4, 5]
    group3 = [6, 7, 8]
    quadrants = []
    for x in range(len(errors)):
      error_x = errors[x][0]
      error_y = errors[x][1]
      if error_x in group1:
        if error_y in group1:
          quadrants.append('1')
        if error_y in group2:
          quadrants.append('2')
        if error_y in group3:
          quadrants.append('3')

      if error_x in group2:
        if error_y in group1:
          quadrants.append('4')
        if error_y in group2:
          quadrants.append('5')
        if error_y in group3:
          quadrants.append('6')

      if error_x in group3:
        if error_y in group1:
          quadrants.append('7')
        if error_y in group2:
          quadrants.append('8')
        if error_y in group3:
          quadrants.append('9')

    return ','.join(set(quadrants))

  def _make_grids(self, strArr):
    grids = []
    for i in strArr:
      grids.append(i.replace('(','').replace(')','').split(','))
    return grids

  def _is_include_horizontal(self, grids, check_value, current_x):
    count = 0
    for y in range(9):
      if check_value == grids[current_x][y]:
        count += 1
    if count >= 2:
      return True
    else:
      return False

  def _is_include_vertical(self, grids, check_value, current_y):
    count = 0
    for x in range(9):
      if check_value == grids[x][current_y]:
        count += 1
    if count >= 2:
      return True
    else:
      return False
