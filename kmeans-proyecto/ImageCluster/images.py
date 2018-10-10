from PIL import Image, ImageOps
from numpy import array
import math

def Euclidian3d(d1,d2):
    return math.sqrt(math.pow(d1[0]-d2[0],2)+math.pow(d1[1]-d2[1],2)+math.pow(d1[2]-d2[2],2))

image1 = Image.open('coke.jpg')
image1.load()
# r, g, b, a = image1.split()
# image1 = Image.merge('RGB',(r,g,b))
arr = array(image1)
# image1 = ImageOps.posterize(image1,8)
# print(arr[1])
# for x in arr:
#     print(x)
# print(arr[0][0],arr[51][0])
print(Euclidian3d(arr[0][0],arr[51][0]))
# image1.show()