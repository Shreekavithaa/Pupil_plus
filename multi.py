import multiprocessing
import Tkinter as tk
import cv2 
import time 
from PIL import Image, ImageTk
import numpy as np
from Tkinter import *

e = multiprocessing.Event()
p = None

# -------begin capturing and saving video
def startrecording(e):
    cap = cv2.VideoCapture(0)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 680)
    cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 340)
    print("[INFO] warming up camera...")
#cap = cv2.VideoCapture(0)
#cap.set(cv2.cv.CV_CAP_PROP_FPS, 30)
# With webcam get(CV_CAP_PROP_FPS) does not work.
# Let's see for ourselves.
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    # to get more properties cv.GetCaptureProperty(capture, property_id) - float
    
    while(True):

        num_frames = 15;
        print ("Capturing {0} frames".format(num_frames))
 
        # Start time
        start = time.time()
     
        # Grab a few frames
        count = 0
        for i in xrange(0, num_frames) :
            ret, frame = cap.read()
            #ret, frame = cap.read()
            cv2.imshow('Webcam',frame)
            #print "img_%d" %count
            count=count + 1
            cv2.imwrite('./%d.tiff' %count, frame)

        # End time
        end = time.time()
 
        # Time elapsed
        seconds = end - start
        print ("Time taken : {0} seconds".format(seconds))


    while(cap.isOpened()):
        if e.is_set():
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            e.clear()
        ret, frame = cap.read()
        if ret==True:
            out.write(frame)
        else:
            break

def start_recording_proc():
    global p
    p = multiprocessing.Process(target=startrecording, args=(e,))
    p.start()

# -------end video capture and stop tk
def stoprecording():
    e.set()
    p.join()

    root.quit()
    root.destroy()

if __name__ == "__main__":
    # -------configure window
    root = tk.Tk()
    root.geometry("%dx%d+0+0" % (100, 100))
    startbutton=tk.Button(root,width=10,height=1,text='START',command=start_recording_proc)
    stopbutton=tk.Button(root,width=10,height=1,text='STOP', command=stoprecording)
    startbutton.pack()
    stopbutton.pack()

    # -------begin
    root.mainloop()