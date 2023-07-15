#!/usr/bin/python3
import sys
 
"""new entry adds an entry to an existing file"""
def new_entry(entry):
    todo_list = open("Todolist.txt", "a")
    todo_list.writelines(entry)
    todo_list.close()

"""this lets you read from the terminal https://www.geeksforgeeks.org/take-input-from-stdin-in-python/"""
def read_from_stdin():
    for line in sys.stdin:
        if 'q' == line.rstrip():
            break
        try:
            new_entry(line)
            print(f'New Entry : {line}')
        except:
            print("failed to append to file")



"""if name is main is a way to run the script
from the terminal https://stackoverflow.com/questions/419163/what-does-if-name-main-do"""
if __name__ == "__main__":







    print(" Todo app\n Please enter new todo items. \n Press 'q + <Enter>' to exit")
    read_from_stdin()
