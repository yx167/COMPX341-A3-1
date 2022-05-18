import subprocess
import os



os.system('npm install')
print('npm install successful')
val = os.system('npm run build')


if val == 0:


        os.system('git add ../.')
        commit = 'git commit -m'+'COMPX341-22A-A3 Commiting from CI/CD Pipeline'
        os.system(commit)
        os.system('git push -u origin main')
        os.system('npm run start')
        print('finsh pipeline')

else:
        print('something wrong')
        os._exit(0)


