import os
import json

JSON_PATH = r'dataset\training_set\political\json\ocr'
cur_dir =  os.getcwd() 
os.chdir('..')
parent_dir = os.getcwd() 
dir_path = os.path.join(parent_dir,JSON_PATH)

qt1 = []
qt2 = []
qt3 = []
qt4 = []

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

#print(ft1)
#print(ft2)
#print(ft3)
#print(ft4)

folder_index = 0
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
		
		#with open(folder_path,'rb') as json:
		#	print(json)
		#print(ft1_val,ft2_val,ft3_val,ft4_val)
		index += 1
	qt1.append(qt1_val)
	qt2.append(qt2_val)
	qt3.append(qt3_val)
	qt4.append(qt4_val)
	folder_index += 1


#print(qt1)
#print(qt2)
#print(qt3)
#print(qt4)
# --------------------------
qt1_sum = 0
for i in range(0,len(qt1)):
	qt1_sum  += qt1[i]
#print(qt1_sum) 

qt2_sum = 0
for i in range(0,len(qt2)):
	qt2_sum  += qt2[i]
#print(qt2_sum)

qt3_sum = 0
for i in range(0,len(qt3)):
	qt3_sum  += qt3[i]
#print(qt3_sum)

qt4_sum = 0
for i in range(0,len(qt4)):
	qt4_sum  += qt4[i]
#print(qt4_sum)

# --------------------------
ft1_sum = 0
for i in range(0,len(ft1)):
	ft1_sum  += ft1[i]
#print(ft1_sum) 

ft2_sum = 0
for i in range(0,len(ft2)):
	ft2_sum  += ft2[i]
#print(ft2_sum)

ft3_sum = 0
for i in range(0,len(ft3)):
	ft3_sum  += ft3[i]
#print(ft3_sum)

ft4_sum = 0
for i in range(0,len(ft4)):
	ft4_sum  += ft4[i]
#print(ft4_sum)

# ---------------------
print("probability of text appearing in a frame belonging to Q1,Q2,Q3,Q4 of a poltical ad video: ")
print([str(round(qt1_sum/ft1_sum,2)),str(round(qt2_sum/ft2_sum,2)),str(round(qt3_sum/ft3_sum,2)),str(round(qt4_sum/ft4_sum,2))])