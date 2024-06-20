# Conditions
# nested if  else

agd = 25
play = "yes"

if agd > 18:
    print("You are adult")
    if play == "yes":
        print("You can play this game")
    else:
        print("You can't play this game")
else:
    print("You are not adult")
