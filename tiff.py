import numpy as np
import cv2
import time 

print("[INFO] warming up camera...")
cap = cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_FPS, 30)
# With webcam get(CV_CAP_PROP_FPS) does not work.
# Let's see for ourselves.
fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
# to get more properties cv.GetCaptureProperty(capture, property_id) - float

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow('Webcam',frame)
    # do what you want with frame
    #  and then save to file\
     # Number of frames to capture
    #writer = cv2.VideoWriter(args["output"], fourcc, args["fps"],
	#		(w, h), True)

    num_frames = 15;
    print ("Capturing {0} frames".format(num_frames))
 
    # Start time
    start = time.time()
     
    # Grab a few frames
    count = 0
    for i in xrange(0, num_frames) :
        ret, frame = cap.read()
    	#print "img_%d" %count
        count=count + 1
        cv2.imwrite('./%d.tiff' %count, frame)

    # End time
    end = time.time()
 
    # Time elapsed
    seconds = end - start
    print ("Time taken : {0} seconds".format(seconds))

    #cv2.imwrite('./img.tiff', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # you can increase delay to 2 seconds here
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()