# finally


class XYZ:

    def f1(self):
        try:
            a = int(input("Enter a number\t"))
        except ValueError as e:
            print("Please enter a valid number")
        else:
            print(f"You entered a number {a}")
        finally:
            print("Finally, i am executed all the times")


x = XYZ()
x.f1()
