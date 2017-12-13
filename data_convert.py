import os

PATH = '/media/scyang/scyang/personal/Database/ILSVRC2012/'

def untar_train_data():
    train_names = os.listdir(os.path.join(PATH,'train'))
    out_dir = os.path.join(PATH, 'train_data')
    for train_name in train_names:
        train_dir_name = os.path.join(out_dir, train_name.split('.')[0])
        sub_dir = os.path.join(os.path.join(PATH,'train'), train_name)
        if not os.path.exists(train_dir_name):
            os.mkdir(train_dir_name)

        # print(sub_dir, train_dir_name)
        os.system('tar -xvf %s -C %s' %(sub_dir, train_dir_name))

def get_train_file_name():
    train_labels = os.listdir(os.path.join(PATH, 'train_data'))
    with open('train_name_paths.txt', 'w') as f:
        for train_label in train_labels:
            label_path = os.path.join(os.path.join(PATH, 'train_data'), train_label)
            lable_names = os.listdir(label_path)
            for label_name in lable_names:
                img_path = os.path.join(label_path, label_name)
                f.write(img_path + '\n')

def get_train_label():

untar_train_data()
