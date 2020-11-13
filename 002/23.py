customer = {
    'name': 'John Smith',
    'age': 30,
   # 'age': 40,
    'is_verified': True
}
customer['name'] = 'Jack Smith'
print(customer['name'])
print(customer.get('age'))
print(customer.get('birthdate', 'January 1st'))
