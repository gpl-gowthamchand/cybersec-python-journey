# input: 10,5
# output: Addition:15,Subtraction:5,Multiplication:50,Division:2.0

a,b = map(int, input("Enter two nums seperated with comma: ").split(","))
sum = a+b 
sub = a-b 
mul = a*b 
div = a/b 

print(f"Addition:{sum},Subtraction:{sub},Multiplication:{mul},Division:{div}")