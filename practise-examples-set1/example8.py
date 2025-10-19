# input: 10,5
# output: 10>5:True,10<5:False,10==5:False,10!=5:True

a,b = map(int, input("Enter two nums seperated by comma: ").split(","))

equalto = a==b 
greaterthan = a>b 
lesstham = a<b 
notequalto = a!=b 
greaterOrEqualto = a>=b 
lessOrEqualto = a<=b 

print(f"{a}>{b}:{greaterthan},{a}<{b}:{lesstham},{a}=={b}:{equalto},{a}!={b}:{notequalto}")