import tkinter as tk
root=tk.Tk()
root.title("Khalki Fashions")
root.geometry("2000x2000")
label=tk.Label(root,text="Hi customer",bg="black",fg="white",font=("Helvetica",16,"bold"))
label.place(x=200,y=200)
button=tk.Button(root,text="proceed")
button.place(x=300,y=300)
root.mainloop() 