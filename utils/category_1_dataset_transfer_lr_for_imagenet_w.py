"""
Category 1 image dataset for transfer learning using imagenet weights

"""
import pandas as pd
import numpy as np
import glob
import shutil
import os

meta = pd.read_csv("meta.csv", sep=",")


index_cv = pd.read_csv("data_category1.csv", sep=",")

index_ = index_cv.values


meta = meta[['case_num','pigment_network','derm']]
meta.loc[meta['pigment_network']=='absent','pigment_network'] = int(0)
meta.loc[meta['pigment_network']=='typical','pigment_network'] = int(1)
meta.loc[meta['pigment_network']=='atypical','pigment_network'] = int(1)


src_dir = "C:\\Users\\bsars\\images"
###############################################################################

indices= []

for i in range(index_.shape[0]):
	indices.append(index_[i,0])
		
meta = meta.loc[indices]
data = meta.values

labels = data[:,[0,1]]
derm_images =  data[:,[0,2]]

negative_dir = "C:\\Users\\bsars\\images_category1\\negative"
positive_dir = "C:\\Users\\bsars\\images_category1\\positive"

for i in range(data.shape[0]):
	path = "C:/Users/bsars/images/"+ str(derm_images[i,1])
	if labels[i,1]==0:
		for jpgfile in glob.iglob(os.path.join(path )):
			shutil.copy(jpgfile, negative_dir)
	else:
		for jpgfile in glob.iglob(os.path.join(path )):
			shutil.copy(jpgfile, positive_dir)

###############################################################################
