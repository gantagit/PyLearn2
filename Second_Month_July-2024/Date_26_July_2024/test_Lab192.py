import csv

from dotenv import load_dotenv
import os


def test_variables_dotenv():
    load_dotenv()
    url = os.getenv("URL")
    print(url)
    cwd = os.getcwd()
    print(cwd)



