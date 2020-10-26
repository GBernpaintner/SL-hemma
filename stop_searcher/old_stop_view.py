from tkinter import *
from tkinter import ttk
from stop_model import get_stops_matching

root = Tk()
TITLE = "Stop Viewer"
root.title(TITLE)
mainframe = ttk.Frame(root)
mainframe.grid(row=0, column=0, sticky=NSEW)
search_results = ttk.Frame(mainframe)
search_results.grid(row=1, column=1, sticky=EW)

gui_search_string = StringVar()
ttk.Label(mainframe, text="Sök hållplatser:").grid(row=0, column=0)
search_entry = ttk.Entry(mainframe, textvariable=gui_search_string).grid(row=0, column=1)


'''def search(search_string):
    stops = get_stops_matching(SearchString=search_string)
    for slave in search_results.grid_slaves():
        slave.destroy()
    for i, stop in enumerate(stops):
        ttk.Label(search_results, text=stop["Name"]).grid(row=i, column=1, sticky=EW)


root.bind("<Return>", lambda *args: search(gui_search_string.get()))'''

root.mainloop()
