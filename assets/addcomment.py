import os


#the function add the first line of my name and ID or something else
def insert_line(file_name,line):
	dummy_file = file_name + '.bak'
	with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
		write_obj.write(line + '\n')
		for line in read_obj:
			write_obj.write(line)

	os.remove(file_name)
	os.rename(dummy_file,file_name)



#function get all the ts file
def getfile_name(n_cwd):
	
	path = n_cwd
	n_cwd = os.listdir(n_cwd)

	for file in n_cwd:
		file_path = os.path.join(path, file) #the file in the path
		if os.path.isdir(file_path):
			#print(file_path)
			getfile_name(file_path)
		elif os.path.isfile(file_path):
			if os.path.splitext(file)[1] == '.ts':


				#print(file)
				#print(file_path)
				#testpath= "/home/yx167/COMPX341-A3-1/assets/testfile.txt"



				namecomment = "//Yingxi Xue 1525640"
				insert_line(file_path,namecomment)
				
				

'''
	for i in n_cwd:
		if os.path.splitext(i)[1] == '.txt':
			print(i)
'''


#file = args.C_commit.replace("'","")

now_path = os.getcwd()
getfile_name(now_path)

