# Python Basic Fundamentals 

This project demonstrates various fundamental Python concepts including functions, decorators, and object-oriented programming. It was created as part of a Python coding assessment to showcase understanding of basic Python principles.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Setup](#setup)
3. [Functions Overview](#functions-overview)
4. [Car Class](#car-class)
5. [Usage Examples](#usage-examples)
6. [Contributing](#contributing)

## Project Structure

The project consists of two main Python files:

- `functions.py`: Contains implementations of various utility functions.
- `car.py`: Contains the Car class implementation.

## Setup

To use this project, follow these steps:

1. Fork the repository:
   - Go to the GitHub page of this project.
   - Click the "Fork" button in the top-right corner to create your own copy of the repository.

2. Clone your forked repository:
   ```
   git clone https://github.com/your-username/python-fundamentals-assessment.git
   cd python-fundamentals-assessment
   ```

3. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. You're all set! No additional dependencies are required as the project uses only Python standard libraries.

## Functions Overview

### In `functions.py`:

1. `add_numbers(num1, num2)`: 
   - Adds two numbers and returns the sum.

2. `is_even(number)`: 
   - Checks if a number is even, returns True if even, False otherwise.

3. `reverse_string(text)`: 
   - Reverses a given string.

4. `count_vowels(text)`: 
   - Counts the number of vowels in a given string (case-insensitive).

5. `calculate_factorial(n)`: 
   - Calculates the factorial of a non-negative integer using recursion.

6. `decorator_func(func)`: 
   - A decorator function that prints "Decorator Applied" before executing the decorated function.

7. `apply_decorator(func)`: 
   - Applies the `decorator_func` to a given function.

8. `sort_by_age(people)`: 
   - Sorts a list of (name, age) tuples by age in ascending order.

9. `merge_dicts(dict1, dict2)`: 
   - Merges two dictionaries, summing values for common keys.

## Car Class

### In `car.py`:

The `Car` class represents a car with the following attributes:
- `make`: The manufacturer of the car
- `model`: The model of the car
- `year`: The year the car was manufactured

It includes a method `display_info()` that prints out the car's information.

## Usage Examples

Here are some examples of how to use the functions and the Car class:

```python
from functions import add_numbers, is_even, reverse_string, count_vowels, calculate_factorial, apply_decorator, sort_by_age, merge_dicts
from car import Car

# Using functions
print(add_numbers(5, 3))  # Output: 8
print(is_even(4))  # Output: True
print(reverse_string("hello"))  # Output: olleh
print(count_vowels("Python"))  # Output: 1
print(calculate_factorial(5))  # Output: 120

@apply_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Decorator Applied \n Hello, Alice!

people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
print(sort_by_age(people))  # Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 5, 'c': 4}

# Using Car class
my_car = Car("Toyota", "Corolla", 2022)
my_car.display_info()  # Output: 2022 Toyota Corolla
```

## Contributing

This project was created for assessment purposes, but contributions for educational purposes are welcome. To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

Please ensure your code adheres to the existing style and includes appropriate comments.

---

This project is part of a Python fundamentals assessment and demonstrates basic concepts in Python programming.