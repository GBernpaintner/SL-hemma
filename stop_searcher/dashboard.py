from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from table import Table
from stop_controller import get_departures_from


class Dashboard(App):
    def build(self):
        # Create time table
        def first(entry):
            return Label(text=entry['StopAreaName'])
        def second(entry):
            return Button(text=entry['TransportMode'], background_color=(200,1,1,1))
        def third(entry):
            return Label(text=entry['DisplayTime'])
        ems = [first, second, third]
        time_table = Table(source=lambda: get_departures_from([1525, 1500]), entry_maps=ems)
        time_table.update()
        Clock.schedule_interval(lambda dt: time_table.update(), 10)

        button1 = Button(text='I am a button', background_color=(1,50,91,1), size_hint=(None, 0.15), width=300)
        button2 = Button(text='I am a button', background_color=(91,130,91,1), size_hint=(None, 0.15), width=300)
        button3 = Button(text='I am a button', background_color=(1,100,51,1), size_hint=(None, 0.15), width=300)
        button4 = Button(text='I am a button', background_color=(1,190,1,1), size_hint=(None, 0.15), width=300)
        
        time_table.size_hint_x = None
        time_table.width = 600
        layout = StackLayout(orientation='tb-lr')
        layout.add_widget(time_table)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)

        return layout


if __name__ == '__main__':
    Dashboard().run()

