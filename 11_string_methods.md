# 🐍 Python String Methods - Interview Cheat Sheet

## 🔤 Case Methods

| Method         | Description                             | Example                                | Output            |
|----------------|-----------------------------------------|----------------------------------------|--------------------|
| `upper()`      | All uppercase                           | `"abc".upper()`                        | `'ABC'`            |
| `lower()`      | All lowercase                           | `"ABC".lower()`                        | `'abc'`            |
| `capitalize()` | First letter uppercase                  | `"python is cool".capitalize()`        | `'Python is cool'` |
| `title()`      | First letter of each word               | `"hello world".title()`                | `'Hello World'`    |
| `swapcase()`   | Swap uppercase and lowercase            | `"PyThOn".swapcase()`                  | `'pYtHoN'`         |
| `casefold()`   | Aggressive lowercase (for comparison)   | `"Straße".casefold()`                  | `'strasse'`        |

---

## 🔍 Search Methods

| Method         | Description                             | Example                          | Output     |
|----------------|-----------------------------------------|----------------------------------|------------|
| `find(sub)`    | First index of substring (or -1)        | `"hello".find("e")`              | `1`        |
| `rfind(sub)`   | Last index of substring                 | `"hello".rfind("l")`             | `3`        |
| `index(sub)`   | Like `find()` but raises error          | `"hello".index("l")`             | `2`        |
| `count(sub)`   | Count occurrences of substring          | `"banana".count("a")`            | `3`        |
| `startswith()` | Check if string starts with substring   | `"hello".startswith("he")`       | `True`     |
| `endswith()`   | Check if string ends with substring     | `"test.py".endswith(".py")`      | `True`     |

---

## 🧹 Whitespace Strip Methods

| Method         | Description                             | Example                           | Output     |
|----------------|-----------------------------------------|-----------------------------------|------------|
| `strip()`      | Remove leading and trailing spaces      | `" hello ".strip()`               | `'hello'`  |
| `lstrip()`     | Remove left spaces                      | `" hello".lstrip()`               | `'hello'`  |
| `rstrip()`     | Remove right spaces                     | `"hello ".rstrip()`               | `'hello'`  |

---

## 🔗 Join / Split / Replace

| Method         | Description                             | Example                           | Output           |
|----------------|-----------------------------------------|-----------------------------------|-------------------|
| `split()`      | Convert string to list by delimiter     | `"a,b,c".split(",")`              | `['a', 'b', 'c']` |
| `rsplit()`     | Split from right                        | `"a,b,c".rsplit(",", 1)`          | `['a,b', 'c']`    |
| `splitlines()` | Split by newline                        | `"a\nb".splitlines()`             | `['a', 'b']`      |
| `join()`       | Join list into string                   | `" ".join(['hello', 'world'])`    | `'hello world'`   |
| `replace()`    | Replace substrings                      | `"hi mateen".replace("hi","yo")`  | `'yo mateen'`     |

---

## 📊 Testing Methods (Return Boolean)

| Method         | Description                             | Example                  | Output   |
|----------------|-----------------------------------------|--------------------------|----------|
| `isalpha()`    | All alphabet characters                 | `"abc".isalpha()`        | `True`   |
| `isdigit()`    | All digits                              | `"123".isdigit()`        | `True`   |
| `isalnum()`    | Only alphanumeric characters            | `"abc123".isalnum()`     | `True`   |
| `isspace()`    | All whitespace                          | `"   ".isspace()`        | `True`   |
| `islower()`    | All lowercase letters                   | `"abc".islower()`        | `True`   |
| `isupper()`    | All uppercase letters                   | `"ABC".isupper()`        | `True`   |
| `istitle()`    | Title case check                        | `"Hello World".istitle()`| `True`   |

---

## 🧰 Formatting Methods

| Method         | Description                             | Example                          | Output          |
|----------------|-----------------------------------------|----------------------------------|------------------|
| `center()`     | Center align string                     | `"hi".center(10)`                | `'   hi    '`     |
| `ljust()`      | Left-align with padding                 | `"hi".ljust(5, "*")`             | `'hi***'`         |
| `rjust()`      | Right-align with padding                | `"hi".rjust(5, "*")`             | `'***hi'`         |
| `zfill()`      | Pad with zeros                          | `"42".zfill(5)`                  | `'00042'`         |
| `format()`     | Format strings                          | `"Hello, {}".format("Mateen")`   | `'Hello, Mateen'` |
| `f""` (f-strings) | Embed variables directly              | `f"Hi {name}"`                   | `'Hi Mateen'`     |

---

## 📄 Escape Characters

| Escape Code | Meaning            |
|-------------|--------------------|
| `\n`        | Newline             |
| `\t`        | Tab                 |
| `\\`        | Backslash           |
| `\'`        | Single quote        |
| `\"`        | Double quote        |

---

## ✅ Must-Know Interview Combo

These are **absolutely essential** for interviews and coding rounds:

- `strip()`, `split()`, `join()`, `replace()`
- `find()`, `count()`, `startswith()`, `endswith()`
- `upper()`, `lower()`, `title()`, `capitalize()`, `swapcase()`
- `isalpha()`, `isdigit()`, `isalnum()`, `isspace()`
- `format()`, `f-strings`, `zfill()`, `center()`, `rjust()`
- Reverse a string: `s[::-1]`
- Palindrome check: `s == s[::-1]`
- Anagram check: `sorted(s1) == sorted(s2)`

---

### ✍️ Pro Tip Practice Questions:

- Reverse words in a sentence using `split()` and `join()`
- Detect palindromes (ignoring case and spaces)
- Remove duplicates or extra spaces
- Count frequency of each character in a string
- Validate strong password using `isalpha()` / `isdigit()` etc.

---

