# driver function based on the browser type

def browser(name):
    name = name.lower()
    match name:
        case "chrome":
            print("You have opened the chrome browser")
        case "edge":
            print("you have opened the edge browser")
        case "firefox":
            print("You have opened the firefox browser")
        case _:
            print("You have entered wrong browser name")


browser("Edge")
browser("chrome")
browser("firefox")
browser("safari")
