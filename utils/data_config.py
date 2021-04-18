# import the necessary packages
import os

class Config_ISIC():
    def __init__(self, dataset_path = "dataset/ISIC/resnet", training_path ="training", val_path = "validation", test_path = "testing"):
        super(Config_ISIC,self).__init__()
        self.dataset_path = dataset_path
        self.training_path = os.path.sep.join([self.dataset_path, training_path])
        self.val_path = os.path.sep.join([self.dataset_path, val_path])
        self.test_path = os.path.sep.join([self.dataset_path, test_path])

class Config_Cat_1():
    def __init__(self, dataset_path = "dataset/7-points/images_category1", training_path ="training", val_path = "validation", test_path = "testing"):
        super(Config_Cat_1,self).__init__()
        self.dataset_path = dataset_path
        self.training_path = os.path.sep.join([self.dataset_path, training_path])
        self.val_path = os.path.sep.join([self.dataset_path, val_path])
        self.test_path = os.path.sep.join([self.dataset_path, test_path])

class Config_Cat_2():
    def __init__(self, dataset_path = "dataset/7-points/images_category2", training_path ="training", val_path = "validation", test_path = "testing"):
        super(Config_Cat_2,self).__init__()
        self.dataset_path = dataset_path
        self.training_path = os.path.sep.join([self.dataset_path, training_path])
        self.val_path = os.path.sep.join([self.dataset_path, val_path])
        self.test_path = os.path.sep.join([self.dataset_path, test_path])

class Config_Cat_3():
    def __init__(self, dataset_path = "dataset/7-points/images_category3", training_path ="training", val_path = "validation", test_path = "testing"):
        super(Config_Cat_3,self).__init__()
        self.dataset_path = dataset_path
        self.training_path = os.path.sep.join([self.dataset_path, training_path])
        self.val_path = os.path.sep.join([self.dataset_path, val_path])
        self.test_path = os.path.sep.join([self.dataset_path, test_path])

class Config_Cat_4():
    def __init__(self, dataset_path = "dataset/7-points/images_category4", training_path ="training", val_path = "validation", test_path = "testing"):
        super(Config_Cat_4,self).__init__()
        self.dataset_path = dataset_path
        self.training_path = os.path.sep.join([self.dataset_path, training_path])
        self.val_path = os.path.sep.join([self.dataset_path, val_path])
        self.test_path = os.path.sep.join([self.dataset_path, test_path])

class Config_Cat_5():
    def __init__(self, dataset_path = "dataset/7-points/images_category5", training_path ="training", val_path = "validation", test_path = "testing"):
        super(Config_Cat_5,self).__init__()
        self.dataset_path = dataset_path
        self.training_path = os.path.sep.join([self.dataset_path, training_path])
        self.val_path = os.path.sep.join([self.dataset_path, val_path])
        self.test_path = os.path.sep.join([self.dataset_path, test_path])

class Config_Cat_6():
    def __init__(self, dataset_path = "dataset/7-points/images_category6", training_path ="training", val_path = "validation", test_path = "testing"):
        super(Config_Cat_6,self).__init__()
        self.dataset_path = dataset_path
        self.training_path = os.path.sep.join([self.dataset_path, training_path])
        self.val_path = os.path.sep.join([self.dataset_path, val_path])
        self.test_path = os.path.sep.join([self.dataset_path, test_path])

class Config_Cat_7():
    def __init__(self, dataset_path = "dataset/7-points/images_category7", training_path ="training", val_path = "validation", test_path = "testing"):
        super(Config_Cat_7,self).__init__()
        self.dataset_path = dataset_path
        self.training_path = os.path.sep.join([self.dataset_path, training_path])
        self.val_path = os.path.sep.join([self.dataset_path, val_path])
        self.test_path = os.path.sep.join([self.dataset_path, test_path])