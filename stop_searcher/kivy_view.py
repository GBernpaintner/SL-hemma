from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class Table(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._entries = kwargs.get('entries', None)
        self._entry_map = kwargs.get('entry_map', None)


    @property
    def entries(self):
        return self._entries


    @entries.setter
    def entries(self, e):
        self._entries = e
        for entry in e:
            for col in range(self.cols):
                self.add_widget(self._entry_map[col](entry))


    @entry_map.setter
    def entry_map(self, em):
        self._entry_map = em
        self.cols = len(em)


class MainApp(App):
    def build(self):
        t = Table()
        return Table()


if __name__ == '__main__':
    MainApp().run()

