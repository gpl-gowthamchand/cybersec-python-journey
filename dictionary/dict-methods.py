## Dictionary methods 

dict1 = {
    1 : "One",
    2 : "Two",
    3 : "Three"
}

## get(key, default) - returns the value for the key, if key not exists then returns default
print(dict1.get(1))              # One
print(dict1.get(4,"Not found"))  # Not found


## keys() - returns keys, we can also use this in loops
print(dict1.keys())            # dict_keys([1, 2, 3])

## values() - returns values, we can also use this in loops
print(dict1.values())          # dict_values(['One', 'Two', 'Three'])

## items() - returns key-value pairs as tuples, we can also use this in loops
print(dict1.items())           # dict_items([(1, 'One'), (2, 'Two'), (3, 'Three')])

## update(dict2) - adds or updates dictionary items from another dictionary
dict2 = {
    4 : "Four",
    5 : "Five"
}

dict1.update(dict2)
print(dict1)             # {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five'}

## pop(key, default) - removes a key and returns it value, if key dont exist then returns default value.
print(dict1.pop(4, "Operation not done"))  # Four - (key 4 got removed and returned the value inside it)
print(dict1)                               # {1: 'One', 2: 'Two', 3: 'Three', 5: 'Five'} -- see no key 4 here now.

## popitem() - removes the last element
print(dict1.popitem())        # (5, 'Five') - this last one will be removed
print(dict1)                  # {1: 'One', 2: 'Two', 3: 'Three'} - see now it was removed

## clear() - removes all items from the dictionary 
print(dict2)                # {4: 'Four', 5: 'Five'}
dict2.clear()
print(dict2)                # {} - empty dict2

## copy - creates a shallow copy of the dictionary 
dict3 = {}
print(dict3)                # {} - now it is empty
dict3 = dict1.copy()
print(dict3)                # {1: 'One', 2: 'Two', 3: 'Three'} - we copied dict1 items into dict3

## setdefault(key, default) - returns the value of the key, if the key dont exist then it is added with given default value.
print(dict3.setdefault(3,"DEFAULT"))  # Three - returned the key value
print(dict3.setdefault(7,"DEFAULT"))  # DEFAULT - key 7 not present so, key 7 is added and then its value is set to "DEFAULT"
print(dict3)                          # {1: 'One', 2: 'Two', 3: 'Three', 7: 'DEFAULT'}

# fromkeys(iterable, value) - creates a new dictiionary from the given keys with the same value.
my_keys = [ "id", "status", "role"]
new_dictionary = dict.fromkeys(my_keys, "Unknownn")
print(new_dictionary)                        # {'id': 'Unknownn', 'status': 'Unknownn', 'role': 'Unknownn'}

# len() - returns the no of key value pairs 
print(len(new_dictionary))            # 3

# in and not in (membership operators) - used to check if a key exists in the dictionary 
print(3 in dict1)      # True
print(8 in dict1)      # False
print(8 not in dict1)  # True 