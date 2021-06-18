import json
import os
import tkinter as tk
from typing import List, Tuple

from helpers import clear_screen
from products import render_products


def render_main_screen(window: tk.Tk):
    tk.Button(
        window, text='Login', background='green', foreground='white',
        command=lambda: render_login(window, on_success=render_products)
    ).grid(row=0, column=0)
    tk.Button(
        window, text='Register', background='yellow', foreground='black',
        command=lambda: render_register(window, on_success=render_main_screen)).grid(row=0, column=1)


def register(**user):
    with open(os.path.join('db', 'user_credentials.txt'), 'a') as user_credentials_fh:
        user_details = json.dumps(user)
        user_credentials_fh.write(user_details)
        user_credentials_fh.write('\n')


def render_register(window: tk.Tk, on_success):
    clear_screen(window)

    labels: List[tk.Label] = [
        tk.Label(window, text='User Name'),
        tk.Label(window, text='First Name'),
        tk.Label(window, text='Last Name'),
        tk.Label(window, text='Password'),
    ]

    for idx, label in enumerate(labels):
        label.grid(row=idx, column=0)

    inputs: List[Tuple[str, tk.Entry]] = [
        ('username', tk.Entry(window)),
        ('first_name', tk.Entry(window)),
        ('last_name', tk.Entry(window)),
        ('password', tk.Entry(window, show='*')),
    ]

    for idx, (user_attr, input) in enumerate(inputs):
        input.grid(row=idx, column=1)

    def on_click():
        error = register(**{user_attr: widget.get()
                         for user_attr, widget in inputs})
        if not error:
            clear_screen(window)
            on_success(window)
        else:
            tk.Label(window, text='error', background='red',
                     foreground='white').grid(row=0, column=4)

    tk.Button(
        window,
        text='Submit',
        command=on_click).grid(row=4, column=0)


def render_login(window: tk.Tk, on_success):
    clear_screen(window)

    inputs = [
        ('username', tk.Entry(window)),
        ('password', tk.Entry(window, show='*')),
    ]

    for idx, (user_attr, input) in enumerate(inputs):
        input.grid(row=idx, column=1)

    labels: List[tk.Label] = [
        tk.Label(window, text='User Name'),
        tk.Label(window, text='Password'),
    ]

    for idx, label in enumerate(labels):
        label.grid(row=idx, column=0)

    def on_click():
        if login(**{user_attr: widget.get()
                    for user_attr, widget in inputs}):
            on_success(window)
        else:
            tk.Label(window, text='Invalid username or password', background='red',
                     foreground='white').grid(row=0, column=4)

    tk.Button(
        window,
        text='Login',
        command=on_click
    ).grid(row=3, column=0)


def login(**user):
    with open(os.path.join('db', 'user_credentials.txt'), 'r') as user_credentials_fh:
        for line in user_credentials_fh:
            user_data = json.loads(line)
            if user_data['username'] == user['username'] and user_data['password'] == user['password']:
                with open(os.path.join('db', 'currenr_user.txt'), 'w')as current_user_fh:
                    current_user_fh.write(json.dumps(user_data))

                return True

    return False
