
###############
# Exercise  1 #
###############
'''
    Write code to analyze each number between 2000 and 6500 and do the following (HINT use the range function)
     1.) If the number is divisible by 5 then print out [Fitty].
     2.) If the number is divisible by 7 then print out [Sevvy].
     3.) If the number is divisible by BOTH 5 and 7 print out ["Winner's win", said Bob] (quotes included)
'''

for num in range(2000, 6501):
    if num % 5 == 0:
        print(num, 'fitty')

    if num % 7 == 0:
        print(num, 'sevvy')

    if num % 5 == 0 and num % 7 == 0:
        print(num, '"Winner\'s win", said Bob')



###############
# Exercise  2 #
###############
'''
    Using the file "access.log", write code that does the following:
    
    1) Read the file into a list.
    2) Print out the following information:

    How many Total logs are there? 
    How many logs have a status code of 404? (Hint: Membership Checking)
    How many logs have a status code of 200?
    How many of the logs contain the text "mis"?

    3) Write some code that replaces all instances of "redflag" with "greenlight" (Hint: string replace method)
    4) Put all logs with the replaced values in a new list
    5) Create a file named "mis5400.log" and write out the list with the replaced values. 
'''

import os

os.chdir(r'C:\Users\Freddy\Desktop\Python Projects\access.log')
raw_log = open('access.log', 'r')
logs = raw_log.readlines()
raw_log.close()

total_404 = 0
total_200 = 0
total_mis = 0
new_log = []

for line in logs:
    if '404' in line:
        total_404 += 1
    if '200' in line:
        total_200 += 1
    if 'mis' in line:
        total_mis += 1

    new_log.append(line.replace('redflag', 'greenlight'))

print('Total Logs:', len(logs))
print('Total 404:', total_404)
print('Total 200:', total_200)
print('Total mis:', total_mis)

new_file = open('mis5400.log','w')
new_file.writelines(new_log)
new_file.close()
