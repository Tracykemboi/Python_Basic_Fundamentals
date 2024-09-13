def add_numbers(num1, num2):
    # Simple addition function
    return num1 + num2

def is_even(number):
    # Check if a number is even using modulo operator
    if number % 2 == 0:
        return True
    else:
        return False

def reverse_string(text):
    # Reverse a string using slice notation
    return text[::-1]

def count_vowels(text):
    vowels = 'aeiou'
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

def calculate_factorial(n):
    # Recursive factorial calculation
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Decorator function
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

def apply_decorator(func):
    # Apply the decorator_func to the given function
    return decorator_func(func)

def sort_by_age(people):
    # Sort list of (name, age) tuples by age
    return sorted(people, key=lambda x: x[1])

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged