# coding=utf-8
import nibabel as nib
import numpy as np
import os


def save_whole_tumor_label(truth_path,save_path):
    nii_data = nib.load(truth_path)
    nii_image = nii_data.get_data()
    image = np.copy(nii_image)
    image[image == 1] = 2
    image[image == 4] = 2
    new_image = nib.Nifti1Image(image,nii_data.affine,nii_data.header)
    nib.save(new_image,os.path.join(save_path,'truth_wt.nii.gz'))

def save_tumor_core_label(truth_path,save_path):
    nii_data = nib.load(truth_path)
    nii_image = nii_data.get_data()
    image = np.copy(nii_image)
    image[image == 2] = 0
    new_image = nib.Nifti1Image(image, nii_data.affine, nii_data.header)
    nib.save(new_image, os.path.join(save_path, 'truth_tc.nii.gz'))

def save_enhancing_core_label(truth_path,save_path):
    nii_data = nib.load(truth_path)
    nii_image = nii_data.get_data()
    image = np.copy(nii_image)
    image[image == 1] = 0
    image[image == 2] = 0
    new_image = nib.Nifti1Image(image, nii_data.affine, nii_data.header)
    nib.save(new_image, os.path.join(save_path, 'truth_ec.nii.gz'))