'''
✅ Problem 1: Clean Phone Numbers
Input: List of strings with messy phone numbers like " +92 300-123 4567 "
Task: Remove spaces, dashes, and convert all to format +923001234567

🔧 Concepts: map, lambda, str.replace()
'''

phone_numbers = [
    " +92 300-123 4567 ",
    "+92-301 234 5678",
    "  +92302-3456789",
    "+92 303 456-7890 ",
    " +92-3041234567",
    "+92 305-12 34 567 ",
    "   +92 306-123-4567   "
]

cleaned_numbers = list(map(lambda num: num.replace("-", "").replace(" ", ""), phone_numbers))
print(cleaned_numbers)

# method 2

cleaned_numbers = list(map(lambda num: num.strip().replace("-", "").replace(" ", ""), phone_numbers))
print(cleaned_numbers)

"""strip()"""

email = "   mateen@gmail.com  "
clean = email.strip()
print(clean == "mateen@gmail.com")  # True

######################################################

'''
✅ Problem 2: Filter Emails from Specific Domain
Input: List of emails
Task: Return emails that are from @gmail.com

🔧 Concepts: filter, lambda
'''

emails = [
    "alice@gmail.com",
    "bob@yahoo.com",
    "charlie@outlook.com",
    "dave@gmail.com ",
    " eve@gmail.com",
    "frank@protonmail.com"
]

gmail_emails = list(map(lambda e: e.strip(), filter(lambda e: e.strip().endswith("@gmail.com"), emails)))
print(gmail_emails)

######################################################

'''
✅ Problem 3: Total Price of Cart Items
Input: List of dictionaries like:

python
Copy
Edit
[{"item": "book", "price": 200}, {"item": "pen", "price": 50}]
Task: Total price

🔧 Concepts: reduce, lambda
'''

from functools import reduce

total_price reduce(lambda total_price, item: total_price + item['price'], cart, 0)
print(total_price)

# method 2

total_price = 0

for item in cart:
    total_price += item["price"]
    
print(total_price)

######################################################

'''
✅ Problem 4: Square of Even Numbers Only
Input: [1, 2, 3, 4, 5, 6]
Task: Square only the even numbers

🔧 Concepts: filter + map + lambda
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = [i**2 for i in numbers if i%2==0]
print(square)

# method 2

square = list(map(lambda x: x**2, filter(lambda x: x%2==0, numbers)))
print(square)

######################################################

'''
✅ Problem 5: Convert JSON Records to Clean Summary

data = [
    {"name": "alice", "score": 78},
    {"name": "bob", "score": 90},
    {"name": "charlie", "score": 82}
]

output:!

"ALICE scored 78"
"BOB scored 90"
"CHARLIE scored 82"
'''

data = [
    {"name": "alice", "score": 78},
    {"name": "bob", "score": 90},
    {"name": "charlie", "score": 82}
]

summary = [f"{d['name'].upper()} scored {d['score']}" for d in data]
print(summary)
