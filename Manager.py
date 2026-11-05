import tkinter as tk
from constantes import style
from screens.Home import Home
from screens.Comparison import Comparison
from screens.Multiple import Multiple
from screens.Mix import Mix
from screens.Candy import Candy
from screens.Creation import Creation
from screens.Calculation import Calculation
from screens.Eating import Eating
from screens.Parametros import Parametros
from screens.Formula import Formula

class Manager(tk.Tk):

     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.title("Vitto's Valía de Dulces")
          icono = tk.PhotoImage(file="imagenes/Vitto's Valía de Dulces.png")
          icono_chico = tk.PhotoImage(file="imagenes/Vitto's Valía de Dulces pequeño.png")
          self.iconphoto(False, icono, icono_chico)
          container = tk.Frame(self)
          self.cual = "Tubos Geles Dulces Sabor Frutilla"
          self.home = Home
          self.comparison = Comparison
          self.multiple = Multiple
          self.mix = Mix
          self.candy = Candy
          self.eating = Eating
          self.parametros = Parametros
          self.formula = Formula
          self.creation = Creation
          self.calculation = Calculation

          # Configurar el evento de tecla F11 para salir de pantalla completa
          self.bind("<F11>", self.toggle_fullscreen)
          self.bind("<Escape>", self.quit_fullscreen)

          container.pack(
               side = tk.TOP,
               fill = tk.BOTH,
               expand = True 
          )
          container.configure(background= style.BACKGROUND)
          container.grid_columnconfigure(0, weight=1) #Estamos haciendo que tenga una columna y fila, el peso es el tamaño con respecto a las demás
          container.grid_rowconfigure(0, weight=1)

          self.frames = {}

          # Crear instancia de Home y pasarla a otras clases
          home_frame = Home(container, self)
          self.frames[Home] = home_frame
          home_frame.grid(row=0, column=0, sticky=tk.NSEW)

          # Crear instancia de Comparison y pasarla a otras clases
          self.comparison_frame = Comparison(container, self)
          self.frames[Comparison] = self.comparison_frame
          self.comparison_frame.grid(row=0, column=0, sticky=tk.NSEW)

          # Crear instancia de Candy y pasar la instancia de Home y comparison
          self.candy_frame = Candy(container, self, home_frame, self.comparison_frame)
          self.frames[Candy] = self.candy_frame
          self.candy_frame.grid(row=0, column=0, sticky=tk.NSEW)

          # Crear instancia de Multiple y pasar la instancia de Home y comparison
          self.multiple_frame = Multiple(container, self, home_frame, self.comparison_frame)
          self.frames[Multiple] = self.multiple_frame
          self.multiple_frame.grid(row=0, column=0, sticky=tk.NSEW)

          # Crear instancia de Mix y pasar la instancia de Home y comparison
          self.mix_frame = Mix(container, self, home_frame, self.comparison_frame)
          self.frames[Mix] = self.mix_frame
          self.mix_frame.grid(row=0, column=0, sticky=tk.NSEW)


          # Crear instancia de Calculation y pasar la instancia de Home y comparison
          self.calculation_frame = Calculation(container, self, home_frame, self.comparison_frame)
          self.frames[Calculation] = self.calculation_frame
          self.calculation_frame.grid(row=0, column=0, sticky=tk.NSEW)

          # Crear instancia de Eating y pasar la instancia de Home
          self.eating_frame = Eating(container, self, home_frame)
          self.frames[Eating] = self.eating_frame
          self.eating_frame.grid(row=0, column=0, sticky=tk.NSEW)

          # Crear instancia de Parámetros y pasar la instancia de Home
          self.parametros_frame = Parametros(container, self, self.comparison_frame)
          self.frames[Parametros] = self.parametros_frame
          self.parametros_frame.grid(row=0, column=0, sticky=tk.NSEW)
          
          # Crear instancia de Formula y pasar la instancia de Home
          self.formula_frame = Formula(container, self)
          self.frames[Formula] = self.formula_frame
          self.formula_frame.grid(row=0, column=0, sticky=tk.NSEW)

          for F in {Creation}:
               frame = F(container, self)
               self.frames[F] = frame
               frame.grid(row = 0, column = 0, sticky = tk.NSEW)
               
          self.show_frame(Home)

     def show_frame(self, container):
          frame = self.frames[container]
          frame.tkraise() #Lo pasa por delante de todo

     def toggle_fullscreen(self, event=None):
        self.attributes("-fullscreen", not self.attributes("-fullscreen"))

     def quit_fullscreen(self, event=None):
        self.attributes("-fullscreen", False)