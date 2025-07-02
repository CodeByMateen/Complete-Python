'''
Jab tu list ya iterable ke elements pe loop kar raha ho, aur saath saath unka index bhi chahiye ho, toh enumerate() best hai.
'''

fruits = ["apple", "banana", "mango"]

# ❌ Without enumerate() (manual index):
for i in range(len(fruits)):
    print(i, fruits[i])

# ✅ With enumerate() (clean & pythonic):
for i, fruit in enumerate(fruits):
    print(i, fruit)

'''output
0 apple  
1 banana  
2 mango
'''

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

'''output
1 apple  
2 banana  
3 mango
'''

#################################
'''
Practice Problem
'''

nums = [3, 1, 2, 3, 4, 5, 6]

for i, num in enumerate(nums):
    if i == num:
        print(f"{num} at index {i}")
