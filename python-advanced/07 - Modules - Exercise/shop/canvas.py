import tkinter as tk

from helpers import clear_screen


def create_window():
    window = tk.Tk()
    window.geometry('600x600')
    window.title('Product Shop')
    
    return window


window = create_window()
