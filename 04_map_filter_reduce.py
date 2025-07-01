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

'''
reduce() – Collapse a list into a single value (needs from functools import reduce)
'''

from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
# 24
