import numpy as np
import cv2 as cv
import os
import random
import pickle as pikl
import hashlib as hlib

askIfNew = input("Is this the first time you're using SteamFace? (Type Y for yes or N for no)")

facestouseraccounts = {

}

userimgpath = ""
image = None
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera!")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Can't recieve frame (stream end?), exiting...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q') and askIfNew == "Y":
        if len(facestouseraccounts) == 0:
            name = input("What is your name?")
            userimgpath = os.curdir + 'training/'+random.randbytes(20)+".png"
            facestouseraccounts[name] = userimgpath
        
        with open("wb", "variables/savedvars.pkl") as f:
                pikl.dump(facestouseraccounts, f)
        image = cv.imwrite(userimgpath, ret)
        break
    elif cv.waitKey(1) == ord('q') and askIfNew == "N":
        if len(facestouseraccounts) == 0:
            with open("rb", "variables/savedvars.pkl") as f:
                facestouseraccounts = pikl.load(f)

        
        
        

cap.release()
cv.destroyAllWindows()