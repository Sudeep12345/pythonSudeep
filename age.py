age = int(input('age:'))

if age <= 0:
	print('invaild input for age')
elif age <= 1:
	print('you are an infant')
elif age <= 12:
	print('you are just kid')
elif age <=20:
	print('you are a teenage')
elif age <= 45:
	print('you are a young')
elif age <= 59:
	print('you are middle age')
elif age < 120: 
	print('you are an old age')
else :
	print('you are too old')
