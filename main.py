from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.properties import ObjectProperty


Builder.load_file('game.kv')

class modulinnhold(Bubble):
    #pass
    def __init__(self, **kwargs):
        super(modulinnhold, self).__init__(**kwargs)

    def remove_bubble(self):
        Bronter.remove_bubble(Bronter())

class menu(Bubble):
    #pass
    def __init__(self, **kwargs):
        super(menu, self).__init__(**kwargs)
        self.moduloversikt = ObjectProperty(None)
        #self.ids.moduloversikt.bind(on_release=self.show_bubble)

    def show_bubble(self, *l):
        Bronter().show_bubble()

class Bronter(FloatLayout):

    def __init__(self, **kwargs):
        super(Bronter, self).__init__(**kwargs)
        self.add_widget(menu())

    def show_bubble(self, *l):
        if not hasattr(self, 'bubb'):
            self.bubb = bubb = modulinnhold()
            self.add_widget(bubb)
        else:
            values = ('left_top')
            index = values

    def remove_bubble(self, *l):
        self.remove_widget(modulinnhold())

class BronterApp(App):
    def build(self):
        return Bronter()

if __name__=="__main__":
    BronterApp().run()
