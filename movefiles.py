import os
import shutil
source=input('Enter the source folder name')
destination=input('Enter the destination folder name')
source=source+'/'
destination=destination+'/'
ListOfFiles=os.listdir(source)
for file in ListOfFiles:
    shutil.move((source+file),destination)