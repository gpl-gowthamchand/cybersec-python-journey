# Convert a tuple to a list and modify it, then convert it back. 

original_tuple = ("Dodge", "Ford", "Porsche", "Maserati", "Ferrari")
print(f"Original tuple: {original_tuple}")

to_list = list(original_tuple)
print(f"Converted to list: {to_list}")

to_list.pop()

updated_tuple = tuple(to_list)
print(f"updated tuple : {updated_tuple}")