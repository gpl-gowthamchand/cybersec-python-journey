'''
Find Common Elements Between Two Lists
Write a function common_elements(list1, list2) that returns common items using set intersection.
'''

def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

list1 = [1,3,4,5,6]
list2 = [3,5,6,7,8]

print(common_elements(list1, list2))