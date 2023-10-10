from tkinter import *
from CPU_info import win_cpu_freq, get_cpu_freq # Import functions from cpu_info module
import platform

gui = Tk()
gui.geometry("360x480")

sys = platform.system()


def show():
    cpu_info = ""
    if sys == "Windows":
        cpu_info = win_cpu_freq()
    else:
        cpu_info = get_cpu_freq()
    myLabel.config(text=cpu_info)

menu = StringVar()

drop = OptionMenu(gui, menu, "CPU", "GPU", "Motherboard", "Network", "RAM")
drop.pack()

myLabel = Label(gui, text="", justify=LEFT)
myLabel.pack()

myButton = Button(gui, text="CPU_Info", command=show)
myButton.pack()

gui.mainloop()