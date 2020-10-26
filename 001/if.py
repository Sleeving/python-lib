temperature = 12

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: # (20, 30]
    print("its a nice day")
elif temperature > 10:
    print("its a bit cold") # 10, 20
else:
    print('its cold')
print("Done")

num1 = 100_000_000
num2 = 1_000_000
total = num1 + num2
print(total)
