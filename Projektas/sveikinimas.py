from tkinter import *

pagrindinis = Tk()
uzrasas = Label(pagrindinis, width=40, height=10, text="Sveikas, pasauli!")
pagrindinis.title("Mano programa")
pagrindinis.iconbitmap(r'sveikinimasis.ico')
uzrasas.pack()
pagrindinis.mainloop()
