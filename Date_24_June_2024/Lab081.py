# filters
# allows to filter the elements
from unicodedata import numeric

# +++++++++++++++++++++++++++
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = lambda num: num % 2 == 0
even_numbers = filter(even, numbers_list)
print(list(even_numbers))

greater_than_five = lambda num: num > 5
print(list(filter(greater_than_five, numbers_list)))

# +++++++++++++++++++++++++++
char_list = ['a', 'b', 'c', 'd', 'e']


def vowels_check(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return char in vowels


print(list(filter(vowels_check, char_list)))

# +++++++++++++++++++++++++++
char_list = ['a', 'b', 'c', 'd', 'e']


def consonants_char(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter not in vowels


print(list(filter(consonants_char, char_list)))
