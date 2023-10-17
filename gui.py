import tkinter as tk
from tkinter import font
from CPU_info import win_cpu_freq, get_cpu_freq # Import functions from cpu_info module
from RAM_info import get_ram_info #Import functions from RAM_info module
from GPU_info import get_gpu_info
from Network_info import get_net_info
from Motherboard_info import get_motherboard_info
import platform

gui = tk.Tk()
gui.geometry("360x600")



cst_font = font.Font(family ="Helvetica", size=7)

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

def showGPU():
    gpu_info = get_gpu_info()
    gpuLabel.config(text=gpu_info)

def showMOBO():
    MOBO_info = get_motherboard_info()
    MOBOLabel.config(text=MOBO_info)

def showNet():
    net_info = get_net_info()
    netLabel.config(text=net_info)


menu = tk.StringVar()

cpuButton = tk.Button(gui, text="CPU Info", command=showCPU)
cpuButton.pack()
cpuLabel = tk.Label(gui, text="", justify=tk.CENTER)
cpuLabel.pack()

ramButton = tk.Button(gui, text="RAM Info", command = showRam)
ramButton.pack()
ramLabel = tk.Label(gui, text="", justify=tk.LEFT)
ramLabel.pack()

tk.Label(gui, text="Only use this button if NVIDIA Graphics Card Installed\n (Otherwise no Info will be Displayed)",justify=tk.CENTER).pack()

gpuButton = tk.Button(gui, text="GPU Info", command=showGPU)
gpuButton.pack()
gpuLabel = tk.Label(gui, text="", justify=tk.CENTER)
gpuLabel.pack()

MOBOButton = tk.Button(gui, text="Motherboard Info", command=showMOBO)
MOBOButton.pack()
MOBOLabel = tk.Label(gui, text="", justify=tk.CENTER, font=cst_font)
MOBOLabel.pack()

netButton = tk.Button(gui, text="Network Info", command=showNet)
netButton.pack()
netLabel = tk.Label(gui, text="", justify=tk.CENTER)
netLabel.pack()

gui.mainloop()