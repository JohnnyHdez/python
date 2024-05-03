#-*- coding: utf-8 -*-

import datetime
from crud_animes import Crud
import sqlite3
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyList(Widget):
    def list(self):
        crud = Crud()
        pane = BoxLayout(orientation="vertical", padding=0.3)

        total = crud.total_animes()
        pane.add_widget(Label(text="Total: {}".format(total[0]), size_hint=(1, 0.1)))
        #pane.add_widget(top)
        COLUMNAS = 6
        lista = crud.mostrar()
        celdas = GridLayout(cols=COLUMNAS)

        hoy = datetime.datetime.now()
        hoy = hoy.date()
        hoy = datetime.datetime.strptime(str(hoy), "%Y-%m-%d")

        semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        #celdas.add_widget(Label(text="ID", size_hint=(0.1, 0.6)))
        #celdas.add_widget(Label(text="Nombre", size_hint=(0.7, 0.6)))
        #celdas.add_widget(Label(text="Temporada", size_hint=(0.1, 0.6)))
        #celdas.add_widget(Label(text="Capítulos", size_hint=(0.1, 0.6)))
        #celdas.add_widget(Label(text="Emitido", size_hint=(0.1, 0.6)))
        #celdas.add_widget(Label(text="Siguiente capítulo", size_hint=(0.15, 0.6)))
        

        for registro in lista:
            if registro[5] == "En emisión":
                estreno = datetime.datetime.strptime("{}".format(registro[8]), "%Y-%m-%d")
                dia = estreno.weekday()

                if hoy == estreno:
                    #Significa que hoy hay un nuevo capítulo
                    celdas.add_widget(Label(text="{}".format(registro[0]), size_hint=(0.1, 0.6), color=(0, 1, 1, 1), bold=True, italic=True))
                    celdas.add_widget(Label(text="{}".format(registro[1]), size_hint=(0.1, 0.6), color=(0, 1, 1, 1), bold=True, italic=True))
                    celdas.add_widget(Label(text="{}".format(registro[3]), size_hint=(0.1, 0.6), color=(0, 1, 1, 1), bold=True, italic=True))
                    celdas.add_widget(Label(text="{}".format(registro[4]), size_hint=(0.1, 0.6), color=(0, 1, 1, 1), bold=True, italic=True))
                    celdas.add_widget(Label(text="{}".format(registro[7]), size_hint=(0.1, 0.6), color=(0, 1, 1, 1), bold=True, italic=True))
                    celdas.add_widget(Label(text="{}, {}".format(registro[8], semana[dia]), size_hint=(0.15, 0.6), color=(0, 1, 1, 1), bold=True, italic=True))
                else:
                    celdas.add_widget(Label(text=str(registro[0]), size_hint=(0.1, 0.6)))
                    celdas.add_widget(Label(text=registro[1], size_hint=(0.1, 0.6)))
                    celdas.add_widget(Label(text=str(registro[3]), size_hint=(0.1, 0.6)))
                    celdas.add_widget(Label(text=str(registro[4]), size_hint=(0.1, 0.6)))
                    celdas.add_widget(Label(text=registro[7], size_hint=(0.1, 0.6)))
                    celdas.add_widget(Label(text="{}, {}".format(registro[8], semana[dia]), size_hint=(0.15, 0.6)))
    
    def myQuery(self):
        super(MyList, self).__init__()
        query = "SELECT id, name, season, chapters, year, next_chapter FROM emission WHERE state LIKE 'En emisión' ORDER BY last_chaptter, name"
        select = ObjectProperty(None)
        con = sqlite3.connect(os.path.join('ddbb', 'animes.db'))
        cur = con.cursor()
        cur.execute(query)

        

class lista_kivy(App):
    def build(self):
        crud = Crud()
        pane = BoxLayout(orientation="vertical", padding=0.3)
        top = GridLayout(cols=2)

        total = crud.total_animes()
        pane.add_widget(Label(text="Total: {}".format(total[0]), size_hint=(1, 0.1)))
        #pane.add_widget(top)
        COLUMNAS = 6
        lista = crud.mostrar()
        celdas = GridLayout(cols=COLUMNAS)

        hoy = datetime.datetime.now()
        hoy = hoy.date()
        hoy = datetime.datetime.strptime(str(hoy), "%Y-%m-%d")

        semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        celdas.add_widget(Label(text="ID", size_hint=(0.1, 0.6)))
        celdas.add_widget(Label(text="Nombre", size_hint=(0.7, 0.6)))
        celdas.add_widget(Label(text="Temporada", size_hint=(0.1, 0.6)))
        celdas.add_widget(Label(text="Capítulos", size_hint=(0.1, 0.6)))
        celdas.add_widget(Label(text="Emitido", size_hint=(0.1, 0.6)))
        celdas.add_widget(Label(text="Siguiente capítulo", size_hint=(0.15, 0.6)))
        

        for registro in lista:
            if registro[5] == "En emisión":
                estreno = datetime.datetime.strptime("{}".format(registro[8]), "%Y-%m-%d")
                dia = estreno.weekday()

                if hoy == estreno:
                    #Significa que hoy hay un nuevo capítulo
                    celdas.add_widget(Label(text="{}".format(registro[0]), size_hint=(0.1, 0.6), color=(0, 1, 1, 1), bold=True, italic=True))
                    celdas.add_widget(Label(text="{}".format(registro[1]), size_hint=(0.1, 0.6), color=(0, 1, 1, 1), bold=True, italic=True))
                    celdas.add_widget(Label(text="{}".format(registro[3]), size_hint=(0.1, 0.6), color=(0, 1, 1, 1), bold=True, italic=True))
                    celdas.add_widget(Label(text="{}".format(registro[4]), size_hint=(0.1, 0.6), color=(0, 1, 1, 1), bold=True, italic=True))
                    celdas.add_widget(Label(text="{}".format(registro[7]), size_hint=(0.1, 0.6), color=(0, 1, 1, 1), bold=True, italic=True))
                    celdas.add_widget(Label(text="{}, {}".format(registro[8], semana[dia]), size_hint=(0.15, 0.6), color=(0, 1, 1, 1), bold=True, italic=True))
                else:
                    celdas.add_widget(Label(text=str(registro[0]), size_hint=(0.1, 0.6)))
                    celdas.add_widget(Label(text=registro[1], size_hint=(0.1, 0.6)))
                    celdas.add_widget(Label(text=str(registro[3]), size_hint=(0.1, 0.6)))
                    celdas.add_widget(Label(text=str(registro[4]), size_hint=(0.1, 0.6)))
                    celdas.add_widget(Label(text=registro[7], size_hint=(0.1, 0.6)))
                    celdas.add_widget(Label(text="{}, {}".format(registro[8], semana[dia]), size_hint=(0.15, 0.6)))


        pane.add_widget(celdas)

        #pane.add_widget(saludo)

        return pane

if __name__ == "__main__":
    crud = Crud()
    crud.actualizar()

    lista_kivy().run()
