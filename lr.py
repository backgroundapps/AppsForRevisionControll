import os
file_name = raw_input('Inserir o nome do arquivo a ser gerado: ')


def open_file_to_get_the_last_revision(f):
	new_file = open(f)
	l = new_file.readlines(0)[0]
	new_file.close()
	return l
	
#this part of the code will select the files and find the head to prepare de process
def prepare_file():	
	if os.path.exists(file_name+'.txt'):
		os.remove(file_name+'.txt')
	list_files = os.listdir('.')
	
	f = open(file_name+'.txt','w')
	for i in list_files:
		if os.path.isfile(i):
			f.write(i+";"+open_file_to_get_the_last_revision(i).replace('head  ',''))
	f.close()
	print file_name+' gerado com sucesso!'



	
prepare_file()
