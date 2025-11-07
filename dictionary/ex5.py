'''
Remove a Key

From:
employee = {"name": "Raj", "role": "Dev", "salary": 50000}

Remove "salary" using pop()
Print the updated dictionary.
'''

employee = {"name": "Raj", "role": "Dev", "salary": 50000}
employee.pop("salary", None)
print(employee)