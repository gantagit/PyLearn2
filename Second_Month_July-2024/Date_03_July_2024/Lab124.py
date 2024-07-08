# Write to a File

Testfile1 = "C:/Users/gvk97/PycharmProjects/PyLearn2/Second_Month_July-2024/Date_03_July_2024/Textfile1.txt"

file = open(Testfile1, "r")  # reading the file
lines = file.readlines()
file.close()

for line in lines:
    print(line, end=" ")
