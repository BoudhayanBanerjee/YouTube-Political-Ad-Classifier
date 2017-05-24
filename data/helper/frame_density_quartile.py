import os
import json
import csv 
import pandas as pd 
import seaborn as sns

JSON_PATH = r'dataset\training_set\political\json\ocr'
cur_dir =  os.getcwd() 
os.chdir('..')
parent_dir = os.getcwd() 
dir_path = os.path.join(parent_dir,JSON_PATH)

ft1 = []
ft2 = []
ft3 = []
ft4 = []

for folder in os.listdir(dir_path):
	folder_path = os.path.join(dir_path,folder)
	list = os.listdir(folder_path)
	num_frame = len(list)
	if (num_frame % 4 == 0):
		quarter_num = num_frame // 4

		ft1.append(quarter_num)
		ft2.append(quarter_num)
		ft3.append(quarter_num)
		ft4.append(quarter_num)
	elif (num_frame % 4 == 1):
		quarter_num = num_frame // 4
		ft1.append(quarter_num)
		ft2.append(quarter_num)
		ft3.append(quarter_num)
		ft4.append(quarter_num + 1)
	elif (num_frame % 4 == 2):
		quarter_num = (num_frame + 2) // 4
		ft1.append(quarter_num)
		ft2.append(quarter_num)
		ft3.append(quarter_num)
		ft4.append(quarter_num - 2)
	elif (num_frame % 4 == 3):
		quarter_num = (num_frame + 1) // 4
		ft1.append(quarter_num)
		ft2.append(quarter_num)
		ft3.append(quarter_num)
		ft4.append(quarter_num - 1)


folder_index = 0
f = open('quartile.csv', 'w',newline='')
writer = csv.writer(f)
writer.writerow( ('file_name', 'Q1', 'Q2', 'Q3', 'Q4', 'F1', 'F2', 'F3', 'F4','P1','P2','P3','P4') )
for folder in os.listdir(dir_path):
	folder_path = os.path.join(dir_path,folder)	

	ft1_val = ft1[folder_index]
	ft2_val = ft2[folder_index]
	ft3_val = ft3[folder_index]
	ft4_val = ft4[folder_index]
	#print(ft1_val,ft2_val,ft3_val,ft4_val)
	index = 0
	qt1_val = 0
	qt2_val = 0
	qt3_val = 0
	qt4_val = 0
	for file in os.listdir(folder_path):

		text_flag = False	

		file_path  = os.path.join(folder_path,file)
		with open(file_path,'r') as json_data:
			data = json.load(json_data)
			
		try:
			for i in range(1,len(data['responses'][0]['textAnnotations'])):
				text_flag = True					
		except:
			text_flag = False

		if (text_flag == True):
			if (index < ft1_val):
				qt1_val += 1
			elif ( (index >= ft1_val) and (index < ft1_val + ft2_val) ):
				qt2_val += 1
			elif ( (index >= ft1_val + ft2_val) and (index < ft1_val + ft2_val + ft3_val) ):
				qt3_val += 1
			elif (index >= ft1_val + ft2_val + ft3_val and index <ft1_val + ft2_val + ft3_val + ft4_val):
				qt4_val += 1 

		index += 1
		
	writer.writerow( (folder,qt1_val,qt2_val,qt3_val,qt4_val,ft1_val,ft2_val,ft3_val,ft4_val,\
				      str(round(qt1_val/ft1_val,2)),str(round(qt2_val/ft2_val,2)),str(round(qt3_val/ft3_val,2)),\
				      str(round(qt4_val/ft4_val,2))) )	

	folder_index += 1

f.close()
