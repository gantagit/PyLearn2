# How to achieve append in tuple

# ++++++++++++++++++++++++++++++++
t1 = (1, 2, 3)
new_t = t1 + (4,)
print(new_t)

# +++++++++++++++
# using new tuple
list_1 = list(t1)
list_1.append(4)
print(list_1)
t2 = tuple(list_1)
print(t2)


#  +++++++++++++++++++
def append_to_tuple(tuple_a, value):
    """Convert tuple to list, append value, convert back to tuple"""
    list_a = list(tuple_a)
    list_a.append(value)
    tuple_a = tuple(list_a)
    return tuple_a


print(t1)  # this prints (1,2,3)
t1 = append_to_tuple(t1, 4)
print(t1)  # this prints (1, 2, 3, 4)
