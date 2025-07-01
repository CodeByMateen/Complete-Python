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

