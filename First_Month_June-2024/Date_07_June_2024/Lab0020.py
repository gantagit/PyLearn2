# List

shopping_list = ["milk", "eggs", "bread", "apples"]
print(len(shopping_list))
print(shopping_list)
print(type(shopping_list))

print(shopping_list[0])
print(shopping_list[-1])

shopping_list.append("bananas")  # add to the end
print(shopping_list)

shopping_list.insert(0, "chocolate")  # add to the beginning (index 0)
shopping_list.insert(1, "coffee")  # insert at the index 1
print(shopping_list)

shopping_list.extend(["mango", "pineapple"])  # add multiple items to the end
print(shopping_list)

shopping_list.remove("coffee")  # remove item
print(shopping_list)

shopping_list.pop()  # remove last item
print(shopping_list)

print(shopping_list.index("milk"))  # get index of item
print(shopping_list.count("milk"))  # get count of item

shopping_list.sort()  # sort list
print(shopping_list)

shopping_list.reverse()  # reverse list
print(shopping_list)
