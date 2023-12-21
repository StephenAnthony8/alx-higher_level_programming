def append_list(matrix=[]):
    return (list(map(lambda x: (list(map(lambda y: y ** 2, x))), matrix)))
# x is the iterator
# list converts the result back into a list
# map, is the iterator
# lambda1 function that contains the second section

#----section 2 ----#
#same thing as above but lambda 2 (inside works on x (matrix[i]))

print(append_list([[1, 2, 3], [2, 3, 4]]))