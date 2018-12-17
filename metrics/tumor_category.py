# coding=utf-8
import numpy as np

tumor_category = ('whole_tumor','tumor_core','enhancing_tumor')

def whole_tumor_mask(data):
    return data > 0

def tumor_core_mask(data):

    return np.logical_or(data == 1, data == 4)

def enhancing_tumor_mask(data):
    return data == 4


