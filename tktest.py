import Tkinter as tk
import cv2
from PIL import Image, ImageTk
#camera = Camera(camera=0)
width, height = 400, 300
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)
lmain.pack()
lmain1 = tk.Label(root)
lmain1.pack(side=tk.LEFT)
def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    #lmain.after(10, show_frame)
    lmain1.imgtk = imgtk
    lmain1.configure(image=imgtk)
    lmain1.after(10, show_frame)
show_frame()

#lmain1.after(10, show_frame)
root.mainloop()
