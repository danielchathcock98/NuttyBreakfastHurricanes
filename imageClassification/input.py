from __future__ import with_statement

from PIL import Image
import numpy as np


labels = {}
categoriesPath = './HomeDepot/categoriesTrain.txt';
f = categories = open(categoriesPath, 'r')
for line in f:
    values = line.split('|')
    labels[values[2].rstrip()] = values[1]
print(labels.keys())
