# Write to a File

Testfile1 = "C:/Users/gvk97/PycharmProjects/PyLearn2/Second_Month_July-2024/Date_03_July_2024/Textfile1.txt"

file = open(Testfile1, "w")
file.write("\n Hai this is Vijay")  # this overwrites the content
# file.read()

file = open(Testfile1, "a")
file.write("\n Hai this is Ganta")  # append to the end
# file.read()

file = open(Testfile1, "r")  # reading the file
print(file.read())
file.close()
