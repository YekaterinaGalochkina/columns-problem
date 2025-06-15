def top_column(matrix):
  
  list = []

  for tuple in matrix:
    for i in range(len(tuple)):
      if len(list) < len(tuple):
        list.append(tuple[i])
      else: 
        list[i] += tuple[i]
  
  max = list[0]

  for el in list:
    if el > max:
      max = el

  return list.index(max)

# Time comp: O(r * c)
# Space comp: O(c)
# r = number of rows
# c = number of columns  


# Test cases
matrix_1 = ((5, 6, 7, 8),
            (3, 9, 2, 5),
            (2, 1, 9, 2))
assert top_column(matrix_1) == 2

matrix_2 = ((1, 2),
            (3, 4))
assert top_column(matrix_2) == 1

matrix_3 = ((3,),
            (4,),
            (9,))
assert top_column(matrix_3) == 0

matrix_4 = ((-2, -1, -3),)
assert top_column(matrix_4) == 1

print("All tests passed!")
print("Finished early? Discuss time & space complexity")