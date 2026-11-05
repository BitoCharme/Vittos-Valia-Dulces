import tkinter as tk
from constantes import style
from PIL import ImageTk,Image
import PIL

class Formula(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background= style.COMPONENT)
        self.controller = controller
        self.init_widgets()

    def init_widgets(self):
        tk.Button(
            self,
            text= "Volver a la comparación",
            command= self.move_to_comparison,
            **style.STYLEBUTTON,
            relief= tk.FLAT,            
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

        tk.Button(
            self,
            text= "Siguiente",
            command= self.move_to_parametros,
            **style.STYLEBUTTON,
            relief= tk.FLAT,            
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

        imagen_formula = Image.open("imagenes/" + "formula parametros.png")        
        width, height = imagen_formula.size #Reajustar tamaño
        aspect_ratio = 1300 / width
        new_width = int(width * aspect_ratio)
        new_height = int(height * aspect_ratio)
        resized_image1 = imagen_formula.resize((new_width, new_height), PIL.Image.Resampling.LANCZOS)

        imagen1 = ImageTk.PhotoImage(resized_image1)
        label1 = tk.Label(self, image=imagen1)
        label1.image = imagen1
        label1.pack(
            side=tk.TOP,
            padx=10,
            pady=11
        )

        tk.Label(
            self,
            text= 'Esta es la fórmula. Cada parámetro se multiplica por su variable, a excepción del precio y gramaje, que usan el mismo parámetro elevado\npara que cambien de manera más rápida, y de esa forma lograr contrastarse mejor entre dulces al variar los parámetros. La fórmula\nestá hecha para que los parámetros sean porcentajes de cada variable. Sin mostrar los parámetros se ve así:',
            justify= tk.CENTER,
            **style.STYLELABEL
        ).pack(
            side= tk.TOP,
            fill= tk.X,
            #expand= True,
            pady= 7
        )

        imagen_formula2 = Image.open("imagenes/formula.png")       
        width, height = imagen_formula2.size #Reajustar tamaño
        aspect_ratio = 900 / width
        new_width = int(width * aspect_ratio)
        new_height = int(height * aspect_ratio)
        resized_image2 = imagen_formula2.resize((new_width, new_height), PIL.Image.Resampling.LANCZOS)

        imagen2 = ImageTk.PhotoImage(resized_image2)
        label2 = tk.Label(self, image=imagen2)
        label2.image = imagen2
        label2.pack(
            side=tk.TOP,
            padx=10,
            pady=11
        )

        tk.Label(
            self, 
            text= 'El adicional se suma directamente y la duración se multiplica por el sabor dividido por la mitad del gramaje.\nEsto porque mientras más sabroso el dulce, más vale lo que dura, y para remediar la elevada duración de los dulces con más cantidad, es\nnecesario incluir el gramaje. El resto de variables se suman, luego multiplican por los gramos del paquete y se dividen por el precio.',
            justify= tk.CENTER,
            **style.STYLELABEL
        ).pack(
            side= tk.TOP,
            fill= tk.X,
            #expand= True,
            pady= 7
        )

        tk.Label(
            self,
            text= 'Cambiar los parámetros sirve para determinar la relevancia que tiene cada variable. Para mantener el orden y poder compararse con\nlos valores de otros usuarios, los parámetros de sabor, duración, capacidad de jugueteo y salud deben sumar 100.',
            justify= tk.CENTER,
            **style.STYLELABEL
        ).pack(
            side= tk.TOP,
            fill= tk.X,
            #expand= True,
            pady= 7
        )

    def move_to_comparison(self):
        self.controller.show_frame(self.controller.comparison)

    def move_to_parametros(self):
        self.controller.show_frame(self.controller.parametros)
