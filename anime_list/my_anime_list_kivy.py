import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
import json
import os

class DemoApp(App):
    def animes(self):
        my_path = os.path.join("ddbb", "animes.json")
        self.pane = GridLayout()
        #self.pane.size_hint=(1, 0.5)

        with open(my_path, encoding="utf-8") as file:
            record = json.load(file)

        self.pane.cols = 6
        self.pane.rows = len(record)

        MY_FONT_COLOR = "#00C000"

        self.pane.add_widget(Label(text="ID", bold=True, color=MY_FONT_COLOR))
        self.pane.add_widget(Label(text="Nombre", bold=True, color=MY_FONT_COLOR))
        self.pane.add_widget(Label(text="Emitido", bold=True, color=MY_FONT_COLOR))
        self.pane.add_widget(Label(text="Temp", bold=True, color=MY_FONT_COLOR))
        self.pane.add_widget(Label(text="Cáp", bold=True, color=MY_FONT_COLOR))
        self.pane.add_widget(Label(text="próximo cápitulo", bold=True, color=MY_FONT_COLOR))
        for animes in record:
            nombre = Label(text=animes.get("Nombre"), color=MY_FONT_COLOR)
            codigo = Label(text=str(animes.get("ID")), color=MY_FONT_COLOR)
            emitido = Label(text=animes.get("Emitido"), color=MY_FONT_COLOR)
            temporada = Label(text=str(animes.get("Temporada")), color=MY_FONT_COLOR)
            capitulo = Label(text=str(animes.get("Capítulos")), color=MY_FONT_COLOR)
            fecha_proximo_capitulo = Label(text=animes.get("Fecha_próximo_capítulo"), color=MY_FONT_COLOR)

            if animes.get("Estado") == "En emisión":
                #self.pane.add_widget(my_button)
                self.pane.add_widget(codigo)
                self.pane.add_widget(nombre)
                self.pane.add_widget(emitido)
                self.pane.add_widget(temporada)
                self.pane.add_widget(capitulo)
                self.pane.add_widget(fecha_proximo_capitulo)

        return self.pane
    
    def build(self):

        return self.animes()

if __name__ == "__main__":
    DemoApp().run()
