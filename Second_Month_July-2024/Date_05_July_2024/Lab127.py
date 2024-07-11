import os

# # home = os.getenv("path")
# #
# # # print(home)
# # # os.chdir('C:/Users/gvk97/PycharmProjects/PyLearn2')
# #
# cwd = os.getcwd()
# #
# # for root, dir, files in os.walk(cwd):
# #     print(f'Current Root: {root}', sep='\n')
# #     print(f'SUB Dir: {dir}', sep='\n')
# #     print(f'Files: {files}', sep='\n')
#
# file_open_read_mode = os.open('Textfile1.txt', os.O_RDWR)
# os.write(file_open_read_mode, b'Hello World')
# os.close(file_open_read_mode)
#
# # file_open_read_mode = os.open(cwd + '/Textfile1.txt', os.O_RDONLY)

file_name = os.open('Textfile1.txt', os.O_RDWR)
os.write(file_name, b'Hello World')
os.close(file_name)
