from tkinter import *
from PIL import Image, ImageTk
rt=Tk()
rt.title("image")
rt.geometry("1600x1400")
photo =ImageTk. PhotoImage(file="flowers.jpg")#to display image
lbl = Label(rt,image=photo)
lbl.pack()
rt.mainloop()