#!/usr/bin/env python
# created by steven.liu
# 2016.12.23
from PIL import Image
im = Image.open('IMG_1820.PNG')

imgWidth = 340 # width of the image you cut off
startX = 205
startY = 638 # the first line position-y
splitPoxis = 12 # split height default 15
blackHeigh = 6 # black line height default 9
maxLineNumber = 28


# function to deal image
def pasteImg( startY, index):
    box = (startX, startY + splitPoxis*index-blackHeigh,startX + imgWidth,startY + splitPoxis*index)
    #print box
    region = im.crop(box)
    
    box_dealed = (startX,startY + splitPoxis * index,startX + imgWidth,startY + splitPoxis*index+blackHeigh)
    #print box
    region_dealed = im.crop(box_dealed)
    
    im.paste( region, box_dealed )


pasteImg(startY, 0)

for index in range(1,maxLineNumber):
    pasteImg( startY, index )


im.save('IMG_1820.dealed.jpg')
#im.show()
