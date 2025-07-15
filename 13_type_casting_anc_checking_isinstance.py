1. Type Casting – (Convert one type to another)

✅ Common Type Castings:

int("5")        # '5' (string) → 5 (int)
str(10)         # 10 (int) → '10' (string)
float("3.14")   # '3.14' → 3.14
list("abc")     # ['a', 'b', 'c']
tuple([1, 2])   # (1, 2)
set([1, 2, 2])  # {1, 2}
bool(0)         # False
bool("Mateen")  # True


2. Type Checking – Check karna ke variable ka type kya hai

(A) type() – Directly gives type

x = 10
print(type(x))         # <class 'int'>
print(type("hello"))   # <class 'str'>


(B) isinstance() – Checks if variable is of a specific type

x = [1, 2, 3]

print(isinstance(x, list))    # ✅ True
print(isinstance(x, str))     # ❌ False

# Multiple types check
print(isinstance(3.14, (int, float)))  # ✅ True

#######################################################

🔍 Difference Between type() and isinstance() in One Line:
Concept	Purpose
type(obj)	Batata hai ke yeh object ka type kya hai
isinstance(obj, type)	Check karta hai ke object iss type ka hai ya nahi


❌ vs ✅ (type vs isinstance)
Task	type()	isinstance()
Exact type match	✅ Yes	✅ Yes
Supports parent-child inheritance	❌ No	✅ Yes (preferred)
Safer for multiple types	❌ No	✅ Yes (tuple support)


-----------------------------

class Animal:
    pass

class Dog(Animal):
    pass


- Dog is a child class of Animal
- Animal is the parent (base) class

     
❌ type() Inheritance nahi samajhta

d = Dog()

print(type(d) == Dog)     # ✅ True
print(type(d) == Animal)  # ❌ False  ← Even though Dog inherits Animal

Matlab: type() exact match check karta hai. Agar tum Dog ho, toh Animal nahi ho sakte type() ke liye.


✅ isinstance() Inheritance samajhta hai

print(isinstance(d, Dog))      # ✅ True
print(isinstance(d, Animal))   # ✅ True ✅ ✅ ✅

Toh isinstance() bolta hai:
“Agar tu Dog hai, aur Dog Animal ka child hai,
toh tu Animal bhi hai. 🧬”
