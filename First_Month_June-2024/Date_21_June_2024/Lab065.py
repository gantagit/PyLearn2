# Tuple - Collection of items

# Example of matrix using tuples

hero_1 = ("Batman", "Bruce Wayne")
hero_2 = ("Spider man", "Peter Parker")

hero_3 = (hero_1, hero_2)
print(hero_3)  # prints tuple of hero_3 which is combined of hero_1 & hero_2 tuples

print(hero_3[0])  # prints first element of hero_3 tuple
print(hero_3[1])  # prints second element of hero_3 tuple

print(hero_3[0][0])  # prints first item of first element of hero_3 tuple
print(hero_3[0][1])  # prints second item of first element of hero_3 tuple

print(hero_3[1][0])  # prints first item of second element of hero_3 tuple
print(hero_3[1][1])  # prints second item of second element of hero_3 tuple
