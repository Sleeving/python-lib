weight = int(input('Enter your weight: '))
unit = input('(L)bs or (K)g: ')
if unit.isupper() == 'L':
    print(weight)
elif unit.isupper() == 'K':
    print(weight * 0.45)



