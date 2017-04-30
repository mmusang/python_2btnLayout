from kivy.app import App
#kivy.require("1.9.0")
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.clock import Clock

class MainScreen(Screen):
    pass

class AnotherScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class ClockWgt(Widget):
    def __init__(self, **kwargs):
        super(ClockWgt, self).__init__(**kwargs)
        Clock.schedule_interval(self.update,1/60.)

    def update(self, *args):
        pass

presentation = Builder.load_file("main.kv") 
#class mainlayout(Widget):
#    pass

class main(App):
    def build(self):
        return presentation

if __name__ == "__main__":
    main().run()
#add something
            

