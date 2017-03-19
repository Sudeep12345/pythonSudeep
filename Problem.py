print('enter the marks of five subject:')

maths=input('maths:')
physcis=input('physic:')
chemestry=input('chemestry:')
Nepali=input('Nepali:')
English=input('English:')

Total=float(maths) + float(physcis) + float(chemestry) + float(Nepali) + float(English)
percentage=Total/500 * 100
print('total marks= {}'.format(Total))
print('total percentage={}'.format(percentage))