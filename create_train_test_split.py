import glob
import os
from shutil import copy

SIGNAL_IMAGES = glob.glob("dataset/*.jpg")
SIGNAL_LABELS = glob.glob("bounding-boxes-digits-infolks/*.txt")
YOLOv3_DATA_PATH = "yolov3/"
AMOUNT_OF_TEST_DATA = 0.2 # 20% test data
CLASSES = 10

def get_class_index_from_file(file_path):
    '''
    returns the class index of the first signal in a label file
    '''
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) < 1:
            return -1
        else:
            return int(lines[0].strip().split()[0])


def get_labels_files_by_class():
    '''
    returns a list of lists of labels file paths
    ordered by the class index of the first enty in the file
    '''
    empty_files = 0
    files_by_class = []
    for i in range(CLASSES):
        files_by_class.append([])

    for labels_file in SIGNAL_LABELS:
        class_index = get_class_index_from_file(labels_file)
        
        if class_index < 0:
            empty_files += 1
        else:
            files_by_class[class_index].append(labels_file)

    for f in files_by_class:
        print(len(f))

    print("empty files: {}".format(empty_files))

    return files_by_class


def find_matching_image_files(labels_files):
    '''
    after the labels files have been devided into a train and a test set,
    the corresponding images need to be split the same way
    '''
    train_image_files = []
    for f in labels_files:
        file_name = os.path.basename(f).split('.txt')[0]
        matching_files = [s for s in SIGNAL_IMAGES if "{}.jpg".format(file_name) in s]
        if len(matching_files) > 1:
            print("matching files: {}".format(matching_files))
            raise ValueError("ERROR: There should only be one matching file!")
        train_image_files.append(matching_files[0])
    return train_image_files


def copy_files(files, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    for f in files:
        copy(f, destination)


def create_data_file(data_file_name, data_path):
    '''
    list all relative paths to the files in the data_path in a text file
    this file is needed for training the yolov3 model 
    '''
    train_txt = open(data_file_name, "w")
    new_files = glob.glob("{}/*.jpg".format(data_path))
    for f in new_files:
        train_txt.write("{}\n".format(f))
    train_txt.close()


def prepare_dataset():
    if len(SIGNAL_IMAGES) != len(SIGNAL_LABELS):
        raise ValueError("ERROR: found {} images and {} labels. Expected an equal amount of files."
            .format(len(SIGNAL_IMAGES), len(SIGNAL_LABELS)))

    if not os.path.exists(YOLOv3_DATA_PATH):
        os.mkdir(YOLOv3_DATA_PATH)

    # train/test split will make the configured split on a class basis
    # this is done to ensure a good distribution of each class in the train and test set
    labels_files_by_class = get_labels_files_by_class()

    train_labels_files = []
    test_labels_files = []

    split = 1 / AMOUNT_OF_TEST_DATA
    count = 0
    for files_for_one_class in labels_files_by_class:
        for f in files_for_one_class:
            count += 1
            if count < split:
                train_labels_files.append(f)
            else:
                test_labels_files.append(f)
                count = 0

    print("train files: {}".format(len(train_labels_files)))
    print("test files: {}".format(len(test_labels_files)))

    train_image_files = find_matching_image_files(train_labels_files)
    test_image_files = find_matching_image_files(test_labels_files)

    train_files_destination_dir = os.path.join(YOLOv3_DATA_PATH, "train")
    test_files_destination_dir = os.path.join(YOLOv3_DATA_PATH, "test")

    copy_files(train_image_files, train_files_destination_dir)
    copy_files(train_labels_files, train_files_destination_dir)

    copy_files(test_image_files, test_files_destination_dir)
    copy_files(test_labels_files, test_files_destination_dir)

    create_data_file("train.txt", train_files_destination_dir)
    create_data_file("test.txt", test_files_destination_dir)
    

if __name__ == "__main__":
    prepare_dataset()