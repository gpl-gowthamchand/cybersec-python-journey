''' 
Unique Languages
Given:
    langs1 = {"Python", "C", "C++"}
    langs2 = {"Java", "C++", "Go"}
Find:
Languages common to both
Languages only in langs1
All languages offered
'''

langs1 = {"Python", "C", "C++"}
langs2 = {"Java", "C++", "Go"}

print(f"Common languages in both sets: {langs1.intersection(langs2)}")
print(f"Languages only in set 1: {langs1.difference(langs2)}")
print(f"All languages offered :{langs1.union(langs2)}")