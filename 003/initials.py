def get_initials(fullname):
  lst = (fullname)
  name_list = lst.split()
  print(name_list)

  first = name_list[0][0]
  second = name_list[1][0]

  return(first.upper() + second.upper())
answer = get_initials(input('Enter a name: '))
print(f'Your initials are {answer}')


def last_3_digits():
  num = input('Enter your student number: ')
  solution = num[-3:]
  print(f'The last 3 digits of your student number are {solution}')


last_3_digits()
