# Dynamic type
# identifier = literal
name = input()
age = int(input())

i_am_good = True
he_is_bad = False

pi = 3.14

print(type(name), type(age), type(pi),  type(i_am_good), type(he_is_bad))
print(name, age, pi, i_am_good, he_is_bad)

complex_number = 1 + 2j

print(type(complex_number.real), type(complex_number.imag), sep=",")
print(complex_number)