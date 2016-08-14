import os
import subprocess

defaultPath = 'G:\GitHub'
fileOrFiles = input('all or one: ')
if fileOrFiles == 'one':
    myFiles = [(input('Input the name of the folder: '))]
    print(myFiles)
elif fileOrFiles == 'all':
    myFiles = ['FE','git','Japanese','java','Lap trinh shell','linux','lpic1','lpic2','network','python','raspberry-pi','selenium','software','testing','training']

condition = input('pull or push: ')
if condition == 'pull':
    for fileName in myFiles:
        os.chdir(os.path.join(defaultPath,fileName))
        subprocess.Popen(['cmd','/K','git pull origin master'])
elif condition == 'push':
    for fileName in myFiles:
        os.chdir(os.path.join(defaultPath,fileName))
        gitAdd = subprocess.Popen(['cmd','/K','git add *'])
        gitCommit = subprocess.Popen(['cmd','/K','git commit -m abc'])
        gitPush = subprocess.Popen(['cmd','/K','git push origin master'])
 
        

    
