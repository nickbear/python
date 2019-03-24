# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 23:59:47 2019

@author: nickbear
"""

import os
import time

#The files and directories to be backed up are specified in a list
#source = ['"D:\\Program Files\\Beyond Compare 4"', 'D:\\tf']
source = '/root/桌面/Python-3.7.0/Modules'
# Notice we had to use double quotes inside the string for names with spaces in it

#The backup must be stored in a main backup directory
target_dir = '/root/桌面/code/target'

#The files are backed up into a zip file.
#The current day is the name of the subdirectory in the main directory
today = target_dir + os.sep + time.strftime('%Y%m%d')

# The current time is the name of the zip archive
now = time.strftime('%H%M%S')

# Take a comment from the user to create the name of the zip file
comment = input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
    comment.replace(' ','_') + '.zip'

#Create the directory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) #make directory
    print('Successfully created directory', today)

#We use the zip command to put the files in a zip archive
zip_command = "zip -qr {0} {1}".format(target,source)
print(zip_command)
# Run the backup
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
#zip -qr D:\VMware\20190324\223747.zip D:\tf
