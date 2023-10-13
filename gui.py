from tkinter import *
from CPU_info import win_cpu_freq, get_cpu_freq # Import functions from cpu_info module
from RAM_info import get_ram_info #Import functions from RAM_info module
import platform

gui = Tk()
gui.geometry("360x480")

sys = platform.system()


def showCPU():
    if sys == "Windows":
        cpu_info = win_cpu_freq()
    else:
        cpu_info = get_cpu_freq()
    cpuLabel.config(text=cpu_info)



def showRam():
    ram_info = get_ram_info()
    ramLabel.config(text=ram_info)


menu = StringVar()

cpuButton = Button(gui, text="CPU_Info", command=showCPU)
cpuButton.pack()
cpuLabel = Label(gui, text="", justify=LEFT)
cpuLabel.pack()

ramButton = Button(gui, text="RAM_Info", command = showRam)
ramButton.pack()
ramLabel = Label(gui, text="", justify=LEFT)
ramLabel.pack()

def macTest():
    print("Button works")

testButton = Button(gui, text="Mac Test", command=macTest)
testButton.pack()

gui.mainloop()