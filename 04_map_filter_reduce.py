'''
map() – Apply a function to each item in a list
'''

nums = [1, 2, 3]
squares = list(map(lambda x: x * x, nums))
# [1, 4, 9]

'''
filter() – Filter items based on a condition
'''

nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
# [2, 4]

# problem
def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n%i==0:
            return False
    return True
      
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
print(list(filter(isPrime, nums)))

print(int((nums[9]**0.5)+1))

'''
reduce() – Collapse a list into a single value (needs from functools import reduce)
'''

from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
# 24
