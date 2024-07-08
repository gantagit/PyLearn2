# finally


# with open('Textfile2.txt', 'r') as file:
#     print(file.read())

try:
    # with open('Textfile1.txt', 'r') as file:
    file = open('Textfile2.txt', 'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print(fnfe)
finally:
    try:
        file.close()
        print("File is closed")
    except NameError as ne:
        print(ne)
