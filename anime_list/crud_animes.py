import sqlite3
import os
import datetime

import ttkbootstrap as ttk

from tkinter import messagebox
try:
    import Tkinter as tk
except ImportError: 
    import tkinter as tk

class Crud:
    def __init__(self) -> None:

        my_path = os.path.join("ddbb", "animes.db")
        try:
         self.con = sqlite3.connect(my_path)
         self.mostrar()
        except:
            messagebox.showerror(title="Error de conección con la base de datos", message="Error al conectar con la base de datos animes.db")
        

    def conexion(consulta):
        def registros(*args):
            my_path = os.path.join("ddbb", "animes.db")
            try:
                con = sqlite3.connect(my_path)
                datos = consulta(con)
            
                return datos
            
            except:
                messagebox.showerror(title="Error de conección con la base de datos", message="Error al conectar con la base de datos animes.db")
            finally:
                con.close()

        return registros


    def actualizar(self):
        query = "select id, chapters, state, next_chapter from emission"
        cur = self.con.cursor()
        records = cur.execute(query)

        hoy = datetime.datetime.now()
        hoy = datetime.datetime.strptime(str(hoy.date()), "%Y-%m-%d")

        for row in records:
            if row[2] == "En emisión":
                capitulo_pasado = str(row[3])

                id = int(row[0])
                capitulos = int(row[1])
                pasado = datetime.datetime.strptime(capitulo_pasado, "%Y-%m-%d")

                if hoy > pasado:
                    capitulos += 1
                    estreno = pasado + datetime.timedelta(weeks=1)
                    estreno = datetime.datetime.strftime(estreno, "%Y-%m-%d")

                    cur.execute("update emission set next_chapter='{}', chapters={} where id={}".format(estreno, capitulos, id))
                    # Once the query ends the changes are saved
                    self.con.commit()

    
    def mostrar(self):
        my_query = "select id, name, author, season, chapters, state, genrer, year, next_chapter, last_chapter\
        from emission where state like 'En emisión' order by next_chapter, name"
        cur = self.con.cursor()
        records = cur.execute(my_query)
        
        return records
    
    def agregar_registro(self, new_id: int, nombre: str, temporada: int, capitulos: int, estado: str, estreno: str, siguiente_capitulo: str):

        query = "insert into emission(id, name, season, chapters, state, year, next_chapter) values ({}, '{}', {}, {}, '{}', '{}', '{}')".format(new_id, nombre, temporada, capitulos, estado, estreno, siguiente_capitulo)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        messagebox.showinfo(title="Nuevo registro", message="Se ha agregado un nuevo registro a la base de datos")

    def total_animes(self):
        cur = self.con.cursor()
        total = cur.execute("select count(id) from emission where state='En emisión'")
        for dato in total:
            animes = dato
        return animes
    
    def total_vistos_2023(self):
        cursor = self.con.cursor()
        query = cursor.execute("SELECT COUNT(id) FROM emission WHERE last_chapter like '2023%' and state like 'Finalizado'")
        for data in query:
            total = data
        return total
    
    def animes_2023(self):
        cur = self.con.cursor()
        total = cur.execute("select id, name, season, chapters, year, last_chapter from emission where state='Finalizado' and last_chapter like '2023%' order by last_chapter, name")
        return total

    def animes_2024(self):
        cur = self.con.cursor()
        total = cur.execute("select id, name, season, chapters, year, last_chapter from emission where state='Finalizado' and last_chapter like '2024%' order by last_chapter, name")
        return total
    
    def total_vistos_2024(self):
        cursor = self.con.cursor()
        query = cursor.execute("SELECT COUNT(id) FROM emission WHERE last_chapter like '2024%' and state like 'Finalizado'")
        for data in query:
            total = data
        return total


class Ventana:
    def __init__(self) -> None:

        marco = ttk.Window(themename="cyborg")
        marco.geometry("1000x350")
        marco.title("Mi lista de animes")
        marco.minsize(width=600, height=200)

        self.mode_state = tk.IntVar()

        #Scrollbars
        canvas = tk.Canvas(master=marco)
        self.panel = ttk.Frame(master=canvas)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=10)
        scrollv = tk.Scrollbar(master=marco, orient=tk.VERTICAL, command=canvas.yview)
        scrollv.pack(side=tk.RIGHT, fill=tk.Y)

        self.formulario()
        
        canvas.create_window(0, 0, anchor=tk.NW, window=self.panel)
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox(tk.ALL),yscrollcommand=scrollv.set)
        
        marco.mainloop()
        crud = Crud()
        crud.con.close()
    
    def nuevo_registro(self):
        marco = tk.Toplevel()
        marco.geometry("1000x220")
        marco.minsize(width=900, height=200)
        marco.title("Nuevo Registro")

        panel = ttk.Frame(master=marco)

        panel.pack()

        arial_10_bold = "Arial 10 bold"

        id = ttk.Label(master=panel, text="ID",font=(arial_10_bold))
        name = ttk.Label(master=panel, text="Nombre",font=(arial_10_bold))
        season = ttk.Label(master=panel, text="Temporada",font=(arial_10_bold))
        chapters = ttk.Label(master=panel, text="Capítulos",font=(arial_10_bold))
        state = ttk.Label(master=panel, text="Estado",font=(arial_10_bold))
        year = ttk.Label(master=panel, text="Emitido",font=(arial_10_bold))
        next_chapter = ttk.Label(master=panel, text="Siguiente capítulo",font=(arial_10_bold))

        #Positioning the labels
        id.grid(row=1, column=1)
        name.grid(row=1, column=2)
        season.grid(row=1, column=3)
        chapters.grid(row=1, column=4)
        state.grid(row=1, column=5)
        year.grid(row=1, column=6)
        next_chapter.grid(row=1, column=7)

        #Defining variables
        new_id = tk.IntVar(value=0)
        nombre = tk.StringVar(value="")
        capitulos = tk.IntVar(value=0)
        temporada = tk.IntVar(value=0)
        estreno = tk.StringVar(value="")
        siguiente_capitulo = tk.StringVar(value="")
        estado = tk.StringVar(value="En emisión")

        #Definineg text elements
        id_txt = ttk.Entry(master=panel, textvariable=new_id)
        name_txt = ttk.Entry(master=panel, textvariable=nombre)
        season_txt = ttk.Entry(master=panel, textvariable=temporada)
        chapters_txt = ttk.Entry(master=panel, textvariable=capitulos)
        state_txt = ttk.Entry(master=panel, textvariable=estado)
        year_txt = ttk.Entry(master=panel, textvariable=estreno)
        next_chapter_txt = ttk.Entry(master=panel, textvariable=siguiente_capitulo)

        #Positioning the entrance widgets
        id_txt.grid(row=3, column=1)
        name_txt.grid(row=3, column=2)
        season_txt.grid(row=3, column=3)
        chapters_txt.grid(row=3, column=4)
        state_txt.grid(row=3, column=5)
        year_txt.grid(row=3, column=6)
        next_chapter_txt.grid(row=3, column=7)

        #Validate button
        agregar_btn = ttk.Button(master=panel, text="Agregar")
        agregar_btn.grid(row=5, column=1, columnspan=2)
        agregar_btn.config(command=lambda:crud.agregar_registro(new_id=new_id.get(), nombre=nombre.get(), temporada=temporada.get(), capitulos=capitulos.get(), estado=estado.get(), estreno=estreno.get(), siguiente_capitulo=siguiente_capitulo.get()))

        marco.mainloop()


    #Positioning with grid function
    def animes_vistos_2023(self):
        marco = tk.Toplevel()
        marco.geometry("1000x400")
        marco.minsize(width=900, height=300)
        marco.title("Animes vistos en 2023")
        
        canvas = tk.Canvas(master=marco)
        
        panel = ttk.Frame(master=canvas)
        #Scrollbars
        scroll_y = tk.Scrollbar(master=marco, orient=tk.VERTICAL, command=canvas.yview)
        scroll_x = tk.Scrollbar(master=marco, orient=tk.HORIZONTAL, command=canvas.xview)

        crud = Crud()
        
        result = crud.animes_2023()

        
        arial_12_bold = "Arial 12 normal"
        arial_14_bold = "Arial 14 bold"

        id_label = ttk.Label(master=panel, text="Id", font=(arial_14_bold))
        name_label = ttk.Label(master=panel, text="Nombre", font=(arial_14_bold))
        season_label = ttk.Label(master=panel, text="Temporadas", font=(arial_14_bold))
        chapters_label = ttk.Label(master=panel, text="Capítulos", font=(arial_14_bold))
        emited_label = ttk.Label(master=panel, text="Emitido", font=(arial_14_bold))
        last_chapter_label = ttk.Label(master=panel, text="Último capítulo", font=(arial_14_bold))
        total_animes_2023_label = ttk.Label(master=panel, text="Total: {}".format(crud.total_vistos_2023()[0]), font=(arial_14_bold))
        
        id_label.grid(row=1, column=1)
        name_label.grid(row=1, column=2)
        season_label.grid(row=1, column=3)
        chapters_label.grid(row=1, column=4)
        emited_label.grid(row=1, column=5)
        last_chapter_label.grid(row=1, column=6)
        total_animes_2023_label.grid(row=1, column=7)
        
        my_row = 2

        for data in result:
            ttk.Label(master=panel, text=data[0], font=(arial_12_bold)).grid(row=my_row, column=1)
            ttk.Label(master=panel, text=data[1], font=(arial_12_bold)).grid(row=my_row, column=2)
            ttk.Label(master=panel, text=data[2], font=(arial_12_bold)).grid(row=my_row, column=3)
            ttk.Label(master=panel, text=data[3], font=(arial_12_bold)).grid(row=my_row, column=4)
            ttk.Label(master=panel, text=data[4], font=(arial_12_bold)).grid(row=my_row, column=5)
            ttk.Label(master=panel, text=data[5], font=(arial_12_bold)).grid(row=my_row, column=6)

            my_row = my_row + 1
        
        canvas.create_window(0, 0, anchor=tk.NW, window=panel)
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox(tk.ALL), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        canvas.place(relx=0.01, rely=0.05, relwidth=0.9, relheight=0.85)
        scroll_y.place(relx=0.97, rely=0.05, relheight=0.85)
        scroll_x.place(relx=0.01, rely=0.95, relwidth=0.9)
        

    
    def animes_vistos_2024(self):
        marco = tk.Toplevel()
        marco.geometry("1100x400")
        marco.minsize(width=900, height=300)
        marco.title("Animes vistos en 2024")
        
        canvas = tk.Canvas(master=marco)
        
        panel = ttk.Frame(master=canvas)
        #Scrollbars
        scroll_y = tk.Scrollbar(master=marco, orient=tk.VERTICAL, command=canvas.yview)
        scroll_x = tk.Scrollbar(master=marco, orient=tk.HORIZONTAL, command=canvas.xview)

        crud = Crud()
        
        result = crud.animes_2024()

        
        arial_12_bold = "Arial 12 normal"
        arial_14_bold = "Arial 14 bold"

        id_label = ttk.Label(master=panel, text="Id", font=(arial_14_bold))
        name_label = ttk.Label(master=panel, text="Nombre", font=(arial_14_bold))
        season_label = ttk.Label(master=panel, text="Temporadas", font=(arial_14_bold))
        chapters_label = ttk.Label(master=panel, text="Capítulos", font=(arial_14_bold))
        emited_label = ttk.Label(master=panel, text="Emitido", font=(arial_14_bold))
        last_chapter_label = ttk.Label(master=panel, text="Último capítulo", font=(arial_14_bold))
        total_animes_2023_label = ttk.Label(master=panel, text="Total: {}".format(crud.total_vistos_2024()[0]), font=(arial_14_bold))
        
        id_label.grid(row=1, column=1)
        name_label.grid(row=1, column=2)
        season_label.grid(row=1, column=3)
        chapters_label.grid(row=1, column=4)
        emited_label.grid(row=1, column=5)
        last_chapter_label.grid(row=1, column=6)
        total_animes_2023_label.grid(row=1, column=7)
        
        my_row = 2

        for data in result:
            ttk.Label(master=panel, text=data[0], font=(arial_12_bold)).grid(row=my_row, column=1)
            ttk.Label(master=panel, text=data[1], font=(arial_12_bold)).grid(row=my_row, column=2)
            ttk.Label(master=panel, text=data[2], font=(arial_12_bold)).grid(row=my_row, column=3)
            ttk.Label(master=panel, text=data[3], font=(arial_12_bold)).grid(row=my_row, column=4)
            ttk.Label(master=panel, text=data[4], font=(arial_12_bold)).grid(row=my_row, column=5)
            ttk.Label(master=panel, text=data[5], font=(arial_12_bold)).grid(row=my_row, column=6)

            my_row = my_row + 1
        
        canvas.create_window(0, 0, anchor=tk.NW, window=panel)
        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox(tk.ALL), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        canvas.place(relx=0.01, rely=0.05, relwidth=0.9, relheight=0.85)
        scroll_y.place(relx=0.97, rely=0.05, relheight=0.85)
        scroll_x.place(relx=0.01, rely=0.95, relwidth=0.9)

   
    
    def formulario(self):

        crud = Crud()

        #An add button
        one_plus = ttk.Button(master=self.panel, text="+")
        one_plus.grid(row=1, column=12, columnspan=2, ipadx=1, ipady=0)
        one_plus.config(command=self.nuevo_registro)

        #Animes seen in 2024        
        animes_seen = ttk.Button(master=self.panel, text="Animes vistos en 2024", bootstyle=ttk.SUCCESS)
        animes_seen.grid(row=1, column=14, ipadx=2)
        animes_seen.config(command=self.animes_vistos_2024)


        #Cantidad de animes que veo en emisión
        mi_total = crud.total_animes()

        arial_10_bold = "Arial 10 bold"
        ttk.Label(master=self.panel, text="Animes total = {}".format(mi_total[0]), font=(arial_10_bold)).grid(row=1, column=1)

        '''These are the names of the labels for the Formular'''
        id = ttk.Label(master=self.panel, text="ID",font=(arial_10_bold))
        name = ttk.Label(master=self.panel, text="Nombre",font=(arial_10_bold))
        season = ttk.Label(master=self.panel, text="Temporada",font=(arial_10_bold))
        chapters = ttk.Label(master=self.panel, text="Capítulos",font=(arial_10_bold))
        year = ttk.Label(master=self.panel, text="Emitido",font=(arial_10_bold))
        next_chapter = ttk.Label(master=self.panel, text="Siguiente capítulo",font=(arial_10_bold))

        '''Positioning the Labels elements in the formular'''
        id.grid(row=3, column=0)
        name.grid(row=3, column=1, columnspan=3)
        season.grid(row=3, column=5)
        chapters.grid(row=3, column=6)
        year.grid(row=3, column=9)
        next_chapter.grid(row=3, column=10)

        '''Positioning the Labels elements in the formular'''
        fields = crud.mostrar()
        pos_x = 5
        hoy = str(datetime.datetime.now().date())

        dia_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        
        for field in fields:
            

            if field[5] == "En emisión" or field[5] == "Próximo":
                n_ch_ls = list(str(field[8]).split("-"))

                anho = int(n_ch_ls[0])
                mes = int(n_ch_ls[1])
                dias = int(n_ch_ls[2])

                fecha_actual = datetime.date(anho, mes, dias)
                semana = fecha_actual.weekday()

                
                if hoy == str(field[8]):
                    ttk.Label(master=self.panel, text=str(field[0]), bootstyle=ttk.INFO).grid(row=pos_x, column=0)
                    ttk.Label(master=self.panel, text=str(field[1]), bootstyle=ttk.INFO).grid(row=pos_x, column=1)
                    ttk.Label(master=self.panel, text=str(field[3]), bootstyle=ttk.INFO).grid(row=pos_x, column=5)
                    ttk.Label(master=self.panel, text=str(field[4]), bootstyle=ttk.INFO).grid(row=pos_x, column=6)
                    ttk.Label(master=self.panel, text=str(field[7]), bootstyle=ttk.INFO).grid(row=pos_x, column=9)
                    ttk.Label(master=self.panel, text="{}, {}".format(str(field[8]), dia_semana[semana]), bootstyle=ttk.INFO).grid(row=pos_x, column=10)
                else:
                    ttk.Label(master=self.panel, text=str(field[0])).grid(row=pos_x, column=0)
                    ttk.Label(master=self.panel, text=str(field[1])).grid(row=pos_x, column=1)
                    ttk.Label(master=self.panel, text=str(field[3])).grid(row=pos_x, column=5)
                    ttk.Label(master=self.panel, text=str(field[4])).grid(row=pos_x, column=6)
                    ttk.Label(master=self.panel, text=str(field[7])).grid(row=pos_x, column=9)
                    ttk.Label(master=self.panel, text="{}, {}".format(str(field[8]), dia_semana[semana])).grid(row=pos_x, column=10)

            pos_x += 1
    
   

if __name__ == "__main__":
    crud = Crud()
    crud.actualizar()
    
    ventana = Ventana()

