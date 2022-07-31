import os
import shutil
import json

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

	# move wav files
	wav_folder = json_data['Wav_Folder']
	list_wav = [s for s in file_list if ((".WAV") in s) or ((".wav") in s)]
	for f_wav in list_wav:
		dest_path = wav_folder+'/'+id
		# create folder if not exists file path 
		if not os.path.exists(dest_path):
			os.makedirs(dest_path)
		# move file
		shutil.move(work_path+'/'+f_wav, dest_path+'/'+f_wav)

	# move csv files
	csv_folder = json_data['Csv_Folder']
	list_csv = [s for s in file_list if ((".CSV") in s) or ((".csv") in s)]
	for f_csv in list_csv:
		dest_path = csv_folder+'/'+id
		# create folder if not exists file path 
		if not os.path.exists(dest_path):
			os.makedirs(dest_path)
		shutil.move(work_path+'/'+f_csv, dest_path+'/'+f_csv)
