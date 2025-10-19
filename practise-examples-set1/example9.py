# input: True,False
# output: True and False:False,True or False:True,not True:False


a, b = input("Enter inputs seperated by comma: ").split(",")
checkAnd = a and b 
checkOr = a or b 
checkNot = not a 

print(f"{a} and {b}:{checkAnd},{a} or {b}:{checkOr},not {a}:{checkNot}")