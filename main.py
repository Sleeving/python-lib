weight = float(input("Weight: "))
unit = input('(K)g or (L)bs: ')
if unit.isupper == 'K':
    converted = weight / 0.45
    print("Weight in lbs: " + str(converted))
else:
    converted = weight * 0.45
    print ('weight in Kgs: ' + str(converted))
