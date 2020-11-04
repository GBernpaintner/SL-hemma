from tkinter import *
from tkinter import ttk
from datetime import datetime
from math import floor

# TODO debug
from pprint import pprint


def calulate_remaining_time(time_string):
    date = datetime.fromisoformat(time_string)
    now = datetime.today()
    delta = date - now
    minutes = delta.seconds // 60 if delta.days >= 0 else 0
    return f'{minutes} min' if minutes > 0 else 'Nu'


def generate_departures_row(parent, departure, row):
    TABLE_COLUMN_PADDING = 16
    TABLE_ROW_PADDING = 4
    stop = ttk.Label(parent, text=departure['StopAreaName'])
    stop.grid(row=row, column=0, padx=(0, TABLE_COLUMN_PADDING), pady=(0, TABLE_ROW_PADDING), sticky=EW)
    time_remaining = calulate_remaining_time(departure['ExpectedDateTime'])
    time = ttk.Label(parent, text=time_remaining)
    time.grid(row=row, column=1, padx=(0, TABLE_COLUMN_PADDING), pady=(0, TABLE_ROW_PADDING), sticky=EW)
    line = departure['GroupOfLine'] 
    if departure['TransportMode'] == 'BUS':
        line = f'Buss {departure["LineNumber"]}' 
    line_name = ttk.Label(parent, text=line)
    line_name.grid(row=row, column=2, padx=(0, TABLE_COLUMN_PADDING), pady=(0, TABLE_ROW_PADDING), sticky=EW)
    ttk.Label(parent, text=departure["Destination"]).grid(row=row, column=3, sticky=EW)


def generate_departures_table(parent, departures):
    for row, departure in enumerate(departures):
        generate_departures_row(parent, departure, row)


def start_stop_view(get_departures_from_SiteIds):
    root = Tk()
    TITLE = "Stop Viewer"
    root.title(TITLE)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    mainframe = ttk.Frame(root)
    mainframe.grid(row=0, column=0, sticky='nsew')

    title = ttk.Label(mainframe, text='Avgångar')
    title.grid(row=1, column=0, sticky=EW)

    search_results = ttk.Frame(mainframe)
    search_results.grid(row=2, column=0, sticky=EW)

    def search():
        departures = []
        # liljeholmen: 9294
        # Valla Torg:  1525
        # Årsta Torg:  1500
        departures = get_departures_from_SiteIds([1525, 1500])

        for slave in search_results.grid_slaves():
            slave.destroy()
        departures = departures[:20]
        generate_departures_table(search_results, departures)

        # TODO debug
        try:
            pprint(departures[-1])
        except:
            print('no departures')

    root.bind("<Return>", lambda *args: search())
    search()

    root.mainloop()
