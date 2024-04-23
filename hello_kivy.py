from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        return Button(text='Hello World from kivy')

if __name__ == '__main__':
    MyApp().run()
