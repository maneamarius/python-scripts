#!/bin/bin/env python3

# we are trying to solve the following problem:
# find 49 cubes that can fit exactly inside a cube with size 6
# so we need to find cubes with any size smaller than 6 (1,2,3,4,5)
# which have a total volume of 216 (6^3)
# let x be an array which contains be the number of cubes with size 1,2,3,4,5
# let v be an array which contains the volume for those cubes with size 1,2,3,4,5

xmin = [0,    0,  0,  0,  0]
xmax = [1,    3,  8, 27, 49]
v =    [125, 64, 27,  8,  1]

for p in range(xmin[0], xmax[0]):
  for q in range(xmin[1], xmax[1]):
    for r in range(xmin[2], xmax[2]):
      for s in range(xmin[3], xmax[3]):
        for t in range(xmin[4], xmax[4]):
          volume = p*v[0] + q*v[1] + r*v[2] + s*v[3] + t*v[4]
          cubes = p + q + r + s + t
          numbers = [ p, q, r, s, t ]
          if volume == 216 and cubes == 49:
            print(p,q,r,s,t)

