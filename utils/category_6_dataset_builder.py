import pandas as pd
import numpy as np
import glob
import shutil
import os

src_path = "./dataset/7-points/"
category_path = src_path +"images_category6/"


meta_train = pd.read_csv(src_path+"meta.csv", sep=",")
meta_val = pd.read_csv( src_path+"meta.csv", sep=",")
meta_test = pd.read_csv(src_path+"meta.csv", sep=",")

train_index_cv = pd.read_csv(src_path+"train_indexes.csv", sep=",")
val_index_cv = pd.read_csv(src_path+"valid_indexes.csv", sep=",")
test_index_cv = pd.read_csv(src_path+"test_indexes.csv", sep=",")

train_index_ = train_index_cv.values
val_index_ = val_index_cv.values
test_index_ = test_index_cv.values


meta_train = meta_train[['case_num','blue_whitish_veil','derm']]
meta_train.loc[meta_train['blue_whitish_veil']=='absent','blue_whitish_veil'] = int(0)
meta_train.loc[meta_train['blue_whitish_veil']=='present','blue_whitish_veil'] = int(1)

meta_val = meta_val[['case_num','blue_whitish_veil','derm']]
meta_val.loc[meta_val['blue_whitish_veil']=='absent','blue_whitish_veil'] = int(0)
meta_val.loc[meta_val['blue_whitish_veil']=='present','blue_whitish_veil'] = int(1)

meta_test = meta_test[['case_num','blue_whitish_veil','derm']]
meta_test.loc[meta_test['blue_whitish_veil']=='absent','blue_whitish_veil'] = int(0)
meta_test.loc[meta_test['blue_whitish_veil']=='present','blue_whitish_veil'] = int(1)


###############################################################################
indices_train = []

for i in range(train_index_.shape[0]):
	indices_train.append(train_index_[i,0])
		
meta_train = meta_train.loc[indices_train]
train_data = meta_train.values

train_labels = train_data[:,[0,1]]
train_derm_images =  train_data[:,[0,2]]

negative_train_dir = category_path+"training/negative"
positive_train_dir = category_path+"/training/positive"

for i in range( train_data.shape[0]):
	path = src_path+"images/"+ str(train_derm_images[i,1])
	if train_labels[i,1]==0:
		for jpgfile in glob.iglob(os.path.join(path )):
			shutil.copy(jpgfile, negative_train_dir)
	else:
		for jpgfile in glob.iglob(os.path.join(path )):
			shutil.copy(jpgfile, positive_train_dir)

###############################################################################
indices_val = []

for i in range(val_index_.shape[0]):
	indices_val.append(val_index_[i,0])
		
meta_val = meta_val.loc[indices_val]
val_data = meta_val.values

val_labels = val_data[:,[0,1]]
val_derm_images = val_data[:,[0,2]]

negative_val_dir = category_path+"validation/negative"
positive_val_dir = category_path+"validation/positive"

for i in range(val_data.shape[0]):
	path = src_path+"images/"+ str(val_derm_images[i,1])
	if val_labels[i,1]==0:
		for jpgfile in glob.iglob(os.path.join(path )):
			shutil.copy(jpgfile, negative_val_dir)
	else:
		for jpgfile in glob.iglob(os.path.join(path )):
			shutil.copy(jpgfile, positive_val_dir)

###############################################################################
indices_test = []

for i in range(test_index_.shape[0]):
	indices_test.append(test_index_[i,0])
	
meta_test = meta_test.loc[indices_test]
test_data = meta_test.values

test_labels = test_data[:,[0,1]]
test_derm_images =  test_data[:,[0,2]]

negative_test_dir = category_path+"testing/negative"
positive_test_dir = category_path+"testing/positive"

for i in range( test_data.shape[0]):
	path =  src_path+"images/"+ str(test_derm_images[i,1])
	if test_labels[i,1]==0:
		for jpgfile in glob.iglob(os.path.join(path )):
			shutil.copy(jpgfile, negative_test_dir)
	else:
		for jpgfile in glob.iglob(os.path.join(path )):
			shutil.copy(jpgfile, positive_test_dir)