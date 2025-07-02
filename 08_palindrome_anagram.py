# Concept 1: Palindrome
# A word, number, or sentence that reads the same forward and backward

# ✅ Examples:
# "madam" -> same forward and backward
# "racecar" -> same
# 121 -> numeric palindrome
# "nurses run" -> (ignoring spaces)

# ❌ Not a palindrome:
# "python" -> reversed is "nohtyp", not same

# Palindrome Checker (Python)
word = "madam"
print(word == word[::-1])  # True


# Concept 2: Anagram
# Two words/phrases that use the same characters, just rearranged.

# ✅ Examples:
# "listen" and "silent"
# "triangle" and "integral"
# "evil" and "vile"

# ❌ Not an anagram:
# "hello" and "world" (different letters)

# Anagram Checker (Python)
str1 = "listen"
str2 = "silent"
print(sorted(str1) == sorted(str2))  # True


# Comparison Table (Text)
# Feature              | Palindrome            | Anagram
# ---------------------|------------------------|------------------------------
# Meaning              | Same when reversed     | Same letters, different order
# Comparison           | Word vs. itself        | Word vs. another word
# Examples             | madam, 121             | listen & silent
# Case Sensitive?      | Often ignored          | Often ignored
# Use in logic         | String reversal        | Sorting / counting chars
