import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
pane = tk.Frame(master=root)
pane.pack()

img = ImageTk.PhotoImage(image=Image.open("./img/logo_muestra.png"))
lbl = tk.Label(master=pane, image=img)
lbl.grid(row=1, column=2)

img_1 = Image.open("./img/3785.jpg")
img_1 = img_1.resize((170, 256))
img_logo_1 = ImageTk.PhotoImage(image=img_1)
lbl_1 = tk.Label(master=pane, image=img_logo_1)
lbl_1.grid(column=1, row=1)

img_2 = Image.open("./img/Signo_mas.jpg")
img_2 = img_2.resize((32,32))
#tk.Label(master=pane, image=ImageTk.PhotoImage(image=img_2)).grid(row=1, column=3)
tk.Button(master=pane, image=ImageTk.PhotoImage(image=img_1)).grid(row=2, column=1)

root.mainloop()