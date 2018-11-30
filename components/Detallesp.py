import tkinter as tk

from models.Proteina import Proteina
from helpers.helpers import resize
from helpers.colors import grisOscuro
class Detalles(tk.Frame):
    def __init__(self, root = None, objeto = Proteina()):
        super().__init__(root)

        self.label = tk.Label(self, text = 'Detalles')
        self.label.config(anchor = tk.CENTER, pady= 10, bg = 'gray', width = 45)
        self.label.pack(side = tk.TOP)
#################################################################################################
        self.body = tk.Frame(self)
        self.body.config(width = 248, height = 330)
        self.body.pack( side = tk.BOTTOM )
        
        """ FOTO DEL ANIMAL """
        #self.photo = tk.PhotoImage(file = objeto.urlImage)
        #self.photo = resize( self.photo, 80 , 80 )

        #self.labelPhoto = tk.Label(self.body, image = self.photo, bg = grisOscuro)
        #self.labelPhoto.place(x = 0 , y = 0)

        self.descripcion = tk.Text(self.body)
        self.descripcion.config(width =50, height = 10)
        self.descripcion.insert(tk.INSERT,objeto.descripcion)
        self.descripcion.place(x = 0, y = 50)
#################################################################################################
        self.button = tk.Button(self.body, text = 'Back')
        self.button.place(x = 100, y = 210)
        self.button.bind('<Button-1>', lambda e: root.handleBackDetalles(e))

    def setDescription(self,objeto = Proteina()):
        #print(objeto.urlImage)
        #self.photo = tk.PhotoImage(file = objeto.urlImage)
        #self.photo = resize( self.photo, 80 , 80 )
        #self.labelPhoto.config(image = self.photo)
        #self.labelPhoto.place(x = 80, y = 10 )
        self.descripcion.delete('1.0',tk.END)
        self.descripcion.insert(tk.INSERT,objeto.descripcion)