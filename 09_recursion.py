# 🧩 Problem 1: Sum of Digits using Recursion

def numSum(num):
    if num == 0:
        return 0
    return numSum(num // 10) + num % 10

# 🔁 Dry Run: numSum(1234)
# → numSum(123) + 4
# → numSum(12) + 3 + 4
# → numSum(1) + 2 + 3 + 4
# → numSum(0) + 1 + 2 + 3 + 4
# → 0 + 1 + 2 + 3 + 4 = 10

print(numSum(1234))  # Output: 10

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 🧩 Problem 2: Count Zeroes in a Number using Recursion

def countZero(num, count=0):
    if num == 0:
        return 1 if count == 0 else count
    if num % 10 == 0:
        count += 1
    return countZero(num // 10, count)

# 🔁 Dry Run: countZero(1020304)
# → 4 (not 0) → count = 0
# → 0 (is 0)  → count = 1
# → 3         → count = 1
# → 0         → count = 2
# → 2         → count = 2
# → 0         → count = 3
# → 1         → count = 3
# → 0 → base case → return 3

print(countZero(1020304))  # Output: 3
print(countZero(0))        # Output: 1

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 🧩 Problem 3: Reverse a String using Recursion

def reverseString(word):
    if len(word) <= 1:
        return word
    return reverseString(word[1:]) + word[0]

# 🔁 Dry Run: reverse("abc")
# → reverse("bc") + "a"
# → (reverse("c") + "b") + "a"
# → ("c" + "b") + "a"
# → "cb" + "a"
# → "cba"

print(reverseString("mateen"))  # Output: "neetam"
print(reverseString("abc"))     # Output: "cba"

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 🧩 Problem 4: Check if Array is Sorted using Recursion

def isSorted(arr):
    if len(arr) <= 1:
        return True
    if arr[0] > arr[1]:
        return False
    return isSorted(arr[1:])

# 🔁 Dry Run: isSorted([1, 3, 4, 5])
# → 1 < 3 → check [3, 4, 5]
# → 3 < 4 → check [4, 5]
# → 4 < 5 → check [5]
# → base case → return True

print(isSorted([1, 3, 4, 5]))     # True
print(isSorted([3, 2]))           # False
print(isSorted([9]))             # True
print(isSorted([]))              # True

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 🧩 Problem 5: Product of Array Elements using Recursion

def product(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * product(arr[1:])

# 🔁 Dry Run: product([2, 3, 4])
# → 2 * product([3, 4])
# → 2 * (3 * product([4]))
# → 2 * (3 * (4 * product([])))
# → 2 * 3 * 4 * 1 = 24

print(product([2, 3, 4]))     # Output: 24
print(product([]))            # Output: 1
