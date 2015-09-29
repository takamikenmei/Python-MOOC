import os
def rename_files():
	# 1. Get filenames in folder
	file_list = os.listdir(r"D:\MOOC\python-mooc\prank\images")
	# print(file_list)
	os.chdir(r"D:\MOOC\python-mooc\prank\images")

	# 2. Rename files
	for file_name in file_list:
		os.rename(file_name, file_name.translate(None, "0123456789"))

	os.chdir(r"D:\MOOC\python-mooc\prank")

rename_files()