# LAB - Class 42

## Project: Pythonisms

- Author: Ekow Yawson

### Overview

> Python has many elegant features that can show the difference between a “programmer who uses Python” and a true “Pythonista”
> Pythonista may be a silly word but it’s a real thing.
> A true pythonista is able to leverage the particular features of Python to accomplish a task in a simpler and more easy to reason about way.

To show off my Pythonistic skills, I have carefully crafted examples of some of the rich features of the Python language. This code base explores the following features:

#### Tasks and Requirements

1. Use `iterators/generators` on a custom collection to accomplish the following:
    - add an ability to be used in a `for` in loop
    - add an ability to be used in a **list comprehension**
    - add an ability to convert to a **list** or other collection type

2. Create a **decorator** that adds behavior to a given function. For example:
    - Calculate the time spent in the function
    - Log relevant info for debugging purposes
    - Slow down the function
    - Convert the return value in some way
    - Validate some condition on the way in

3. Use `dunder` methods to make your code more readable and elegant. For example:
    - add ability for two custom data structure to be considered equal
    - add ability for custom data structure to be considered truthy/falsy

4. Create a function that implements high level features of Python.

#### User Acceptance Tests

- Unit tests to demonstrate all the features selected.

---

### Task 1: Use iterators/generators on a custom collection

Created a custom collection class called **`PythonicCollection`** that can be iterated over using a generator.
This class stores elements and allows iteration in several Pythonic ways.

- It can be iterated over in a `for` loop.
- It supports list comprehensions, as shown by the squared numbers example.
- It can be easily converted to a list or other collection types.

### Task 2: Create a decorator

Defined a simple timing decorator to measure execution time, a useful example of decorators in practice.

- A `timer_decorator` that wraps (decorates) any function to measure and print its execution time.
- `timer_decorator` can be applied to `sample_function`, which introduces a delay of **2** seconds.

### Task 3: Use dunder methods

For **Task 3**, I demonstrated the use of dunder methods (`__eq__` and `__bool__`) in a `CustomDataStructure` class:

- **Equality Comparison**: Two instances of `CustomDataStructure` are considered equal if their data attributes are equal.
- **Truthiness Evaluation**: An instance of `CustomDataStructure` evaluates to `True` if it contains data, and `False` otherwise.

### Task 4: Implement a function that demonstrates high-level Python features

For **Task 4**, we've implemented a function named `transform_and_sum` that demonstrates high-level features of Python. This function:

- Filters even numbers from a given list.
- Squares the filtered numbers.
- Sums up the squares of these numbers.

### Unit Tests

Unit tests are provided to demonstrate and validate the functionality of each feature implemented. The tests are written using Python's `pytest` module.

```python
import pytest
from time import sleep
from functools import reduce
from pythonista.pythonistic import PythonicCollection, timer_decorator, CustomDataStructure, transform_and_sum

# Test for PythonicCollection
def test_pythonic_collection():
    pc = PythonicCollection([1, 2, 3])
    assert list(pc) == [1, 2, 3], "Conversion to list failed"
    assert [x**2 for x in pc] == [1, 4, 9], "List comprehension failed"

# Test for timer_decorator
def test_timer_decorator(capsys):
    @timer_decorator
    def dummy_sleep_function():
        sleep(0.1)
    dummy_sleep_function()
    captured = capsys.readouterr()
    assert "executed in" in captured.out, "Decorator output not as expected"

# Test for CustomDataStructure
def test_custom_data_structure_equality():
    instance_a = CustomDataStructure([1, 2, 3])
    instance_b = CustomDataStructure([1, 2, 3])
    assert instance_a == instance_b, "Instances should be equal"

def test_custom_data_structure_truthiness():
    truthy_instance = CustomDataStructure([1])
    falsy_instance = CustomDataStructure([])
    assert truthy_instance, "Instance should be truthy"
    assert not falsy_instance, "Instance should be falsy"

# Test for transform_and_sum
def test_transform_and_sum():
    data = [1, 2, 3, 4, 5, 6]
    assert transform_and_sum(data) == 56, "Sum of squares of even numbers failed"

```

### Setup / How to initialize/run your application

To run this app, you must:

1. Create a Python **virtual environment**: `python3 -m venv .venv`.
2. Enter the **virtual environment**: `source .venv/bin/activate`.
3. Install required packages: `pip install -r requirements.txt`.
4. Modify and run `python -m runner`, or...
5. Run `pytest` to run unit tests.

### Links and Resources

- [Class Repo](https://canvas.instructure.com/courses/8309911/assignments/42655285)
- [How to Write Pythonic Code](https://builtin.com/data-science/pythonic)
- [Code Style](https://docs.python-guide.org/writing/style/)
