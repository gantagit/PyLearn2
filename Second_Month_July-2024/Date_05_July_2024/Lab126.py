# OS Module
# OS module provides functions for interacting with the Operating System
# get Current Working directory, change dir, file exist, filename, file size, envir

import os
import shutil
import time

os_path = os.path

print(os.name)  # Get the current os version

print(os.getcwd())
# os.chdir('/Second_Month_July-2024')  # Change the current working directory
#
# print(os.getcwd())  # Get the current working directory
# os.chdir('/Second_Month_July-2024/Date_05_July_2024')
# os.mkdir('mydir')  # Make a directory
print(os.getcwd())  # Get the current working directory
print(os.listdir())  # List all files and directories in the current working directory

print(os.path.exists('Lab126.py'))  # Check if a path exists
print(os.path.getsize('Lab126.py'))  # Get the size of a file
print(os.path.getmtime('Lab126.py'))  # Get the modification time of a file

print(os.path.realpath('Lab126.py'))  # Get the real path of a file

if os.path.exists('Lab126.py'):
    print('Path exists')
    # os.remove('Lab126.py') this line delete the file
    # print('File deleted')

    print(os.path.exists('Lab126.py'))

print(os.listdir(os.getcwd()))  # List all files and directories in the current working directory

epoch = os.path.getmtime('Lab126.py')
gmt_time = time.gmtime(epoch)

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", gmt_time)
print(formatted_time)
