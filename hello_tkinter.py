import tkinter as tk

root = tk.Tk()

root.title('Hello from tkinter')
root.geometry('400x300')
hello = tk.Label(root, text='Hello from tkinter')
hello.grid(row=1, column=1)

root.mainloop()