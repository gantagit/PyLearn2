# Reading from CSV file

import csv

with open("login.csv") as Cfile:
    # Cfile = open("login.csv")
    reader = csv.reader(Cfile)
    for col in reader:
        print(col[0], col[1], sep=" | ")
    Cfile.close()
