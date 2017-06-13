import src.read_data as read_data


def prepare_data(path_train):
	print("read from ", path_train)
	train_set = read_data.load_jpeg_data_in_fixed_size(path_train, 320, 240)


if __name__ == "__main__":
    prepare_data('/Users/bagbeom-yong/Workspace/spac_ml/SPaC_ML/dataset/benz/')
