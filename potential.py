#-----------------------------------------------------------------------
# potential.py
#-----------------------------------------------------------------------
import sys

import stddraw
import stdio
import stdarray
from charge import Charge
from color import Color
from picture import Picture
from instream import InStream
from outstream import OutStream

# Read values from standard input to create an array of charged
# particles. Set each pixel color in an image to a grayscale value
# proportional to the total of the potentials due to the particles at
# corresponding points. Draw the resulting image to standard draw.

MAX_GRAY_SCALE = 255

# Read charges from standard input into an array.

n = 9
inFilenames = 'charges.txt'
instream = InStream(inFilenames)
charges1 = instream.readAllFloats()
charges=stdarray.create1D(n)
c=0
for i in range(0, n*3, 3):
    x0 = charges1[i]
    y0 = charges1[i+1]
    q0 = charges1[i+2]
    charges[c] = Charge(x0, y0, q0)
    c+=1

# Create a Picture depicting potential values.
pic = Picture()
for col in range(pic.width()):
    for row in range(pic.height()):
        # Compute pixel color.
        x = 1.0 * col / pic.width()
        y = 1.0 * row / pic.height()
        v = 0.0

        for i in range(n):
            v += charges[i].potentialAt(x, y)    
        v = (MAX_GRAY_SCALE / 2.0)  + (v / 2.0e10)
        if v < 0:
            grayScale = 0
        elif v > MAX_GRAY_SCALE:
            grayScale = MAX_GRAY_SCALE
        else:
            grayScale = int(v)            
        color = Color(grayScale, grayScale, grayScale)
        pic.set(col, pic.height()-1-row, color)

# Draw the Picture.
stddraw.setCanvasSize(pic.width(), pic.height())
stddraw.picture(pic)
stddraw.show()


#-----------------------------------------------------------------------

# python potential.py < charges.txt
