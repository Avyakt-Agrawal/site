
import os
from os.path import join

lookfor = "IMG_097.img"
for root, dirs, files in os.walk('C:\\'):
    print("searching", root)
    if lookfor in files:
        print("found: %s" % join(root, lookfor))
        a = open(root, "r")
        print(a.read)
        break
