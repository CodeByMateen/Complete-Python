🧊 frozenset kya hota hai?

🔓 set → mutable hota hai (update ho sakta hai)

🔒 frozenset → immutable hota hai (update nahi ho sakta)

✅ Example:

normal_set = {"a", "b", "c"}
frozen = frozenset(["a", "b", "c"])

normal_set.add("d")      # ✅ Allowed
frozen.add("d")          # ❌ Error: 'frozenset' object has no attribute 'add'
