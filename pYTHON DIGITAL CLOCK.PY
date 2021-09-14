from datetime import *
from tkinter import *
def time():
    dt = datetime.now()
    timeto = dt.strftime("%H:%M:%S %p")
    my_label.config(text = timeto)
    my_label.after(1000, time)
root = Tk()
root.title("Clock")
my_label = Label(root, fg = "cyan", bg = "black", font = ("ds-digital",80,"bold"))
my_label.pack()
time()
root.mainloop()
