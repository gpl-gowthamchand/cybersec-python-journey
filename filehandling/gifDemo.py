# to animate - back and forth repeatedly to make it look moving 

import sys

from PIL import Image

images = [] # empty list to store images

for arg in sys.argv[1:] :
    image = Image.open(arg) # arg to take input from the terminal -$ python ./gifDemo.py ./images/catImg_1.png ./images/catImg_2.png 
    images.append(image)

images[0].save(
    "catgif.gif", save_all=True, append_images=[images[1]], duratiion=200, loop=0
)