#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      india
#
# Created:     11/11/2022
# Copyright:   (c) india 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(50)
h = 0.5
for i in range(400):
    c = colorsys.hsv_to_rgb(h,1,1)
    h+=0.002
    t.color(c)
    t.fd(i)
    t.circle(90,steps=5)
    t.fd(i)
    t.rt(160)
    t.done()