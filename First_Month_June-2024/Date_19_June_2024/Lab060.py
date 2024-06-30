# Functions Scope and Lifetime
# function to check the given mumber is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
        # print(f"{num} is even")
    else:
        print(f"{num} is odd")


check_even_odd(5)

# using lambda
chk_evn_odd = lambda nums: print(f"{nums} is even") if nums % 2 == 0 else print(f"{nums} is odd")
chk_evn_odd(6)
