# Sum of all elements in a list without using sum().
#(Use a loop.)


num = [1,2,3,4,5,6,7,8,9]
sum_of_nums = 0 

for i in num:
    sum_of_nums = sum_of_nums + i

print(f"Sum: {sum_of_nums}")