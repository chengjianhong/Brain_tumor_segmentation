# coding=utf-8
import nibabel as nib
import numpy as np

import os


def read_NIFTI(file_path):
    nii_image = nib.load(file_path)
    nii_image = nii_image.get_data()
    return nii_image

def train_test_split(data,labels,te):
    return

num=0
np.random.seed(5)
while(num<5):

    print(np.random.random())
    num+=1
