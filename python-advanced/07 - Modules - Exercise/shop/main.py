import json
import tkinter as tk
from typing import List, Tuple

from authentification import render_main_screen
from canvas import window
from helpers import clear_screen

if __name__ == '__main__':
    render_main_screen(window)
    window.mainloop()
