from __future__ import with_statement

from PIL import Image
import numpy as np
import os

TRAIN_DIR = './HomeDepot/ImagesTrain'

def readImages():
    labels = {}

    for part in os.listdir(TRAIN_DIR):
        partPath = os.path.join(TRAIN_DIR, part)
        for filename in os.listdir(partPath):
            filepath = os.path.join(partPath, filename)

            image = Image.open(filepath)
            imageClass = labels[filename]




readImages()
