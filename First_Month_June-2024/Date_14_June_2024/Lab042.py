# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# match case (Similar to Switch case Java)
browser = str(input("Enter the browser name:\t"))

match browser.lower():   # here lower() is used to convert the input string in lower case
    case "edge":
        print("You have opened the Edge browser")
    case "firefox":
        print("You have opened the Firefox browser")
    case "chrome":
        print("You have opened the chrome browser")
    case _:
        print("You have entered wrong browser name")
