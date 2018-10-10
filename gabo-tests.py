# on cmd execute the following commands
# pip3 install pillow
# pip3 install numpy
from PIL import Image
from numpy import array
myImage = Image.open("test.jpg")
myImage.load()
arr = array(myImage)
print(arr)