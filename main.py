import glob
import os
import cv2
from os.path import isfile, join
import numpy as np
from matplotlib import pyplot as plt

path=os.getcwd()
file_path=path+'/archive'
img_path=path+'/archive/images'
onlyfiles = [f for f in os.listdir(img_path) if isfile(join(img_path, f))]

IMAGE_SIZE = 224
data_path = join(img_path,'*g')
files = glob.glob(data_path)
files.sort()
X=[]
print(files)

for f1 in files:
    img = cv2.imread(f1)
    img = cv2.resize(img, (IMAGE_SIZE,IMAGE_SIZE))
    X.append(np.array(img))

plt.figure(figsize=(10, 20))
for i in range(0, 17):
    plt.axis('off')
    plt.imshow(X[i])
    plt.show()