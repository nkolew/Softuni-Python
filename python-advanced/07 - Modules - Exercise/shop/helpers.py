import tkinter as tk


def clear_screen(window: tk.Tk):
    for el in window.grid_slaves():
        el.destroy()
