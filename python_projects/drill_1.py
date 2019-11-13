
import os
import time

ext = '.txt'

dirName = 'drill_Dir'

fName = 'drill_1.txt'

fPath = 'C:\\python_projects\\'


abPath = os.path.join(fPath,dirName)
print(abPath,"\n")


dirList = os.listdir(dirName)
# print the list
print(dirList,'\n')
for file in dirList:
    if file.endswith(ext):
        print(abPath,'\\',file)
        modTime = os.path.getmtime(os.path.join(abPath,file))
        # print the last modification time
        print(modTime)

        realTime = time.ctime(modTime)
        print(realTime,'\n')
