# Functions Scope and Lifetime
# Function with arguments list


numbers = [1, 2, 3, 4, 5]


def display_list(num):
    num.append(7)
    num[0] = 10
    return numbers


numbers.append(6)
result = display_list(numbers)
print(result)
