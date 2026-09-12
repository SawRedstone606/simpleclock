from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime


class TimeApp(App):
    def build(self):
        self.time_label = Label(
            text="",
            font_size=48
        )

        Clock.schedule_interval(self.update_time, 1)
        self.update_time(0)

        return self.time_label

    def update_time(self, dt):
        now = datetime.now()
        self.time_label.text = now.strftime("%H:%M:%S")


TimeApp().run()
