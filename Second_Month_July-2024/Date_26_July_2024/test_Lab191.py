# use of "conftest.py"

def test_check_something(launch_browser, close_browser):
    launch_browser
    print("test use of conftest.py")
    close_browser
