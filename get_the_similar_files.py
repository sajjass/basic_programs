import os, glob

os.chdir("/Users/sajjas/Desktop/")
for file in glob.glob("*.jpg"):
    print file