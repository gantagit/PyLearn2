import csv
import os
import pandas as pd

cwd = os.getcwd()
test_csv_file = cwd + '/testdata.csv'


class Test_CRUD(object):
    def test_csv(self):
        with open(test_csv_file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0], row[1])

    def test_csv_using_pandas(self):
        df = pd.read_csv(test_csv_file)
        print(df)
