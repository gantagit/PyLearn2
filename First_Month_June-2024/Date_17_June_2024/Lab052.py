# function with tuple

def pizza(*toppings):
    for i in toppings:
        print(i)


a = ("onion", "capsicum", "cheese", "olives")
b = ["pane", "tomato", "cheese"]
pizza(a)
pizza(b)

pizza("cheese", "tom")
