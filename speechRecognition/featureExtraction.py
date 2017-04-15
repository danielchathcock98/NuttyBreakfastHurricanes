from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

import librosa
import librosa.display


filename = './HomeDepot/training/1.flac'
y, sr = librosa.load(filename)

for i in range(len(y)):
    print(y[i])

mfccs = librosa.feature.mfcc(y=y, sr=sr)

plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()
