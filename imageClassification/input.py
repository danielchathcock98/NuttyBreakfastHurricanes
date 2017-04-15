from __future__ import with_statement

from PIL import Image
import numpy as np
import os

TRAIN_DIR = './HomeDepot/ImagesTrain'
CATEGORIES_PATH = './HomeDepot/categoriesTrain.txt';

def readImages():

    labels = {}
    labelDict = {'Plumbing': 1, 'Outdoors': 2, 'Flooring': 3,
        'Lighting & Ceiling Fans': 4, 'Appliances': 5}
    with open(CATEGORIES_PATH, 'r') as f:
        for line in f:
            values = line.split('|')
            labels[values[2].rstrip()] = labelDict[values[1]]

    trainingData = np.empty((len(labels), 65, 65, 3), dtype=np.uint8)
    trainingLabels = np.empty((len(labels),), dtype=np.uint8)

    for part in os.listdir(TRAIN_DIR):
        i = 0;
        if (part != '.DS_Store'):
            partPath = os.path.join(TRAIN_DIR, part)
            for filename in os.listdir(partPath):
                if (partPath != '.DS_Store'):
                    filepath = os.path.join(partPath, filename)

                    image = np.array(Image.open(filepath))
                    if (np.shape(image) == (65, 65)):
                        temp = np.empty((65, 65, 3), dtype=np.uint8)
                        temp[:,:,0] = temp[:,:,1] = temp[:,:,2] = image
                        image = temp
                    trainingData[i] = image
                    imageClass = labels[filename]
                    trainingLabels[i] = imageClass
                    i += 1
                    if (i % 10000 == 0):
                        print(i)





readImages()
