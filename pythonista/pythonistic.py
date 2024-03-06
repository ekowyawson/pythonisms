from functools import reduce
import time


class PythonicCollection:
    def __init__(self, elements=None):
        if elements is None:
            elements = []
        self._elements = elements

    def __iter__(self):
        """Make the collection iterable"""
        for element in self._elements:
            yield element

    def add(self, element):
        """Add an element to the collection"""
        self._elements.append(element)


class CustomCollection:
    def __init__(self, elements):
        self._elements = elements

    def __iter__(self):
        """Make the collection iterable v2"""
        return iter(self._elements)

    def __len__(self):
        """Return the size of the collection"""
        return len(self._elements)


class CustomDataStructure:
    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        """Compare two CustomDataStructure instances based on their data"""
        return self.data == other.data

    def __bool__(self):
        """Return truthiness of instance based on if it contains data"""
        return bool(self.data)
    

def transform_and_sum(data):
    """Filter even numbers, square them, then sum the squares"""
    filtered_data = filter(lambda x: x % 2 == 0, data)
    squared_data = map(lambda x: x**2, filtered_data)
    result = reduce(lambda x, y: x + y, squared_data)
    return result


def timer_decorator(func):
    """Decorator that prints the execution time of the function it decorates"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time} seconds.")
        return result
    return wrapper
