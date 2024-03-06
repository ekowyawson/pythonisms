from pythonista.pythonistic import PythonicCollection, CustomCollection, timer_decorator, CustomDataStructure, transform_and_sum

#################################################
# Demonstrating the custom collection
pc = PythonicCollection()
pc.add(1)
pc.add(2)
pc.add(3)

# Using in a for loop
for elem in pc:
    print(elem)

# Using in a list comprehension
squared_elems = [x**2 for x in pc]
print(squared_elems)

# Converting to a list
list_elems = list(pc)
print(list_elems)

#################################################
# Example usage
collection = CustomCollection([1, 2, 3, 4, 5])

# Using in a for loop
for item in collection:
    print(item)

# Using in a list comprehension
squared = [x**2 for x in collection]
print(squared)

# Converting to a list
list_converted = list(collection)
print(list_converted)

#################################################
# Demonstrating equality comparison
instance_a = CustomDataStructure([1, 2, 3])
instance_b = CustomDataStructure([1, 2, 3])
instance_c = CustomDataStructure([])

# Check equality
equality_ab = instance_a == instance_b  # Should be True
equality_ac = instance_a == instance_c  # Should be False

# Check truthiness
truthiness_a = bool(instance_a)  # Should be True
truthiness_c = bool(instance_c)  # Should be False

equality_ab, equality_ac, truthiness_a, truthiness_c