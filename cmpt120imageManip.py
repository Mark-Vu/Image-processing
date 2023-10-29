# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Minh Vu
# Date: Dec 6th, 2021
# Student ID: 301474569
# Description: This program is created to manipulate image
# Note: Code tested in Visual Studio Code
import cmpt120imageProjHelper as helper


def applyRedFilter(pixels):
    """
    Input:  pixel parameter is the 2D R/G/B array representing the image
    Returns: a 2D R/G/B array representing the red-filtered image
    """
    for rows in pixels:
        for cols in rows:
            cols[1] = 0
            cols[2] = 0

    return pixels


def applyGreenFilter(pixels):
    """
    Input:  pixel parameter is the 2D R/G/B array representing the image
    Returns: a 2D R/G/B array representing the green-filtered image
    """
    for rows in pixels:
        for cols in rows:
            cols[0] = 0
            cols[2] = 0

    return pixels


def applyBlueFilter(pixels):
    """
    Input:  pixel parameter is the 2D R/G/B array representing the image
    Returns: a 2D R/G/B array representing the blue-filtered image
    """
    for rows in pixels:
        for cols in rows:
            cols[0] = 0
            cols[1] = 0

    return pixels


def applySepiaFilter(pixels):
    """
    Input:  pixel parameter is the 2D R/G/B array representing the image
    Returns: a 2D R/G/B array representing the sepia-filtered image
    """
    for rows in pixels:
        for cols in rows:
            sepia_red = int(cols[0]*.393 + cols[1]*.769 + cols[2]*.189)
            sepia_green = int(cols[0]*.349 + cols[1]*.686 + cols[2]*.168)
            sepia_blue = int(cols[0] * .272 + cols[1]*.534 + cols[2]*.131)

            cols[0] = min(sepia_red, 255)
            cols[1] = min(sepia_green, 255)
            cols[2] = min(sepia_blue, 255)
    return pixels


def applyWarmFilter(pixels):
    """
    Input:  pixel parameter is the 2D R/G/B array representing the image
    Returns: a 2D R/G/B array representing the warm-filtered image
    """
    for rows in pixels:
        for cols in rows:
            if cols[0] < 64:
                cols[0] = int(cols[0]/64 * 80)
            elif 64 <= cols[0] < 128:
                cols[0] = int((cols[0]-64)/(128-64) * (160-80) + 80)
            else:
                cols[0] = int((cols[0]-128)/(255-128) * (255-160) + 160)

            if cols[2] < 64:
                cols[2] = int(cols[2]/64 * 50)
            elif 64 <= cols[1] < 128:
                cols[2] = int((cols[2]-64)/(128-64) * (100-50) + 50)
            else:
                cols[2] = int((cols[2]-128)/(255-128) * (255-100) + 100)
    return pixels


def applyColdFilter(pixels):
    """
    Input:  pixel parameter is the 2D R/G/B array representing the image
    Returns: a 2D R/G/B array representing the cold-filtered image
    """
    pixels = applyWarmFilter(pixels)
    for rows in pixels:
        for cols in rows:
            temp = cols[0]
            cols[0] = cols[2]
            cols[2] = temp
    return pixels


def rotateLeft(pixels):
    """
    Input:  pixel parameter is the 2D R/G/B array representing the image
    Returns: 2D R/G/B array with the original rotate left
    """
    rows = len(pixels)
    columns = len(pixels[0])
    new_img = helper.getBlackImage(rows, columns)
    for i in range(rows):
        for j in range(columns):
            new_img[j][i] = pixels[i][columns-j-1]
    return new_img

def rotateRight(pixels):
    """
    Input:  pixel parameter is the 2D R/G/B array representing the image
    Returns: 2D R/G/B array with the original rotate right
    """
    rows = len(pixels)
    columns = len(pixels[0])
    new_img = helper.getBlackImage(rows, columns)
    for i in range(rows):
        for j in range(columns):
            new_img[j][i] = pixels[rows-i-1][j]
    return new_img
 
def doubleSize(pixels):
    """
    Input:  pixel parameter is the 2D R/G/B array representing the image
    Returns: 2D R/G/B array that is 2x bigger then the original image
    """
    rows = len(pixels)
    columns = len(pixels[0])
    new_img = helper.getBlackImage(columns * 2,rows * 2)
    for i in range(rows):
        for j in range(columns):
            new_img[i*2+1][j*2] = pixels[i][j]
            new_img[i*2+1][j*2+1] = pixels[i][j]
            new_img[i*2][j*2+1] = pixels[i][j]
            new_img[i*2][j*2] = pixels[i][j]
    return new_img

def halfSize(pixels):
    """
    Input:  pixel parameter is the 2D R/G/B array representing the image
    Returns: 2D R/G/B array that is 2x smaller then the original image
    """
    rows = len(pixels)
    columns = len(pixels[0])
    new_img = helper.getBlackImage(int(columns/2),int(rows/2))
    for i in range(rows - 1):
        for j in range(columns - 1):
            new_img[int(i/2)][int(j/2)] = pixels[i][j]
    return new_img

def draw_box(pixels, top_left, top_right, bottom_left, bottom_right):
    """
    Input:  pixels-2D R/G/B array representing the image
            top_left-list containing the value of the row and column of the top left corner
            of the fish
            top_right-list containing the value of the row and column of the top right corner
            of the fish
            bottom_left-list containing the value of the row and column of the bottom left corner
            of the fish
            bottom_right-list containing the value of the row and column of the bottom right corner
            of the fish
    Returns: 2D R/G/B array with the box around the fish
    """
    #drawing the top and bottom lines of the fish
    for i in range(top_left[1], top_right[1]):
        pixels[top_left[0]][i] = [0, 255, 0]
        pixels[bottom_left[0]][i] = [0,255,0]
    
    #Drawing the left and right lines of the fish
    for i in range(top_left[0], bottom_left[0]):
        pixels[i][top_left[1]] = [0, 255, 0]
        pixels[i][top_right[1]] = [0, 255, 0]
    
    return pixels

def locateFish(pixels):
    """
    Input: pixels-2D R/G/B array representing the image
    Returns: 2D R/G/B array with the box around the fish
    """
    rows = len(pixels)
    columns = len(pixels[0])
    #x,y is a list containing all the rows and columns that contains the fish color
    x = []
    y = []
    
    for i in range(rows):
        for j in range(columns):
            each_pixel = pixels[i][j]
            r = each_pixel[0]
            g = each_pixel[1]
            b = each_pixel[2]
            h, s, v = helper.rgb_to_hsv(r,g,b)
            if 54 <= h <= 90  and 30 <= s <= 65 and 85 <= v <= 100:
                x.append(i)
                y.append(j)
    
    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)
    #we can find the top left, top right, bottom left and bottom right corner of the fish
    #by taking the greatest and smallest value of x and y
    top_left = [min_x, min_y]
    top_right = [min_x, max_y]
    bottom_left = [max_x, min_y]
    bottom_right = [max_x, max_y]
    
    return draw_box(pixels, top_left, top_right, bottom_left, bottom_right)