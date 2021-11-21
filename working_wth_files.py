# this script takes some data from user's input and writes it to the new file
import sys

print("""You can write everything you want and we write it to the file named 'User_input.txt'
To stop writing text just enter the 'end' word with a new line""")

with open('User_input.txt', 'a') as usf:
    usr_inpt = input()
    while usr_inpt != 'end':
        usf.write(usr_inpt+'\n')
        usr_inpt = input()
    print("Everything is saved")
