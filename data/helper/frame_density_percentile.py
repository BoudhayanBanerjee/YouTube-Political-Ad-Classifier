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
ft5 = []
ft6 = []
ft7 = []
ft8 = []
ft9 = []
ft10 = []

for folder in os.listdir(dir_path):
	folder_path = os.path.join(dir_path,folder)
	list = os.listdir(folder_path)
	num_frame = len(list)
	if (num_frame % 10 == 0):
		percentile_num = num_frame // 10
		ft1.append(percentile_num)
		ft2.append(percentile_num)
		ft3.append(percentile_num)
		ft4.append(percentile_num)
		ft5.append(percentile_num)
		ft6.append(percentile_num)
		ft7.append(percentile_num)
		ft8.append(percentile_num)
		ft9.append(percentile_num)
		ft10.append(percentile_num)
	elif (num_frame % 10 == 1):
		percentile_num = num_frame // 10
		ft1.append(percentile_num)
		ft2.append(percentile_num)
		ft3.append(percentile_num)
		ft4.append(percentile_num)
		ft5.append(percentile_num)
		ft6.append(percentile_num)
		ft7.append(percentile_num)
		ft8.append(percentile_num)
		ft9.append(percentile_num)
		ft10.append(percentile_num+1)
	elif (num_frame % 10 == 2):
		percentile_num = (num_frame + 2) // 10
		ft1.append(percentile_num)
		ft2.append(percentile_num)
		ft3.append(percentile_num)
		ft4.append(percentile_num)
		ft5.append(percentile_num)
		ft6.append(percentile_num)
		ft7.append(percentile_num)
		ft8.append(percentile_num)
		ft9.append(percentile_num+1)
		ft10.append(percentile_num+1)
	elif (num_frame % 10 == 3):
		percentile_num = (num_frame + 1) // 10
		ft1.append(percentile_num)
		ft2.append(percentile_num)
		ft3.append(percentile_num)
		ft4.append(percentile_num)
		ft5.append(percentile_num)
		ft6.append(percentile_num)
		ft7.append(percentile_num)
		ft8.append(percentile_num+1)
		ft9.append(percentile_num+1)
		ft10.append(percentile_num+1)
	elif (num_frame % 10 == 4):
		percentile_num = (num_frame + 1) // 10
		ft1.append(percentile_num)
		ft2.append(percentile_num)
		ft3.append(percentile_num)
		ft4.append(percentile_num)
		ft5.append(percentile_num)
		ft6.append(percentile_num)
		ft7.append(percentile_num+1)
		ft8.append(percentile_num+1)
		ft9.append(percentile_num+1)
		ft10.append(percentile_num+1)
	elif (num_frame % 10 == 5):
		percentile_num = (num_frame + 1) // 10
		ft1.append(percentile_num)
		ft2.append(percentile_num)
		ft3.append(percentile_num)
		ft4.append(percentile_num)
		ft5.append(percentile_num)
		ft6.append(percentile_num+1)
		ft7.append(percentile_num+1)
		ft8.append(percentile_num+1)
		ft9.append(percentile_num+1)
		ft10.append(percentile_num+1)
	elif (num_frame % 10 == 6):
		percentile_num = num_frame // 10
		ft1.append(percentile_num)
		ft2.append(percentile_num)
		ft3.append(percentile_num)
		ft4.append(percentile_num)
		ft5.append(percentile_num+1)
		ft6.append(percentile_num+1)
		ft7.append(percentile_num+1)
		ft8.append(percentile_num+1)
		ft9.append(percentile_num+1)
		ft10.append(percentile_num+1)
	elif (num_frame % 10 == 7):
		percentile_num = num_frame // 10
		ft1.append(percentile_num)
		ft2.append(percentile_num)
		ft3.append(percentile_num)
		ft4.append(percentile_num+1)
		ft5.append(percentile_num+1)
		ft6.append(percentile_num+1)
		ft7.append(percentile_num+1)
		ft8.append(percentile_num+1)
		ft9.append(percentile_num+1)
		ft10.append(percentile_num+1)
	elif (num_frame % 10 == 8):
		percentile_num = (num_frame + 2) // 10
		ft1.append(percentile_num)
		ft2.append(percentile_num)
		ft3.append(percentile_num+1)
		ft4.append(percentile_num+1)
		ft5.append(percentile_num+1)
		ft6.append(percentile_num+1)
		ft7.append(percentile_num+1)
		ft8.append(percentile_num+1)
		ft9.append(percentile_num+1)
		ft10.append(percentile_num+1)
	elif (num_frame % 10 == 9):
		percentile_num = (num_frame + 1) // 10
		ft1.append(percentile_num)
		ft2.append(percentile_num+1)
		ft3.append(percentile_num+1)
		ft4.append(percentile_num+1)
		ft5.append(percentile_num+1)
		ft6.append(percentile_num+1)
		ft7.append(percentile_num+1)
		ft8.append(percentile_num+1)
		ft9.append(percentile_num+1)
		ft10.append(percentile_num+1)

folder_index = 0
f = open('percentile.csv', 'w' ,newline='')
writer = csv.writer(f)
writer.writerow( ('file_name', 'Q1', 'Q2', 'Q3', 'Q4','Q5','Q6','Q7','Q8','Q9','Q10',\
               'F1', 'F2', 'F3', 'F4','F5','F6','F7','F8','F9','F10',\
               'P1', 'P2', 'P3', 'P4','P5','P6','P7','P8','P9','P10') )
for folder in os.listdir(dir_path):
	folder_path = os.path.join(dir_path,folder)	
	ft1_val = ft1[folder_index]
	ft2_val = ft2[folder_index]
	ft3_val = ft3[folder_index]
	ft4_val = ft4[folder_index]
	ft5_val = ft5[folder_index]
	ft6_val = ft6[folder_index]
	ft7_val = ft7[folder_index]
	ft8_val = ft8[folder_index]
	ft9_val = ft9[folder_index]
	ft10_val = ft10[folder_index]
	#print(ft1_val,ft2_val,ft3_val,ft4_val)
	index = 0
	qt1_val = 0
	qt2_val = 0
	qt3_val = 0
	qt4_val = 0
	qt5_val = 0
	qt6_val = 0
	qt7_val = 0
	qt8_val = 0
	qt9_val = 0
	qt10_val = 0
	for file in os.listdir(folder_path):

		text_flag = False	

		file_path  = os.path.join(folder_path,file)
		#print("processing ",file_path)
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
			elif ( (index >= ft1_val + ft2_val + ft3_val + ft4_val) and (index < ft1_val + ft2_val + ft3_val + ft4_val + ft5_val) ):
				qt5_val += 1
			elif ( (index >= ft1_val + ft2_val + ft3_val + ft4_val + ft5_val) and (index < ft1_val + ft2_val + ft3_val + ft4_val + ft5_val + ft6_val) ):
				qt6_val += 1
			elif (index >= ft1_val + ft2_val + ft3_val + ft4_val + ft5_val + ft6_val and index <ft1_val + ft2_val + ft3_val + ft4_val + ft5_val + ft6_val + ft7_val):
				qt7_val += 1 
			elif ( (index >= ft1_val + ft2_val + ft3_val + ft4_val + ft5_val + ft6_val + ft7_val) and (index < ft1_val + ft2_val + ft3_val + ft4_val + ft5_val + ft6_val + ft7_val + ft8_val) ):
				qt8_val += 1
			elif ( (index >= ft1_val + ft2_val + ft3_val + ft4_val + ft5_val + ft6_val + ft7_val + ft8_val) and (index < ft1_val + ft2_val + ft3_val + ft4_val + ft5_val + ft6_val + ft7_val + ft8_val + ft9_val) ):
				qt9_val += 1
			elif (index >= ft1_val + ft2_val + ft3_val + ft4_val + ft5_val + ft6_val + ft7_val + ft8_val + ft9_val and index <ft1_val + ft2_val + ft3_val + ft4_val + ft5_val + ft6_val + ft7_val + ft8_val + ft9_val + ft10_val):
				qt10_val += 1 
		
		index += 1

	writer.writerow( (folder,qt1_val,qt2_val,qt3_val,qt4_val,qt5_val,qt6_val,qt7_val,qt8_val,qt9_val,\
		            qt10_val,ft1_val,ft2_val,ft3_val,ft4_val,ft5_val,ft6_val,ft7_val,ft8_val,ft9_val,ft10_val,\
		            str(round(qt1_val/ft1_val,2)),str(round(qt2_val/ft2_val,2)),str(round(qt3_val/ft3_val,2)),
		            str(round(qt4_val/ft4_val,2)),str(round(qt5_val/ft5_val,2)),str(round(qt6_val/ft6_val,2)),
		            str(round(qt7_val/ft7_val,2)),str(round(qt8_val/ft8_val,2)),str(round(qt9_val/ft9_val,2)),
		            str(round(qt10_val/ft10_val,2))))
	
	folder_index += 1

'''
#print(qt1)
#print(qt2)
#print(qt3)
#print(qt4)
#print(qt5)
#print(qt6)
#print(qt7)
#print(qt8)
#print(qt9)
#print(qt10)
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

qt5_sum = 0
for i in range(0,len(qt5)):
	qt5_sum  += qt5[i]
#print(qt3_sum)

qt6_sum = 0
for i in range(0,len(qt6)):
	qt6_sum  += qt6[i]
#print(qt4_sum)

qt7_sum = 0
for i in range(0,len(qt7)):
	qt7_sum  += qt7[i]
#print(qt3_sum)

qt8_sum = 0
for i in range(0,len(qt8)):
	qt8_sum  += qt8[i]

qt9_sum = 0
for i in range(0,len(qt9)):
	qt9_sum  += qt9[i]
#print(qt3_sum)

qt10_sum = 0
for i in range(0,len(qt10)):
	qt10_sum  += qt10[i]



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

ft5_sum = 0
for i in range(0,len(ft5)):
	ft5_sum  += ft5[i]
#print(ft3_sum)

ft6_sum = 0
for i in range(0,len(ft6)):
	ft6_sum  += ft6[i]
#print(ft4_sum)

ft7_sum = 0
for i in range(0,len(ft7)):
	ft7_sum  += ft7[i]
#print(ft3_sum)

ft8_sum = 0
for i in range(0,len(ft8)):
	ft8_sum  += ft8[i]

ft9_sum = 0
for i in range(0,len(ft9)):
	ft9_sum  += ft9[i]
#print(ft3_sum)

ft10_sum = 0
for i in range(0,len(ft10)):
	ft10_sum  += ft10[i]

# ---------------------
print("probability of text appearing in a frame belonging to P1,P2,P3,P4,P5,P6,P7,P8,P9,P10 of a poltical ad video: ")
print([str(round(qt1_sum/ft1_sum,2)),str(round(qt2_sum/ft2_sum,2)),str(round(qt3_sum/ft3_sum,2)),str(round(qt4_sum/ft4_sum,2))
	  ,str(round(qt5_sum/ft5_sum,2)),str(round(qt6_sum/ft6_sum,2)),str(round(qt7_sum/ft7_sum,2))
	  ,str(round(qt8_sum/ft8_sum,2)),str(round(qt9_sum/ft9_sum,2)),str(round(qt10_sum/ft10_sum,2))])
'''

