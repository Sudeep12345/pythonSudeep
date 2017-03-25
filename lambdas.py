my_list = [1, 2, 3, 4, 5]

squares = list(map(lambda x:x**2,my_list) )
squares_2 = [x**2 for x in my_list]

print(squares)
print(squares_2)