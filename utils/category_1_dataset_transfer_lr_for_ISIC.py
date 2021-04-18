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


meta = meta[['pigment_network','derm', 'diagnosis']]
meta.loc[meta['pigment_network']=='absent','pigment_network'] = int(0)
meta.loc[meta['pigment_network']=='typical','pigment_network'] = int(1)
meta.loc[meta['pigment_network']=='atypical','pigment_network'] = int(1)
meta.loc[meta['diagnosis']=='melanoma (in situ)','diagnosis'] = int(1)
meta.loc[meta['diagnosis']=='melanoma (less than 0.76 mm)','diagnosis'] = int(1)
meta.loc[meta['diagnosis']=='melanoma (0.76 to 1.5 mm)','diagnosis'] = int(1)
meta.loc[meta['diagnosis']=='melanoma (more than 1.5 mm)','diagnosis'] = int(1)
meta.loc[meta['diagnosis']=='melanoma metastasis','diagnosis'] = int(1)
meta.loc[meta['diagnosis']=='melanosis','diagnosis'] = int(1)
meta.loc[meta['diagnosis']=='melanoma','diagnosis'] = int(1)
meta.loc[meta['diagnosis']=='melanoma','diagnosis' ] = int(1)
meta.loc[meta['diagnosis']=='basal cell carcinoma','diagnosis' ] = int(0)
meta.loc[meta['diagnosis']=='blue nevus','diagnosis' ] = int(0)
meta.loc[meta['diagnosis']=='combined nevus','diagnosis' ] = int(0)
meta.loc[meta['diagnosis']=='congenital nevus','diagnosis' ] = int(0)
meta.loc[meta['diagnosis']=='dermal nevus','diagnosis' ] = int(0)
meta.loc[meta['diagnosis']=='dermatofibroma','diagnosis' ] = int(0)
meta.loc[meta['diagnosis']=='lentigo','diagnosis' ] = int(0)
meta.loc[meta['diagnosis']=='miscellaneous','diagnosis' ] = int(0)
meta.loc[meta['diagnosis']=='recurrent nevus','diagnosis' ] = int(0)
meta.loc[meta['diagnosis']=='reed or spitz nevus','diagnosis' ] = int(0)
meta.loc[meta['diagnosis']=='vascular lesion','diagnosis' ] = int(0)



melanoma = meta[meta['derm'].notnull() & (meta['pigment_network'] == 1)& (meta['diagnosis'] == 1)]
non_mela = meta[meta['derm'].notnull() & (meta['pigment_network'] == 1)& (meta['diagnosis'] == 0)]

X_melanoma = melanoma.values
X_non_mela = non_mela.values


src_dir = "C:\\Users\\bsars\\images"
##############################################################################

melanoma_dir = "C:\\Users\\bsars\\images_for_ISIC_Cat_1\\Melanoma"
non_melanoma_dir = "C:\\Users\\bsars\\images_for_ISIC_Cat_1\\Non_melanoma"

for i in range(X_melanoma.shape[0]):
	path = "C:/Users/bsars/images/"+ str(X_melanoma[i,1])
	for jpgfile in glob.iglob(os.path.join(path )):
		shutil.copy(jpgfile, melanoma_dir)
		
for i in range(X_non_mela.shape[0]):		
	path = "C:/Users/bsars/images/"+ str(X_non_mela[i,1])
	for jpgfile in glob.iglob(os.path.join(path )):
		shutil.copy(jpgfile, non_melanoma_dir)

##############################################################################
