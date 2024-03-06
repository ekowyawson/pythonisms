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
