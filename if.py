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
