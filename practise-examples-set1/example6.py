# input: 5
# output: "Countdown:5 4 3 2 1 Blast Off!"

num = int(input("Enter a num: "))


li = []
for i in range(num, 0, -1):
    li.append(i)



print("Countdown:", *li, " ", end="Blast Off!")
