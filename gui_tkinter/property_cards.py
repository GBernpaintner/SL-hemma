from tkinter import *
from tkinter import ttk


default_title_width = 7

def label_row(parent, title, text, *, title_width=default_title_width):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text=title, width=title_width).grid(row=0, column=0, sticky=W)
    ttk.Label(frame, text=text).grid(row=0, column=1)
    return frame


def entry_row(parent, title, textvariable, *, title_width=default_title_width):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text=title, width=title_width).grid(row=0, column=0, sticky=W)
    ttk.Entry(frame, textvariable=textvariable).grid(row=0, column=1)
    return frame


def option_row(parent, title, textvariable, options, *, title_width=default_title_width):
    frame = ttk.Frame(parent)
    ttk.Label(frame, text=title, width=title_width).grid(row=0, column=0, sticky=W)
    ttk.OptionMenu(frame, textvariable, textvariable.get(), *options).grid(row=0, column=1)
    return frame


def number_row(parent, title, numbervariable, *, title_width=default_title_width):
    frame = ttk.Frame(parent)
    #ttk.Label(frame, text=title, width=title_width).grid(row=i, column=0, sticky=W)
    ttk.Entry(frame, numbervariable=numbervariable).grid(row=i, column=1)
    return frame