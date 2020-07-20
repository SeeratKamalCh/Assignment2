import sys
from math import sqrt

if len(sys.argv) < 2:
    raise Exception("Usage: Number of triangles")
    sys.exit()

n = int(sys.argv[1])
count = 0

x2 = (1-sqrt(1+8*n))/2

if x2.is_integer():
    level = int(x2)*-1
    print("Levels:"+str(level))
    for i in range(level+1):
        for j in range(i):
            print("*", end="")
        print()
else:
    raise Exception("Usage: " + str(n) + " stars do not form a triangle shape:\
        Enter # of stars that form a triangle shape for example 1,3,6,10....")
