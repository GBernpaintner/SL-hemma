from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from table import Table
from traffic_data_source import get_departures_from
from weather_data_source import get_forecast, WeatherInfo
from datetime import datetime


class Dashboard(App):
    def build(self):
        # Create time table
        def first(entry):
            return Label(text=entry['StopAreaName'])

        def second(entry):
            return Button(text=entry['TransportMode'], background_color=(200,1,1,1))

        def third(entry):
            return Label(text=entry['DisplayTime'])

        def fourth(entry):
            return Label(text=entry['Destination'])
        ems = [first, second, third, fourth]
        time_table = Table(source=lambda: get_departures_from([1525, 1500]), entry_maps=ems)
        time_table.update()
        Clock.schedule_interval(lambda dt: time_table.update(), 10)
        time_table.size_hint_x = None
        time_table.width = 600

        def wfirst(entry):
            code = entry["condition"]["code"]
            icon = [condition['icon'] for condition in WeatherInfo.conditions if condition['code'] == code][0]
            return Image(source=f'resources/weather_icons_64x64/day/{icon}.png')
        def wsecond(entry):
            time = datetime.fromisoformat(entry['time'])
            return Label(text=str(time.hour))
        ems = [wfirst,wsecond]
        weather_table = Table(source=lambda: get_forecast()[:24], entry_maps=ems)
        weather_table.update()
        weather_table.size_hint_x = None
        weather_table.width = 600

        layout = StackLayout(orientation='tb-lr')
        layout.add_widget(time_table)
        layout.add_widget(weather_table)

        return layout


if __name__ == '__main__':
    Dashboard().run()

