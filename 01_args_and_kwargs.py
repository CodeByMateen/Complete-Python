 '''
*args (Arguments):
- Think of *args like a backpack that can hold any number of items
- It lets you pass any number of values to a function
- The values are stored as a tuple
- The name 'args' is just a convention - you could use *numbers or *items too
'''

# Simple *args example - Adding any number of numbers
def add_numbers(*numbers):
    print(f"I received these numbers: {numbers}")  # Shows it's a tuple
    return sum(numbers)

# print(add_numbers(1, 2))          # You can pass 2 numbers
# print(add_numbers(1, 2, 3, 4))    # Or 4 numbers
# print(add_numbers(10))            # Or just 1 number!

'''
**kwargs (Keyword Arguments):
- Think of **kwargs like a labeled box where each item has a name
- It lets you pass any number of key=value pairs to a function
- The values are stored as a dictionary
- The name 'kwargs' is just a convention - you could use **data or **info too
'''

# Simple **kwargs example - Describing a person
def describe_person(**details):
    print(f"I received these details: {details}")  # Shows it's a dictionary
    for key, value in details.items():
        print(f"Their {key} is {value}")

# describe_person(name="Bob", age=25)                    # You can pass 2 details
# describe_person(name="Alice", age=30, hobby="coding")  # Or 3 details!

'''
practice problems
'''
# Q1: avarage of numbers using args

def avarage(*args):
    return sum(args) / len(args)

print(avarage(1, 2, 3, 4, 5))

# Q2: concatenate strings using *args

def concatenate_strings(*args):
    return " ".join(args)

print(concatenate_strings("Hello", "World", "Python", "is", "awesome"))

# Q3: find the maximum of numbers using *args

def find_max(*args):
    return max(args)

print(find_max(10, 5, 23, 17, 44))

# Q4: Using both *args and **kwargs
def student_info(*args, **kwargs):
    print("Args (Subjects):", args)
    print("Kwargs (Student Details):", kwargs)
    
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=" ")

student_info("Math", "Physics", "Chemistry", 
             name="John", age=20, grade="A")

# Q5: Shopping cart with **kwargs
def calculate_total(**kwargs):
    total = 0
    for item, price in kwargs.items():
        print(f"{item}: ${price}")
        total += price
    return f"Total: ${total}"

print(calculate_total(shirt=25, pants=35, shoes=45))

# Q6: Function with regular params, *args and **kwargs
def mixed_function(required_param, *args, **kwargs):
    print("Required:", required_param)
    print("Args:", args)
    print("Kwargs:", kwargs)

mixed_function("Hello", 1, 2, 3, name="Alice", age=25)
