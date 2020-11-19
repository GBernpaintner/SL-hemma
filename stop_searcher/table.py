from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from stop_controller import get_departures_from
from kivy.clock import Clock


class Table(GridLayout):
    def __init__(self, **kwargs):
        self.source = kwargs.pop('source', None)
        self._entry_maps = kwargs.pop('entry_maps', None)
        super().__init__(**kwargs)


    def update(self):
        try:
            self._entries = self.source()
        except TypeError as e:
            self._entries = self.source
        self.cols = len(self._entry_maps)
        # Remove old children.
        self.clear_widgets()
        # Add new children.
        for entry in self._entries:
            for entry_map in self._entry_maps:
                self.add_widget(entry_map(entry))


    # This is a list containing the objects/things that are passed to
    # the entry_maps functions for populating the table.
    @property
    def entries(self):
        return self._entries


    @property
    def entry_maps(self):
        return self._entry_maps


    @entry_maps.setter
    def entry_maps(self, em):
        self._entry_maps = em
        self.cols = len(em)


class MainApp(App):
    def build(self):
        def first(entry):
            return Label(text=entry['StopAreaName'])
        def second(entry):
            return Button(text=entry['TransportMode'], background_color=(200,1,1,1))
        def third(entry):
            return Label(text=entry['DisplayTime'])
        ems = [first, second, third]
        t = Table(source=lambda: get_departures_from([1525, 1500]), entry_maps=ems)
        t.update()
        Clock.schedule_interval(lambda dt: t.update(), 10)
        return t


if __name__ == '__main__':
    MainApp().run()

