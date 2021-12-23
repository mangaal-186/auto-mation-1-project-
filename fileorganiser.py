import os
import shutil

from backupfiles import ListOfFiles
path=input('Enter the name of directory to be sorted')
ListOfFiles=os.listdir(path)
for file in ListOfFiles:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=='':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move (path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move (path+'/'+file,path+'/'+ext+'/'+file)
