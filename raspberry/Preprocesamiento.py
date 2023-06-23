import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

#Denoising 
def filtrado(img, gauss=True, bil=True, median=True, sharp=True):

    img_filtrada = img.copy()
    
    #Filtro Gaussiano
    if gauss:
        img_filtrada = cv2.GaussianBlur(img_filtrada, (5,5), 0)
    
    #Median filter
    if median:
        img_filtrada = cv2.medianBlur(img_filtrada, 5)
    
    #Sharpening
    if sharp:
        kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]]) 
        img_filtrada = cv2.filter2D(img_filtrada, -1, kernel)

    return img_filtrada

#Histogram equalization
def equalizeHistogram(img):

    r, g, b = cv2.split(img)

    eq_r = cv2.equalizeHist(r)
    eq_g = cv2.equalizeHist(g)
    eq_b = cv2.equalizeHist(b)

    img = cv2.merge([eq_r, eq_g, eq_b])

    return img


def detect_red(img):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    low_s, low_v = 150, 1
    high_s, high_v = 255, 255

    low1 = np.array([0, low_s, low_v])
    high1 = np.array([15, high_s, high_v])
    low2 = np.array([165, low_s, low_v])
    high2 = np.array([180, high_s, high_v])

    mask1 = cv2.inRange(img_hsv, low1, high1)
    mask2 = cv2.inRange(img_hsv, low2, high2)

    mask = cv2.bitwise_or(mask1, mask2)
    
    red = cv2.bitwise_and(img, img, mask=mask)

    # masked_image = cv2.bitwise_not(mask)
    # masked_image = cv2.cvtColor(masked_image, cv2.COLOR_GRAY2RGB)
    # masked_image = cv2.bitwise_and(img, masked_image)

    return red
