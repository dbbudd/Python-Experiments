#!/usr/bin/env python

import Tkinter as tk
from Tkinter import *
import pygame

#setup GUI Window
window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry("800x600")
window.title("EmuBot")


def keypress(event):
    print(event.char)


print("Press the <q> key to exit:")
window.bind_all('<Key>', keypress)
window.bind()


window.mainloop()