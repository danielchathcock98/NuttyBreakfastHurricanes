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


    for part in os.listdir(TRAIN_DIR):
        if (part != '.DS_Store'):
            partPath = os.path.join(TRAIN_DIR, part)
            for filename in os.listdir(partPath):
                if (partPath != '.DS_Store'):
                    filepath = os.path.join(partPath, filename)

                    image = Image.open(filepath)
                    imageClass = labels[filename]
                    print(imageClass)




readImages()
