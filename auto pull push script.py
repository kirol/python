import os
import subprocess

def myprocess(data):
    proc = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    procOutput, procError = proc.communicate()
    print("")
    print(procOutput)
    print(procError)
    print("")
    return proc.returncode

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
            pullCmd = r"""cmd /K git pull origin master"""
            myprocess(pullCmd)
        continue
    elif condition == 'push':
        for fileName in myFiles:
            currentDir = os.chdir(os.path.join(defaultPath,fileName))
            addCmd = r"""cmd /K git add *"""
            if myprocess(addCmd) == 0:
                commitCmd = r"""cmd /K git commit -m 'abc'"""
                if myprocess(commitCmd) == 0:
                    pushCmd = r"""cmd /K git push origin master"""
                    myprocess(pushCmd)
        continue
    elif condition == 'exit':
        break
