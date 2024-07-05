my_dict = {
    'a': 3,
    'b': "Vijay",
    'C': 2
}

for k, v in my_dict.items():  # to check specific key is present in dictionary or not
    if k == 'b':
        print(my_dict[k])
    else:
        print(f"key {k} is not is not equal to b")

verify = 'b' in my_dict  # other way to check specific key is present in dictionary or not
print("b is present in my dictionary")
