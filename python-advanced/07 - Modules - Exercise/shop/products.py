import os
import json
import tkinter as tk
from typing import Text

from helpers import clear_screen
from PIL import Image, ImageTk

ROW_SIZE = 5


def render_products(window: tk.Tk):
    clear_screen(window)

    with open(os.path.join('db', 'products.txt')) as products_fh:

        current_row = current_col = 0

        for product_idx, line in enumerate(products_fh):
            product = json.loads(line)

            if product_idx % ROW_SIZE == 0:
                current_row += 3
                current_col = 0

            tk.Label(window, text=product['name']).grid(
                row=current_row, column=current_col)

            image = Image.open(os.path.join(
                'db', 'img', product['img_path']))
            image = image.resize((100, 100))
            tk_image = ImageTk.PhotoImage(image)
            lbl = tk.Label(window, image=tk_image)
            lbl.image = tk_image
            lbl.grid(row=current_row+1, column=current_col)

            tk.Label(window, text=product['count']).grid(
                row=current_row+2, column=current_col)

            tk.Button(window, text=f'Buy {product["name"]}').grid(
                row=current_row+3, column=current_col)

            current_col += 1
