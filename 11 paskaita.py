from tkinter import *

langas = Tk()


def spausdinti(event):
    ivesta = laukas.get()
    rezultatas["text"] = 'Labas,', ivesta


meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", )
submeniu.add_command(label="Atkurti paskutinį")
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=langas.destroy)

uzrasas = Label(langas, text="Iveskite varda")
laukas = Entry(langas)
mygtukas1 = Button(langas, text="Patvirtinti")
langas.bind("<Return>", spausdinti)
rezultatas = Label(langas, text="")

uzrasas.grid(row=0, column=0)
laukas.grid(row=0, column=1)
mygtukas1.grid(row=0, column=2)
rezultatas.grid(row=1, columnspan=2)

langas.mainloop()
