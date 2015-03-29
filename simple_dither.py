#!/usr/bin/python 

import random

# laser bed geometry
xmax = 40
ymax = 40
quantum = 0.2

# length of time to lase a single dot
dwell = 0.5

# maximum distance between mechanical limit and working limit
padding = 10

# deterministic pro tempore
random.seed(0)

# reset laser 
print "(prepare laser)"
print "m5 (turn off laser)"
print "g0 x-%d y-%d (move to home) " % (xmax + padding, ymax + padding)
print "g92 x0 y0 (reset axes)"

for xstep in range(0, int(xmax / quantum)):
  x = xstep * quantum
  dots = 0
  for ystep in range(0, int(ymax / quantum)):
    y = ystep * quantum
    yd = y + quantum
    if random.randint(0, xmax / quantum) <= xstep:
      print "g0 x%.1f y%.1f" % (x, y)
      print "m3"
      print "g4 p%.1f" % dwell
      print "m5"
      dots += 1
  print "(printed %d dots on row %d)" % (dots, xstep)

