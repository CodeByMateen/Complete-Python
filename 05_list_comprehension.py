'''
list comprehension – Cleaner, faster way to create lists
'''

nums = [1, 2, 3]
squares = [x * x for x in nums]
# [1, 4, 9]


# practice problem

people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 18},
    {"name": "Dave", "age": 16},
    {"name": "Eve", "age": 22}
]

expected_result = ['BOB', 'CHARLIE', 'EVE']

'''method1'''
result = sorted(p['name'].upper() for p in people if p['age'] >= 18)
'''method2'''
result = sorted(list(map(lambda p: p['name'].upper(), filter(lambda p: p['age'] >= 18, people))))
print(result)
