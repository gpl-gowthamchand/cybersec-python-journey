'''
Find the Largest of Three Numbers
Write a function largest(a, b, c) that returns the largest number among three.
'''

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

result = largest(9, 5, 6)
print(result)


''' Shortest using max()


def largest(a, b, c):
    return max(a, b, c)

print(largest(9, 5, 6))

'''