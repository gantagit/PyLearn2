# SET
# Example of Union and Intersection of Sets
# Set is a collection of elements where order is not considered and duplicates are not allowed.
# set gives the output in random order

# Union operation: Combines all unique elements from both sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set2.union(set1))
# print(set1 | set2)  # Alternative way to perform union
# Output: # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection operation: Finds common elements between both sets
print(set1.intersection(set2))  # Output: {4, 5}
print(set2.intersection(set1))
# print(set1 & set2)  # Alternative way to perform intersection
# Output:  {4, 5}

# Example of Difference operation
print(set1.difference(set2))  # Output: {1, 2, 3}
print(set2.difference(set1))  # Output: {6, 7, 8}
print(set1 - set2)  # Alternative way to perform difference
print(set2 - set1)  # Alternative way to perform difference
