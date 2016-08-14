import os
import subprocess

defaultPath = 'G:\GitHub'
fileOrFiles = input('all or one: ')
if fileOrFiles == 'one':
    myFiles = [(input('Input the name of the folder: '))]
    print(myFiles)
elif fileOrFiles == 'all':
    myFiles = ['FE','git','Japanese','java','Lap trinh shell','linux','lpic1','lpic2','network','python','raspberry-pi','selenium','software','testing','training']

while True:
    condition = input('pull or add or commit or push or exit: ')
    if condition == 'pull':
        for fileName in myFiles:
            currentDir = os.chdir(os.path.join(defaultPath,fileName))
            subprocess.Popen(['cmd','/K','git pull origin master'])
        continue
    elif condition == 'add':
        for fileName in myFiles:
            currentDir = os.chdir(os.path.join(defaultPath,fileName))
            subprocess.Popen(['cmd','/K','git add *'])
        continue
    elif condition == 'commit':
        for fileName in myFiles:
            currentDir = os.chdir(os.path.join(defaultPath,fileName))
            subprocess.Popen(['cmd','/K','git commit -m abc'])
        continue
    elif condition == 'push':
        for fileName in myFiles:
            currentDir = os.chdir(os.path.join(defaultPath,fileName))
            subprocess.Popen(['cmd','/K','git push origin master'])
        continue
    elif condition == 'exit':
        break
