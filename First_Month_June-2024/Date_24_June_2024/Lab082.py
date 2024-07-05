# map vs filter

numbers = [1, 2, 3, 4, 5]

square = lambda num: num ** 2
print(list(map(square, numbers)))  # map will perform on all the items and return all the items

even = lambda num: num % 2 == 0
print(list(filter(even, numbers)))  # filter will perform on all the items and return only the items which are true
