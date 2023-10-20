import argparse
import glob
import math
import numpy as np
import cv2
import os
from pathlib import Path
from matplotlib import pyplot as plt


# Change the series of images to video
def convert_to_video(image_path, pathout, fps):

    files = []
    arr = []

    # For loop to loop through all the images and add the names to a list
    for f in os.listdir(pathin):
        if os.path.isfile(f):
            files.append(f)

    # In order to sort the files remove the letters from the file names and use files.sort
    files.sort(key = lambda  x: int(x[4:-4]))

    # Loop through the files and write them into the video file
    for i in range(len(files)):

        filename = pathin + files[i]

        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)

        arr.append(img)

        out = cv2.VideoWriter(pathout, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

        for i in range(len(arr)):
            out.write(arr[i])
        out.release()

# Adjust the image brightness
def brightness_adjustment(image, chp = 4):
    gray = image

    # We need to calculate the grayscale histogram
    hist = cv2.calcHist([gray], [0], None, [256], [0,256])
    hsize = len(hist)

    # Now we need to calculate the cumulative distribution from the histogram
    acc = []
    acc.append(float(hist[0]))
    for i in range(1, hsize):
        acc.append(acc[i - 1] + float(hist[i]))

    # Find the points to clip
    maxi = acc[-1]
    chp*= (maxi/100.0)
    chp /= 2.0

    # Find the left clipping point
    min = 0
    while acc[min] < chp:
        min += 1

    # Find the right clipping point
    max = hsize - 1
    while acc[max] >= (maxi - chp):
        max -= 1

    # Calculate alpha and beta values
    alpha = 255 / (max - min)
    beta = -min * alpha

    auto_result = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    return auto_result, alpha, beta

# Adjust the image gamma
def gamma_adjustment(image, gamma=1.0):

    invGamma = 1.0/gamma
    table = np.array([((i/255.0)** invGamma) *255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image,table)

# Get the first part of the path that will be used for the directories
wkd = Path.cwd()


# Parsing the arguments that will be used at run time
# Arguments that need to be passed are as follows:
#
# Directory "-d" flag - this is the path of the files that need to be edited this only has to be the path from current working directory to the directory containing the images
# output directory or "RequiredDirectory" with the "-r" flag ( Works the same as the -d flag)
# The directory needs to be passed with the folder that the python program is in as the working directory
# the corrupted images in the images folder and output them in the results folder
# i would pass " -d images/ -r results/"
# The resulting images and video are automatically put into results and results/vout/ respectively

parser = argparse.ArgumentParser(
    description='Perform Gamma correction on the provided image')

parser.add_argument('-d','--directory', required=True,metavar='', type=str, help='Specify the directory that contains the images')

parser.add_argument('-r','--ResultingDirectory', required=True,metavar='', type=str, help='specify the directory that the images go into')

args = parser.parse_args()


# Create variable to store path to images that need to be processed as well as where the new images and video will go
resulting_directory = os.path.join(wkd, args.ResultingDirectory, '')
wkd = os.path.join(wkd, args.directory, '')


# when working directory is feteched it returns address with '\' instead of '//'
# We need to change this when passing an argument to access the files in these directories
wkd = wkd.replace('\\', '/')
resulting_directory = resulting_directory.replace('\\', '/')

a = 1
resulting_directory = (resulting_directory)
os.chdir(resulting_directory)
img_array = []

for filename in os.listdir(wkd):


    f = os.path.join(wkd, filename)

    # Check if it is a file
    if os.path.isfile(f):
        point1 = np.float32([[20,20],[16, 385], [963, 374], [944,7]])
        point2 = np.float32([[0,0], [0, 393], [1023, 393], [1023,0]])

        # Read in image from file
        image = cv2.imread(f, cv2.IMREAD_COLOR)
        image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Use CLAHE to adjust contrast
        clache = cv2.createCLAHE(clipLimit=4)
        image_bw = cv2.medianBlur(image_bw,3)

        image_bw, alpha, beta = brightness_adjustment(image_bw)
        image_bw = gamma_adjustment(image_bw, gamma=4)

        width,height = 1023, 393
        matrix = cv2.getPerspectiveTransform(point1,point2)
        image_bw = cv2.warpPerspective(image_bw, matrix, (width, height))

        final_img = clache.apply(image_bw)

        cv2.imwrite(resulting_directory + '/test{}.png'.format(a), final_img)
        a += 1

pathin = resulting_directory
pathout = 'vout/video.avi'
fps = 3

# Convert the images into video
convert_to_video(pathin, pathout, fps)
