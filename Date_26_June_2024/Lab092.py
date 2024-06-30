from Lab091 import Calc

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

cal = Calc(num1, num2)

perform = int(input("Enter"
                    "\n1 for Addition"
                    "\n2 for Subtraction"
                    "\n3 for Multiplication"
                    "\n4 for Division"
                    "\n5 for Modulo"
                    "\n6 for Floor Division"
                    "\n7 for Power\n"))

match perform:
    case 1:
        print(cal.add())
    case 2:
        print(cal.minus())
    case 3:
        print(cal.multiply())
    case 4:
        print(cal.divide())
    case 5:
        print(cal.modulo())
    case 6:
        print(cal.floor_div())
    case 7:
        print(cal.power())
    case _:
        print("Invalid Input")
