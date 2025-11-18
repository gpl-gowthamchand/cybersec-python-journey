'''
Prime Number Checker
Write a function is_prime(num) that returns True if a number is prime.'''


def is_prime(num):
    num = abs(num)
    fact = 0 
    if num == 1 or num == 0:
        return False
    else:
        for i in range(1,num+1):
            if num % i == 0:
                fact += 1
    
        if fact == 2 :
            return True
        else:
            return False


print(is_prime(-3))