from PIL import Image, ImageOps
from numpy import array
image1 = Image.open('coke.jpg')
image1.load()
r, g, b, a = image1.split()
image1 = Image.merge('RGB',(r,g,b))
arr = array(image1)
# image1 = ImageOps.posterize(image1,8)
# print(arr[1])
for x in arr:
    print(x)
# image1.show()