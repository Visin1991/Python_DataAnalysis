# this is a initial python script. just used for set up the intial content for the current programming

print('hi from GUI init')


from sys import path
from pprint import pprint

from os import getcwd, chdir, pardir



curFull = getcwd()	
curDir = curFull.split('\\')[-1] 
print(curDir)

if curDir == 'PyScripts':
	path.append(curFull + "/Folder1/Folder2/Folder3/Folder4")
	print("Hahahahaha")


pprint(path)
print('\n\n')
