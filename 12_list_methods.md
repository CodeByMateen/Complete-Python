# 📋 Python List Methods - Full Interview Cheat Sheet (with Examples)

Python lists are **ordered**, **mutable**, and **versatile**. Here’s every list method you need to **master** for interviews 🔥

---

## 🔧 Core Built-in List Methods

| Method             | Description                                                   | Example                                |
|--------------------|---------------------------------------------------------------|----------------------------------------|
| `append(x)`        | Add element `x` at the end                                    | `lst.append(10)` → `[1, 2, 10]`         |
| `extend(iter)`     | Add all elements from another iterable                        | `lst.extend([4, 5])` → `[1, 2, 4, 5]`   |
| `insert(i, x)`     | Insert `x` at index `i`                                       | `lst.insert(1, 100)` → `[1, 100, 2]`    |
| `remove(x)`        | Remove **first** occurrence of `x`                            | `lst.remove(2)` → `[1, 3]`              |
| `pop([i])`         | Remove and return element at index `i`, last if not given     | `lst.pop()` → returns last             |
| `clear()`          | Remove all items from the list                                | `lst.clear()` → `[]`                   |
| `index(x[, start[, end]])` | Return index of `x` (error if not found)             | `lst.index(3)` → `2`                   |
| `count(x)`         | Count how many times `x` appears                              | `lst.count(2)` → `3`                   |
| `sort(reverse=False, key=None)` | Sort list (in-place)                           | `lst.sort()` or `lst.sort(reverse=True)` |
| `reverse()`        | Reverse list **in-place**                                     | `lst.reverse()`                        |
| `copy()`           | Return shallow copy of list                                   | `new = lst.copy()`                     |

---

## 🔬 Non-methods (But Useful List Operations)

| Operation          | Description                                  | Example                       |
|--------------------|----------------------------------------------|-------------------------------|
| `len(lst)`         | Number of items                              | `len([1, 2, 3])` → `3`        |
| `sum(lst)`         | Sum of all numbers                           | `sum([1, 2, 3])` → `6`        |
| `sorted(lst)`      | Return new **sorted** list                   | `sorted([3, 1, 2])` → `[1,2,3]` |
| `reversed(lst)`    | Return reversed iterator                     | `list(reversed(lst))`         |
| `min(lst)` / `max(lst)` | Min/Max element                        | `min([1,5,3])` → `1`          |
| `any(lst)`         | `True` if **any** element is truthy          | `any([0, "", 3])` → `True`    |
| `all(lst)`         | `True` if **all** elements are truthy        | `all([1, 2, 3])` → `True`     |

---

## 🧪 Quick Practical Examples

```python
lst = [1, 2, 3]

lst.append(4)           # [1, 2, 3, 4]
lst.extend([5, 6])      # [1, 2, 3, 4, 5, 6]
lst.insert(2, 100)      # [1, 2, 100, 3, 4, 5, 6]
lst.remove(100)         # [1, 2, 3, 4, 5, 6]
lst.pop()               # returns 6 → [1, 2, 3, 4, 5]
lst.count(2)            # 1
lst.index(4)            # 3
lst.sort()              # [1, 2, 3, 4, 5]
lst.reverse()           # [5, 4, 3, 2, 1]
new_list = lst.copy()   # copy of list
