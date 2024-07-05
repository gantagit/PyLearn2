# SET
# Example

set1 = {1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12}

print(set1)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
print(len(set1))  # Output: 12

set1.remove(4)
print(set1)  # Output: {1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12}
print(len(set1))  # Output: 11

set1.add(13)
print(set1)  # Output: {1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13}
print(len(set1))  # Output: 12

set1.pop()
print(set1)  # Output: {1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 13}
# pop will remove the first item of the set
print(len(set1))  # Output: 11
