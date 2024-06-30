# Dictionaries
# nothing but a Key value pair
# Dictionaries are mutable
# example of a dictionary
d = {"name": "vijay", "age": 20, "city": "chennai"}
print(d["name"])

# using dict keyword
d = dict(name="vijay", age=20, city="chennai")
print(d["name"])

my_contact = dict(
    name="Ganta",
    age=20,
    city="London")
print(my_contact["name"])
print(my_contact.keys())
print(my_contact.values())
print(my_contact.items())
print(my_contact)
print(len(my_contact))

# adding a new key value pair
my_contact["email"] = "XXXXXXXXXXXXXXX"

# change the value of name
my_contact["name"] = "vijay"

print(my_contact)

print(my_contact.get("name"))

print(type(my_contact["name"]))

print(id(my_contact["name"]))

print(list(my_contact.keys()))
for i in my_contact.keys():
    print(i)
    print(my_contact[i])

for k, v in my_contact.items():
    print(k, v)
