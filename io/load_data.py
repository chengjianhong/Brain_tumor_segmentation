# coding=utf-8
import nibabel as nib

import os


def read_NIFTI(file_path):
    nii_image = nib.load(file_path)
    nii_image = nii_image.get_data()
    return nii_image

def train_test_split():
    return