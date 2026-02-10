
# Assignment 1 – Python with Data Analytics
# Name: Devesh Vashisth

# Q1. Why dictionary keys must be immutable
# Dictionary keys must be immutable because Python uses hashing.
# Immutable objects have fixed hash values, ensuring data integrity.

# Example
valid_dict = {1: "One", "two": 2}
print("Valid Dictionary:", valid_dict)

# Q2. Frequency of elements in a list
elements = [1, 2, 2, 3, 4, 1, 2, 3]
frequency = {}

for item in elements:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Frequency:", frequency)

# Q3. Difference between dict.get() and dict[key]
student = {"name": "Amit", "age": 20}

print("Using get():", student.get("marks"))  # Safe
# print(student["marks"])  # This would raise KeyError

# Q4. Merge two dictionaries keeping larger value
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 25, "c": 15, "d": 40}

merged = dict1.copy()
for key, value in dict2.items():
    if key in merged:
        merged[key] = max(merged[key], value)
    else:
        merged[key] = value

print("Merged Dictionary:", merged)

# Q5. Dictionary comprehension for odd numbers cube
numbers = [1, 2, 3, 4, 5, 6, 7]
cube_dict = {num: num**3 for num in numbers if num % 2 != 0}

print("Odd Cubes:", cube_dict)
