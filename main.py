import numpy as np
import src.read_data as read_data
import sys

def prepare_data(path_train):
     train_set = read_data.load_jpeg_data_in_fixed_size(path_train, 320, 240)
     num_train, w, h = train_set.shape

     if num_train == 0:
         print "Training set loading failed!!\n"
         return 0
     else:
         print "Training set", num_train, "x", w, "x", h, "are loaded."
         return train_set

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Usage : python main.py [TrainSet_Directory]"
        sys.exit()
    else:
        path_train = sys.argv[1]
        print "TrainSet Directory :", path_train
        
    prepare_data('/Users/js21c/jscode/SPaC_ML/dataset/benz/')

