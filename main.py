# Author Victour Bue
# This script will input a directory and for every image in said directory it will copy it in seperate directory
# Separated by Aspect Rati0

from email.mime import image
import pathlib
from re import S
from urllib import response
from PIL import Image
import os, os.path

import PIL

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def aspect_ratio(val, lim):
    lower = [0,1]
    upper = [1,0]

    while True:
        mediant = [lower[0] + upper[0], lower[1] + upper[1]]

        if (val * mediant[1] > mediant[0]):
            if (lim < mediant[1]):
                return upper
            lower = mediant
        elif (val * mediant[1] == mediant[0]):
            if (lim >= mediant[1]):
                return mediant
            if (lower[1] < upper[1]):
                return lower
            return upper
        else:
            if (lim < mediant[1]):
                return lower
            upper = mediant

# Get Input and Output Directory from User
def get_directory():
    print("Which directory would you like to sort by aspect ratio?")
    response = input()
    # Check if Valid Input
    # Search Computer's Hard Drive for matching directory
    
    if os.path.isdir(response):
        pass
        print("That is a valid directory.")
        # Check if there are images in directory
        print("Trying to load images...")
        return response
    else:
        print("That is not a valid directory.")
        return get_directory()

def get_limiter():
    print("Please select a limiter. This will set how aggressively the algorithm will match aproximate ratios. lower = more aggressive. 0 to disable.")
    response = input()
    return int(response)

# Load all images from directory
def load_and_sort_images(directory, limiter):
    images = pathlib.Path(directory)
    for path in images.iterdir():
        if not path.is_file():
            continue
        # TODO: handle image decoding errors
        image = PIL.Image.open(path)
        width = image.width
        height = image.height
        ratio = gcd(width,height)
        x = int(width /ratio)
        y = int(height/ratio)
        if limiter == 0:
            print(f"{x}:{y}")
            savepath = directory + f"\sorted_images\{x}x{y}"
            print(savepath)
            if (os.path.isdir(savepath)):
                image.save(f"{savepath}\{os.path.basename(image.filename)}")
            else:
                os.makedirs(savepath)
                image.save(f"{savepath}\{os.path.basename(image.filename)}")
            
            print("Sorted File Saved...")
        else:
            print(aspect_ratio(x/y, int(limiter)))
            x, y = aspect_ratio(x/y, int(limiter))
            savepath = directory + f"\sorted_images\{x}x{y}"
            print(savepath)
            if (os.path.isdir(savepath)):
                image.save(f"{savepath}\{os.path.basename(image.filename)}")
            else:
                os.makedirs(savepath)
                image.save(f"{savepath}\{os.path.basename(image.filename)}")
            
            print("Sorted File Saved...")
        
def repeat_sort():
    print("Would you like to sort a different directory? Or perhaps change the limiter? y/n")
    response = input()
    if(response == 'y'):
        main()
    elif(response == 'n'):
        quit()
    else:
        print("I'm sorry but I didn't understand that.")
        repeat_sort()


def main():
    path = get_directory()
    limiter = get_limiter()
    load_and_sort_images(path, limiter)
    repeat_sort()


main()