from tkinter import *
from tkinter import ttk


def start_stop_view(calculate_departures):
    root = Tk()
    TITLE = "Stop Viewer"
    root.title(TITLE)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    mainframe = ttk.Frame(root)
    mainframe.grid(row=0, column=0, sticky='nsew')

    search_container = ttk.Label(mainframe)
    search_container.grid(row=0, column=0, sticky=EW)
    gui_search_string = StringVar()
    ttk.Label(search_container, text="Hållplats:").grid(row=0, column=0)
    ttk.Entry(search_container, textvariable=gui_search_string).grid(row=0, column=1)

    gui_stop_name = StringVar()
    stop_name = ttk.Label(mainframe, textvariable=gui_stop_name)
    stop_name.grid(row=1, column=0, sticky=EW)

    # todo Listbox
    search_results = ttk.Frame(mainframe)
    search_results.grid(row=2, column=0, sticky=EW)

    def search(search_string, stop_name_string_var):
        departures = []
        try:
            departures = calculate_departures(search_string)
            stop_name_string_var.set(departures[0]["StopAreaName"])
        except IndexError:
            pass

        for slave in search_results.grid_slaves():
            slave.destroy()
        departures = departures[:20]
        for i, departure in enumerate(departures):
            ttk.Label(search_results, text=departure["DisplayTime"]).grid(row=i, column=0, sticky=EW)
            ttk.Label(search_results, text=departure["LineNumber"]).grid(row=i, column=1, sticky=EW)
            ttk.Label(search_results, text=departure["Destination"]).grid(row=i, column=2, sticky=EW)
            ttk.Label(search_results, text=departure["GroupOfLine"]).grid(row=i, column=3, sticky=EW)

    root.bind("<Return>", lambda *args: search(gui_search_string.get(), gui_stop_name))

    root.mainloop()
