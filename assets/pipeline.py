import subprocess
import os
import argparse


#check the input from user
parse = argparse.ArgumentParser()
parse.add_argument('C_commit', type=ascii, help='input the commit text')
args=parse.parse_args()
#print(args.C_commit)
commit = 'git commit -m ' +args.C_commit
print(commit)


#npm start 
os.system('npm install')
print('npm install successful')
val = os.system('npm run build')
print(val)

if val == 0:

        os.system('git add ../.')
        #commit = 'git commit -m ' +'"COMPX341-22A-A3 Commiting from CI/CD Pipeline"'
        os.system(commit)

        os.system('git push -u origin main')
        os.system('npm run start')
        print('finish all')

else:
        print('something wrong')
        os._exit(0)


