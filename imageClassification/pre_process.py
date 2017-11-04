"""Preprocessor for imageClassification images

This module contains some functions to take the jpeg images supplies for
the imageClassification challenge, and convert them into data which is easily
fed into tensorflow (along with the associated label of each image).

Author: Daniel Hathcock

"""

import os
import shutil
import sys
import random

from scipy import misc

OUT_DATA_DIR = '/tmp/image_classification/tf_data/'
IN_DATA_DIR = './HomeDepot/ImagesTrain/'
IN_DATA_LABELS = './HomeDepot/categoriesTrain.txt'
META_PATH = os.path.join(OUT_DATA_DIR, 'data.meta.txt')

LABEL_DICT = {'Plumbing': 0, 'Outdoors': 1, 'Flooring': 2,
              'Lighting & Ceiling Fans': 3, 'Appliances': 4}



def convert_images():
    """Convert the images at the supplied paths to raw binary data, prepended with
    the 1-byte label of that image.
    """
    if os.path.exists(OUT_DATA_DIR):
        shutil.rmtree(OUT_DATA_DIR)
    os.makedirs(OUT_DATA_DIR)

    # make class dictionary
    labels = {}

    with open(IN_DATA_LABELS, 'r') as f:
        for line in f:
            line_info = line[:-1].split('|')
            if len(line_info) != 3:
                print('Error:', line)
            labels[line_info[2]] = LABEL_DICT[line_info[1]]


    # iterate through images, and write raw to OUT_DATA_DIR
    # each bin file has 25 folders of pictures

    files = [open(os.path.join(OUT_DATA_DIR, 'data_batch_%d.bin' % n), 'wb') for n in range(6)]
    file_size = [0] * 6
    print(file_size)


    print('Converting images to raw binary. This may take some time...')

    for dir_num in range(141):
        # dynamic terminal output
        sys.stdout.write('\r%03d/140' % dir_num)
        sys.stdout.flush()

        dir_name = os.path.join(IN_DATA_DIR, 'part-%05d' % dir_num)
        # if not os.path.exists(dir_name):
        #     print('Error:', dir_name)
        for filename in os.listdir(dir_name):
            im = misc.imread(os.path.join(dir_name, filename), mode='RGB')
            # if im.ndim != 3:
            #     print('Error:', filename, im.shape)
            ind = random.randrange(6)

            files[ind].write(bytes([labels[filename]]))
            files[ind].write(im.tobytes())
            file_size[ind] += 1
    print()
    for f in files:
        f.close()

    total_epoch_size = sum(file_size)
    total_train_size = sum(file_size[:5])
    total_eval_size = file_size[5]

    with open(META_PATH, 'w') as f:
        f.write('%d,%d,%d' % (total_epoch_size, total_train_size, total_eval_size))

    print(file_size)
    print('Total num examples:', total_epoch_size)
    print('Total training examples (0 - 4):', total_train_size)
    print('Total eval examples (5):', total_eval_size)

    return (total_epoch_size, total_train_size, total_eval_size)


def maybe_convert():
    """If raw images not already converted at given directories, then convert."""
    if not os.path.exists(OUT_DATA_DIR) or not os.path.isfile(META_PATH):
        return convert_images()
    with open(META_PATH, 'r') as f:
        nums = f.read().split(',')

    total_epoch_size = int(nums[0])
    total_train_size = int(nums[1])
    total_eval_size = int(nums[2])

    return (total_epoch_size, total_train_size, total_eval_size)


if __name__ == '__main__':
    convert_images()
