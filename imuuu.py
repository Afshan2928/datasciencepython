from tkinter import *
from PIL import Image,ImageTk
rt=Tk()
rt.title("fashion")
rt.geometry("2000x2500")
label=Label(rt,text="Hi customer",bg="black",fg="white",font=("Helvetica",16,"bold"))
label.place(x=200,y=200)
image=Image.open("fashion.jpg")
photo=ImageTk.PhotoImage(image)
lbl=Label(rt,image=photo)
lbl.pack()
button=Button(rt,text="proceed")
button.place(x=300,y=300)
rt.mainloop()