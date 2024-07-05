# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# match case (Similar to Switch case Java)


number = int(input("Enter the number:\t"))

match number:
    case 1:
        print(" you have entered number {}".format(number))
    case 2:
        print(" you have entered number {}".format(number))
    case _:  # here _ is default
        print("number out of range")
