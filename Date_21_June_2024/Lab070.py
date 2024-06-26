# SET
# Example
# issubset() and issuperset() methods:
# issubset checks whether the set is subset or not and returns boolean
# issuperset checks whether the set is superset or not and returns boolean

set1 = {"A", "B", "C", "D"}
set2 = {"B", "C", "D"}

print(set1.issubset(set2))  # Output will be False
print(set2.issubset(set1))  # Output will be True

print(set1.issuperset(set2))  # Output will be True
print(set2.issuperset(set1))  # Output will be False
