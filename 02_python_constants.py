class Constants:
    _instance = None
    PI = 3.14159
    MAX_USERS = 100
    APP_NAME = "MyApp"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __setattr__(self, key, value):
        raise TypeError(f"Cannot modify constant '{key}'")

    def __delattr__(self, key):
        raise TypeError(f"Cannot delete constant '{key}'")

const = Constants()

print(const.PI)         # ✅ 3.14159
print(const.APP_NAME)   # ✅ MyApp

# const.PI = 3          # ❌ TypeError: Cannot modify constant 'PI'
# del const.PI          # ❌ TypeError: Cannot delete constant 'PI'
