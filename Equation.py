Equation = input("Y=mx+c")

# 'y' , 'mx +c'
rhs = Equation.split('=') [1]
parts = rhs.split('+')

m=parts[0].replace('x','').strip()
c=parts[1].strip()

print('slope of line: {}'.format(m))
print('Y-Intercept: {}'.format(c))