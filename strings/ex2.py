## string methods 

s = " heLlo python!   "
print(s)

#modify 
x= s.strip() #removes space on both sides, lstrip and rstrip to remove space left and right side
print(x)

#case 
a = x.upper()
print(a)

print(x.lower())
print(x.title())
print(x.capitalize())
print(x.swapcase())

#search
print(x.count("o"))
print(x.find("p"))

#split and join 
print(x.split())
print("#".join(['one', 'two', 'three']))