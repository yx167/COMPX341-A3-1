import subprocess
import os
from git import Repo

'''
cmd = 'ls'
os.system(cmd)
val = os.popen('pwd').read()
print(val)
'''

dirfile = os.path.abspath(os.path.join(os.getcwd(),".."))
repo = Repo(dirfile)

os.system('npm install')
print('npm install successful')
val = os.system('npm run build')
print(val)

if val == 0:
	'''
        os.system('git add ../.')
        commit = 'git commit -m'+'COMPX341-22A-A3 Commiting from CI/CD Pipeline'
        os.system(commit)
	'''
	g = repo.git
	g.add("--all")
	g.commit("-m COMPX341-22A-A3 Commiting from CI/CD Peipeline")
	g.push()
        #os.system('git push -u origin main')
	os.system('npm run start')
	print('finsh pipeline')

else:
	print('something wrong')
	os._exit(0)


