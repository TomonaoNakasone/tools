import os
import json
import re
import shutil

# cd execute folder
os.chdir(os.path.dirname(__file__))

# read config
json_file = open('config.json', 'r', encoding='utf-8')
json_data = json.load(json_file)

work_root = json_data['Work_Root']
tsid_list = os.listdir(work_root)
for id in tsid_list:
	work_path = work_root+'/'+id

	# Get files name
	file_list = os.listdir(work_path)

	# change name of jpg files
	list_jpg = [s for s in file_list if ((".JPG") in s) or ((".jpg") in s)]
	for f in list_jpg:
		regex_list = json_data['Regex_List']
		for r in regex_list:
			# rename
			regex = re.compile(r['Regex_Word'])
			if regex.search(f):
				f_new = regex.sub(r['Chenge_Word'], f)
				shutil.move(work_path+'/'+f, work_path+'/'+f_new)
