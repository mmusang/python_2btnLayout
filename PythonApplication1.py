from kivy.app import App
#kivy.require("1.9.0")
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class mainlayout(Widget):
    pass

class SimpleKivy4(App):
    def build(self):
        return mainlayout()

if __name__ == "__main__":
    SimpleKivy4().run()
#add something
            

