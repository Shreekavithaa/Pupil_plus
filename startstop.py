from Tkinter import *
import cv2
from PIL import Image, ImageTk

isrunning = 0
def Start():
    global isrunning
    if isrunning == 0:
        width, height = 800, 600
        cap = cv2.VideoCapture(0)
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, height)
        isrunning = 1
        lmain.pack(side = RIGHT)

        def show_frame():
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            if isrunning == 1:
                lmain.after(10, show_frame)

    show_frame()

def Stop():
    global isrunning
    isrunning = 0
    lmain.pack_forget()

root = Tk()
lmain = Label(root)

Button1 = Button(root, text = "Start", command = Start)
Button1.pack(side = LEFT)
Button2 = Button(root, text = "Stop", command = Stop)
Button2.pack(side = LEFT)

root.mainloop()
