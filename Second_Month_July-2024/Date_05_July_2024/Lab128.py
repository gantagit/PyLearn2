import os


class Except(Exception):

    def __init__(self, msg):
        self.message = msg
        super().__init__(msg)


def get_browser() -> dict:
    browser_list = {
        "chrome": {"browser": "chromium"},
        "firefox": {"browser": "firefox"},
        "safari": {"browser": "webkit"},
        "edge": {"browser": "chromium", "channel": "msedge"},
    }

    env_browser: str = os.getenv("BROWSER", "chrome")
    if env_browser not in browser_list:
        raise Except("Invalid browser")

    return browser_list[env_browser]


# def get_os() -> dict:
#     os_list = {
#         "windows": {"os": "windows"},
#         "linux": {"os": "linux"},
#         "macos": {"os": "macos"},
#     }
#
#     env_os: str = os.getenv("OS", "windows")
#     if env_os not in os_list:
#         raise Except("Invalid OS")
#
#     return os_list[env_os]