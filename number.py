squares = [x**2 for x in range(10)]
print('squares:',squares)

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = [x for x in number if x %2 ==0]
odd_number = [x for x in number if x % 2 !=0]
print('number:', number)
print('even number:',even_number)
print('odd number:', odd_number)