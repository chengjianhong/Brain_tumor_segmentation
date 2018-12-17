# coding=utf-8
import sys,os
sys.path.append('..')
import numpy as np
from scipy import ndimage
from loader.load_data import read_NIFTI
from metrics.tumor_category import *
"""
# 0，1，2，4 are respectively respresented the pixel values of background,encrotic,edema,enhancing_tumor 
"""


def dice_coefficient(y_true,y_pred):
    """
    :param y_true: the ground_truth
    :param y_pred: the predicted
    :return:
    """
    intersect = np.sum(np.multiply(y_true,y_pred))
    print(intersect)
    sum_true_pred = np.sum(y_true) + np.sum(y_pred)
    return 1 if sum_true_pred == 0 else 2 * intersect / sum_true_pred

def sensitivity(y_true,y_pred):
    """
    compute flase negative rate
    :param y_true:
    :param y_pred:
    :return:
    """
    intersect = np.sum(np.multiply(y_true, y_pred))
    sum_true = np.sum(y_true)
    return 1 if sum_true == 0 else intersect / sum_true

def specificity(y_true,y_pred):
    """
    compute flase positive rete(specificity)
    :param y_true:
    :param y_pred:
    :return:
    """
    intersect = np.sum(np.multiply(y_true == 0, y_pred == 0))
    sum_true = np.sum(y_true == 0)
    return 1 if sum_true == 0 else intersect / sum_true

def border_map(binary_img,neigh):
    """
    Creates the border for a 3D image
    """
    binary_map = np.asarray(binary_img, dtype=np.uint8)
    neigh = neigh
    west = ndimage.shift(binary_map, [-1, 0,0], order=0)
    east = ndimage.shift(binary_map, [1, 0,0], order=0)
    north = ndimage.shift(binary_map, [0, 1,0], order=0)
    south = ndimage.shift(binary_map, [0, -1,0], order=0)
    top = ndimage.shift(binary_map, [0, 0, 1], order=0)
    bottom = ndimage.shift(binary_map, [0, 0, -1], order=0)
    cumulative = west + east + north + south + top + bottom
    border = ((cumulative < 6) * binary_map) == 1
    return border


def border_distance(y_true,y_pred):
    """
    This functions determines the map of distance from the borders of the
    segmentation and the reference and the border maps themselves
    """
    neigh=8
    border_true = border_map(y_true,neigh)
    border_pred = border_map(y_pred,neigh)
    oppose_true = 1 - y_true
    oppose_pred = 1 - y_pred
    # euclidean distance transform
    distance_true = ndimage.distance_transform_edt(oppose_true)
    distance_pred = ndimage.distance_transform_edt(oppose_pred)
    distance_border_pred = border_true * distance_pred
    distance_border_true = border_pred * distance_true
    return distance_border_true, distance_border_pred

def hausdorff_distance(y_true,y_pred):
    """
    This functions calculates the average symmetric distance and the
    hausdorff distance between a segmentation and a reference image
    :return: hausdorff distance and average symmetric distance
    """
    true_border_dist, pred_border_dist = border_distance(y_true,y_pred)
    hausdorff_distance = np.max(
        [np.max(true_border_dist), np.max(pred_border_dist)])
    return hausdorff_distance




y_true = read_NIFTI(os.path.join(os.getcwd(),'truth.nii.gz'))
y_pred = read_NIFTI(os.path.join(os.getcwd(),'prediction.nii.gz'))

function_mask = (whole_tumor_mask,tumor_core_mask,enhanced_tumor_mask)

dice = [dice_coefficient(func(y_true),func(y_pred)) for func in function_mask]

sensitivity = [sensitivity(func(y_true),func(y_pred)) for func in function_mask]

specificity = [specificity(func(y_true),func(y_pred)) for func in function_mask]

hausdorff = [hausdorff_distance(func(y_true),func(y_pred)) for func in function_mask]
hausdorff_distance = hausdorff_distance(y_true == 0,y_pred == 0)
#print(hausdorff_distance)
#print('dice:',dice,'\nsensitivity:',sensitivity,'\nspecificity:',specificity,'\nhausdorff_distance:',hausdorff)

