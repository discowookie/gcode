#!/usr/bin/python 

import random

# defs
length=50
width=40
step=0.2
  
# reset
print("g0 x-50 y-50 ( reset axis )")
print("g92 x0 y0 ( set current position to x=0,y=0 )")

for row in range(0, int(length/step)):
  # 250 rows
  random.seed()
  dots = 0
  for col in range(0, int(width/step)):
    # 200 cols
    r = random.randint(0, length/step)
    if(r <= int(row)):
      print "g1 x%.1f y%.1f" % (row*step, col*step) 
      print "M3"
      print "g1 x%.1f y%.1f" % (row*step, (col+1)*step) # move it over one step
      print "M5"
      dots += 1
  print "( printed %d dots, going to new line )" % dots

