# coding=utf-8
import nibabel as nib
import numpy as np
import glob
import os


def read_NIFTI(file_path):
    """
    :param file_path: the nifti files path
    :return: the data of nifti
    """
    nii_image = nib.load(file_path)
    nii_image = nii_image.get_data()
    return nii_image

def train_test_split(train_path,test_path,seed = 42):
    """
    :param train_path:
    :param test_path:
    :param seed:
    :return:
    """
    train_list = os.listdir(glob.iglob(train_path))
    test_list = os.listdir(glob.iglob(test_path))
    train_set = []
    train_label = []

    test_set = []
    test_label = []

    for file in train_list:

        print(file)
        nii_data = read_NIFTI(os.path.join(train_path,file))
        train_set.append(nii_data)

    for file in test_list:
        nii_data = read_NIFTI(os.path.join(train_path,file))
        test_set.append(nii_data)

    print(train_set)
    return train_set,train_label,test_set,test_label

#train_path = '/Users/cheng/Desktop/MICCAI_BraTS17_Data_Training/LGG/**'
#test_path = '/Users/cheng/Desktop/MICCAI_BraTS17_Data_Training/HGG/**'

#train_list = os.listdir(glob.glob(train_path))
#print(train_list)
#train_test_split(train_path,test_path)