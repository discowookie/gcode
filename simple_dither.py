#!/usr/bin/python 

import random

xmax = 40
ymax = 40
quantum = 0.2

# number of oscillations when etching a single point
# TODO(cody): investigate using g4 (dwell) instead
burn_count = 10

# maximum distance between mechanical limit and working limit
overstep = 10

# deterministic pro tempore
random.seed(0)

# reset laser 
print "(resetting laser position)"
print "m5 (turn off laser)"
print "g0 x-%d y-%d (reset axis)" % (xmax + overstep, ymax + overstep)
print "g92 x0 y0 (set current position to zero)"

for xstep in range(0, int(xmax / quantum)):
  x = xstep * quantum
  dots = 0
  for ystep in range(0, int(ymax / quantum)):
    y = ystep * quantum
    yd = y + quantum
    if random.randint(0, xmax / quantum) <= xstep:
      print "(printing dot at (%.1f, %.1f))" % (x, y)
      print "g0 x%.1f y%.1f" % (x, y)
      print "m3"
      for time in range (0, burn_count):
        print "g1 x%.1f y%.1f" % (x, yd) # move it over one quantum
        print "g1 x%.1f y%.1f" % (x, y)  # and back
      print "m5"
      dots += 1
  print "(printed %d dots on row %d)" % (dots, xstep)

