import subprocess
import os


'''
cmd = 'ls'
os.system(cmd)
val = os.popen('pwd').read()
print(val)
'''



os.system('npm install')
print('npm install successful')
val = os.system('npm run build')
print(val)

if val == 0:

        os.system('git add ../.')
        commit = 'git commit -m'+' "COMPX341-22A-A3 Commiting from CI/CD Pipeline"'
        os.system(commit)

        os.system('git push -u origin main')
        os.system('npm run start')
        print(commit)

else:
        print('something wrong')
        os._exit(0)
