#!/usr/bin/env python

import sqlite3
import tkinter as tk

def insert_query(arg1: str, arg2: str, arg3: str, arg4: int):
    con = sqlite3.connect("./ddbb/animes.db")
    cur = con.cursor()
    my_list = (arg1, arg2, arg3, arg4)
    #query = "insert into emission (name, author, genrer, year) values(?, ?, ?, ?)"
    #cur.executemany(query, my_list)
    query1 = "insert into emission (name, author, genrer, year) values ('arg1', 'arg2', 'arg3', 'arg4')"
    cur.execute(query1)
    con.commit()

def select_records():
    con = sqlite3.connect("./ddbb/animes.db")
    cur = con.cursor()
    query = "select name, author, genrer, year from emission order by name asc"
    cur.execute(query)

def frame():
    root = tk.Tk()
    root.geometry("300x200")
    root.title("My anime list")

    records = tk.Frame()

    #Variables required
    name = tk.StringVar()
    author = tk.StringVar()
    genrer = tk.StringVar()
    year = tk.IntVar()

    #Widgets required
    label1 = tk.Label(root, text="My anime list")
    label2 = tk.Label(root, text="Name")
    label3 = tk.Label(root, text="Author")
    label4 = tk.Label(root, text="Genrer")
    label5 = tk.Label(root, text="Year")

    entry1 = tk.Entry(root, textvariable=name)
    entry2 = tk.Entry(root, textvariable=author)
    entry3 = tk.Entry(root, textvariable=genrer)
    entry4 = tk.Entry(root, textvariable=year)

    list_name = name.get().lower()
    list_author = author.get().lower()
    list_genrer = genrer.get().lower()
    list_year = year.get()

    button1 = tk.Button(root, text="Insert", command=lambda:insert_query(list_name, list_author, list_genrer, list_year))
    button2 = tk.Button(root, text="Show records", command=lambda:select_records())

    #positioning the widgets in a gridlayout
    label1.grid(row=1, column=1, columnspan=2, pady=2)
    label2.grid(row=2, column=1, pady=2)
    label3.grid(row=3, column=1, pady=2)
    label4.grid(row=4, column=1, pady=2)
    label5.grid(row=5, column=1, pady=2)

    entry1.grid(row=2, column=2, pady=2, padx=2)
    entry2.grid(row=3, column=2, pady=2, padx=2)
    entry3.grid(row=4, column=2, pady=2, padx=2)
    entry4.grid(row=5, column=2, pady=2, padx=2)

    button1.grid(row=6, column=1, columnspan=2, pady=2)
    button2.grid(row=6, column=3, columnspan=2, pady=2)

    #Anime records
    label6 = tk.Label(records, text="Amnime records")

    label6.grid(row=1, column=1, columnspan=2)

    root.mainloop()

frame()

if "__name__" == "__main__":
    frame()
    