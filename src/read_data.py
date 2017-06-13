import numpy as np
import scipy.misc as misc
import os
import sys

def load_jpeg_data_in_blk(path_input, blk_size):
    num_patch = 0
    for root, dirs, files in os.walk(path_input):
        for file in files:
            im = misc.imread(path_input + file, mode='YCbCr')
            w, h, c = im.shape
            w_blk = int(w / blk_size)
            h_blk = int(h / blk_size)
            num_patch += (w_blk * h_blk)

    train_set = np.zeros([num_patch, blk_size, blk_size], dtype='float')
    cnt = 0

    for root, dirs, files in os.walk(path_input):
        for file in files:
            im = misc.imread(path_input + file, mode='YCbCr')
            w, h, c = im.shape
            im_y = im[0,:,:]
            w_blk = int(w / blk_size)
            h_blk = int(h / blk_size)

            for y_blk in range(0, h_blk):
                for x_blk in range(0, w_blk):
                    x = y_blk * blk_size
                    y = y_blk * blk_size
                    train_set[cnt] = im[y:y+blk_size, x:x+blk_size]
                    cnt = cnt + 1

def load_jpeg_data_in_fixed_size(path_input, w, h):
    num_img = 0

    for root, dirs, files in os.walk(path_input):
        num_patch = len(files)
        t_train_set = np.zeros([num_patch, h, w])

        for file in files:
            if os.path.splitext(file)[1].lower() == '.jpg':
                im = misc.imread(path_input + file, mode='YCbCr')
                im_y = im[:,:,0]
                resized_im = misc.imresize(im_y, [h, w], interp='lanczos')
                t_train_set[num_img] = resized_im
                num_img = num_img + 1

    if num_img > 0:
        train_set = t_train_set[0:num_img]
    else:
        train_set = []
            
    return train_set

            
