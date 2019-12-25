import os
import sys
import shutil


def get_files_at(path):
	return os.listdir(path)

def print_files_at(path):
	print("Files at: ", path)
	files = get_files_at(path)
	for file in files:
		print(file)

# moves files
# shutil.move returns path the destination directory
# will create the specified destination directory if it does not exist
def move_file(source, destination):
	return shutil.move(source, destination)

def move_multiple_extensions(source, destination):
	extensions = ['.txt', '.pdf']

	files = get_files_at(source)
	for file in files:
		if any(ext in file for ext in extensions):
			move_file(source + file, destination)

def paths_exist(paths):
	exists = True

	for directory in paths:
		# check if the directory/path exists
		if not(os.path.isdir(directory)):
			exists = False

	if exists:
		return True
	else:
		return False


def main():
	source = "C:\\Users\\niran\\Downloads\\"
	destination = 'C:\\Users\\niran\\Desktop\\B\\'
	pdf_path = "C:\\Users\\niran\\Documents\\PDFs"
	word_path = "C:\\Users\\niran\\Documents\\Word downloads"
	excel_path = "C:\\Users\\niran\\Documents\\Excel downloads"
	

	paths = [] 
	paths.append(source)
	paths.append(destination)
	paths.append(pdf_path)
	paths.append(word_path)
	paths.append(excel_path)
	


	if paths_exist(paths):
		files = get_files_at(source)
		for file in files:
			if '.pdf' in file:
				move_file(source + file, pdf_path)
			if '.docx' in file:
				move_file(source + file, word_path)
			if '.xlsx' in file or '.csv' in file:
				move_file(source + file, excel_path)
			if '.bmp' in file:
				move_file(source + file, image_path)
	else:
		print("Invalid directory paths!")

	print_files_at(pdf_path)
	print_files_at(word_path)
	print_files_at(excel_path)

main()
