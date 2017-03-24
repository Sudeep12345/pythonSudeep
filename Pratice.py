names =['John Doe ','Jane Doe','Johnny Truk']

names[0] = 'Foo Bar'
print('Names now:', names)

names.append('Molly Mormon')
names.append('Joe Boggs')
print('Names finally:',names)
print('Last name in the list: %s' % names[-1])

joined_name = '\n' .join(names)
print('\nList of names:')
print(joined_name)s