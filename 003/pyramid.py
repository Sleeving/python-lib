num = int(input("enter the number of rows: "))
for i in range(num): 
  print(" " * (num - 1 - i) + "* " *(i + 1))
