#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tkinter as tk
import os
import json
import datetime as dt
from datetime import datetime
from tkinter import ttk

def limpiar_frame(frame):
    return frame.winfo_children().clear()

def my_list(path: str):

    with open(path, encoding="utf-8") as file:
        my_record = json.load(file)
    return my_record

def actualizar_proximo_capitulo():
    my_path = os.path.join("ddbb", "animes.json")

    hoy = datetime.today()

    with open(my_path, encoding="utf-8") as file:
        my_record = json.load(file)
        for record in my_record:
            if record.get("Estado") == "En emisión":
                fpc = record.get("Proximo") #fpc: fecha del próximo cápitulo
                fecha_proximo_capitulo = datetime.strptime(fpc, "%Y-%m-%d")
                proximo_capitulo = record.get("Capitulos")
                if hoy > fecha_proximo_capitulo:
                    fecha_proximo_capitulo += dt.timedelta(weeks=1)
                    proximo_capitulo += 1
                    record[6] = fecha_proximo_capitulo
                    record[3] = proximo_capitulo
                    print(fecha_proximo_capitulo)
                    print(proximo_capitulo)
    

def en_emision(frame):
    limpiar_frame(frame=frame)
    frame_en_emision = ttk.Frame(frame)
    frame_en_emision.pack(side=tk.TOP)

    my_anime_path = os.path.join("ddbb", "animes.json")
    
    
    pos_x = 4
    hoy = str(datetime.now().date())
    #Zona de título de la tabla
    tk.Label(frame_en_emision, text="ID", font=("", 10, "bold")).grid(column=0, row=2)
    tk.Label(frame_en_emision, text="Nombre", font=("", 10, "bold")).grid(column=1, row=2, columnspan=2)
    tk.Label(frame_en_emision, text="Temporada", font=("", 10, "bold")).grid(column=3, row=2)
    tk.Label(frame_en_emision, text="Capítulo", font=("", 10, "bold")).grid(column=4, row=2)
    tk.Label(frame_en_emision, text="Estado", font=("", 10, "bold")).grid(column=5, row=2)
    tk.Label(frame_en_emision, text="Fecha próximo capítulo", font=("", 10, "bold")).grid(column=6, row=2)

    for data in my_list(my_anime_path):
        if data.get("Estado") == "En emisión":
            tk.Label(frame_en_emision, text=data.get("ID")).grid(column=0, row=pos_x)
            tk.Label(frame_en_emision, text=data.get("Nombre")).grid(column=1, row=pos_x, columnspan=2)
            tk.Label(frame_en_emision, text=data.get("Temporada")).grid(column=3, row=pos_x)
            tk.Label(frame_en_emision, text=data.get("Capítulos")).grid(column=4, row=pos_x)
            tk.Label(frame_en_emision, text=data.get("Estado")).grid(column=5, row=pos_x)
            if data.get("Fecha_próximo_capítulo") == hoy:
                tk.Label(frame_en_emision, text=data.get("Fecha_próximo_capítulo"), bg="cyan").grid(column=6, row=pos_x)
            else:
                tk.Label(frame_en_emision, text=data.get("Fecha_próximo_capítulo")).grid(column=6, row=pos_x)

        pos_x += 1

def finalizado(frame):
    my_anime_path = os.path.join("ddbb", "animes.json")
    frame_finalizado = ttk.Frame(master=frame)
    frame_finalizado.pack(side=tk.TOP)
    
    pos_x = 4

    #Zona de título de la tabla
    tk.Label(frame_finalizado, text="ID", font=("", 10, "bold")).grid(column=0, row=2)
    tk.Label(frame_finalizado, text="Nombre", font=("", 10, "bold")).grid(column=1, row=2)
    tk.Label(frame_finalizado, text="Temporada", font=("", 10, "bold")).grid(column=2, row=2)
    tk.Label(frame_finalizado, text="Cápitulo", font=("", 10, "bold")).grid(column=3, row=2)
    tk.Label(frame_finalizado, text="Estado", font=("", 10, "bold")).grid(column=4, row=2)
    tk.Label(frame_finalizado, text="Emitido", font=("", 10, "bold")).grid(column=5, row=2)
    ttk.Label(frame_finalizado, text="Último cápitulo", font=("", 10, "bold")).grid(column=6, row=2)

    for data in my_list(my_anime_path):
        if data.get("Estado") == "Finalizado":
            tk.Label(frame_finalizado, text=data.get("ID")).grid(column=0, row=pos_x)
            tk.Label(frame_finalizado, text=data.get("Nombre")).grid(column=1, row=pos_x)
            tk.Label(frame_finalizado, text=data.get("Temporada")).grid(column=2, row=pos_x)
            tk.Label(frame_finalizado, text=data.get("Capítulos")).grid(column=3, row=pos_x)
            tk.Label(frame_finalizado, text=data.get("Estado")).grid(column=4, row=pos_x)
            tk.Label(frame_finalizado, text=data.get("Emitido")).grid(column=5, row=pos_x)
            ttk.Label(frame_finalizado, text=data.get("Ultimo")).grid(column=6, row=pos_x)

        pos_x += 1

def todos(frame):
    my_anime_path = os.path.join("ddbb", "animes.json")
    frame_todos = ttk.Frame(master=frame)
    frame_todos.pack(side=tk.TOP)

    pos_x = 4
    hoy = str(datetime.now().date())
    #Zona de título de la tabla
    ttk.Labelframe(frame_todos, text="ID", style="").grid(column=0, row=2)
    #tk.Label(frame, text="ID", font=("", 10, "bold")).grid(column=0, row=2)
    tk.Label(frame_todos, text="Nombre", font=("", 10, "bold")).grid(column=1, row=2, columnspan=2)
    tk.Label(frame_todos, text="Temporada", font=("", 10, "bold")).grid(column=3, row=2)
    tk.Label(frame_todos, text="Cápitulo", font=("", 10, "bold")).grid(column=4, row=2)
    tk.Label(frame_todos, text="Estado", font=("", 10, "bold")).grid(column=5, row=2)
    tk.Label(frame_todos, text="Emitido", font=("", 10, "bold")).grid(column=6, row=2)
    tk.Label(frame_todos, text="Próximo", font=("", 10, "bold")).grid(column=7, row=2)

    for data in my_list(my_anime_path):

        tk.Label(frame_todos, text=data.get("ID")).grid(column=0, row=pos_x)
        tk.Label(frame_todos, text=data.get("Nombre")).grid(column=1, row=pos_x, columnspan=2)
        tk.Label(frame_todos, text=data.get("Temporada")).grid(column=3, row=pos_x)
        tk.Label(frame_todos, text=data.get("Capitulos")).grid(column=4, row=pos_x)
        tk.Label(frame_todos, text=data.get("Estado")).grid(column=5, row=pos_x)
        tk.Label(frame_todos, text=data.get("Emitido")).grid(column=6, row=pos_x)
        if data.get("Estado") == "En emisión" and data.get("Proximo") == hoy:
            tk.Label(frame_todos, text=data.get("Proximo"), bg="cyan").grid(column=7, row=pos_x)
        else:
            tk.Label(frame_todos, text=data.get("Proximo")).grid(column=7, row=pos_x)

        pos_x += 1

def myfunction(opt: tuple, box, pane):
    if opt[0] == box.get():
        en_emision(pane)
    elif opt[1] == box.get():
        finalizado(pane)
    elif opt[2] == box.get():
        todos(pane)

def cuarentena(frame):
    my_anime_path = os.path.join("ddbb", "animes.json")
    frame_cuarentena = ttk.Frame(frame)
    frame_cuarentena.pack()

    pos_x = 4

    #Zona de título de la tabla
    ttk.Labelframe(frame_cuarentena, text="ID", style="").grid(column=0, row=2)
    #tk.Label(frame, text="ID", font=("", 10, "bold")).grid(column=0, row=2)
    tk.Label(frame_cuarentena, text="Nombre", font=("", 10, "bold")).grid(column=1, row=2, columnspan=2)
    tk.Label(frame_cuarentena, text="Temporada", font=("", 10, "bold")).grid(column=3, row=2)
    tk.Label(frame_cuarentena, text="Cápitulo", font=("", 10, "bold")).grid(column=4, row=2)
    tk.Label(frame_cuarentena, text="Estado", font=("", 10, "bold")).grid(column=5, row=2)
    tk.Label(frame_cuarentena, text="Emitido", font=("", 10, "bold")).grid(column=6, row=2)
    tk.Label(frame_cuarentena, text="Próximo", font=("", 10, "bold")).grid(column=7, row=2)

    for data in my_list(my_anime_path):
        if data.get("Estado") == "Cuarentena":
            tk.Label(frame_cuarentena, text=data.get("ID")).grid(column=0, row=pos_x)
            tk.Label(frame_cuarentena, text=data.get("Nombre")).grid(column=1, row=pos_x, columnspan=2)
            tk.Label(frame_cuarentena, text=data.get("Temporada")).grid(column=3, row=pos_x)
            tk.Label(frame_cuarentena, text=data.get("Capitulos")).grid(column=4, row=pos_x)
            tk.Label(frame_cuarentena, text=data.get("Estado")).grid(column=5, row=pos_x)
            tk.Label(frame_cuarentena, text=data.get("Emitido")).grid(column=6, row=pos_x)
            tk.Label(frame_cuarentena, text=data.get("Proximo")).grid(column=7, row=pos_x)

        pos_x += 1

def my_frame():
    FRAME = tk.Tk()
    FRAME.geometry("900x500")
    FRAME.minsize(width=1024, height=400)
    FRAME.title("My anime list")

    menubar = ttk.Frame(FRAME)
    menubar.pack(side=tk.TOP)

    menu_frame = ttk.Frame(FRAME)
    menu_frame.pack(side=tk.LEFT)

    menu_frame.config(border=5)

    #my_options = ("En emisión", "Finalizado", "Todos")
    #my_combobox = ttk.Combobox(menubar, values=my_options, width=12, state="readonly")
    #my_combobox.current(0)
    #my_combobox.pack()

    #my_combobox.bind("<<ComboboxSelected>>", myfunction(my_options, my_combobox, main_frame))
    tk.Button(menu_frame, text="Todos", command=lambda:todos(FRAME)).pack(pady=10)
    tk.Button(menu_frame, text="En emisión", command=lambda:en_emision(FRAME)).pack(pady=10)
    tk.Button(menu_frame, text="Finalizado", command=lambda:finalizado(FRAME)).pack(pady=10)
    tk.Button(menu_frame, text="Cuarentena", command=lambda:cuarentena(FRAME)).pack(pady=10)

    en_emision(FRAME)
    
    FRAME.mainloop()

if __name__ == "__main__":
    #actualizar_proximo_capitulo()
    my_frame()
