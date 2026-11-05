import tkinter as tk
from constantes import style
import time
from PIL import ImageTk,Image
import PIL

class Eating(tk.Frame):

    def __init__(self, parent, controller, home_instance):
        super().__init__(parent)
        self.configure(background="pink")
        self.home_instance = home_instance
        self.controller = controller
        self.inicio = None
        self.comenzar = None
        self.tiempo = 0
        self.barra = tk.StringVar()
        self.porciones = tk.StringVar()
        self.nombre = ""
        self.porciones = 0
        self.porciones_label = None
        self.porcion = ""
        self.porcion_label = None
        self.nombre_label = None
        self.left_frame = None
        self.dulce_image = None
        self.imagen = None
        self.porciones_frame = None
        self.init_widgets()

    def init_widgets(self):
        self.barra_label = tk.Label(
            self,
            textvariable=self.barra,
            font=("Light Calibri", 40),
            fg="white",
            bg="black",
            justify="center"
        )
        self.barra_label.pack(
            fill=tk.X,
            side=tk.TOP
        )
    
        self.left_frame = tk.Frame(self, bg=style.BACKGROUND)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.comenzar = tk.Button(
            self.left_frame,
            text= "Comenzar cronómetro",
            command= self.partir,
            **style.STYLEBUTTON,
            relief= tk.FLAT,
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        )
        self.comenzar.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

        tk.Button(
            self.left_frame,
            text= "Volver",
            command= self.move_to_candy,
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

    def create_new_widgets (self, nombre, porciones, porcion):
        self.nombre = nombre
        self.porciones = porciones
        self.porcion = porcion

        if self.porciones_label:
            self.porciones_label.destroy()

        if self.porcion_label:
            self.porcion_label.destroy()
        
        if self.nombre_label:
            self.nombre_label.destroy()

        if self.imagen:
            self.imagen.destroy()

        if self.porciones_frame:
            self.porciones_frame.destroy()

        self.nombre_label = tk.Label(
            self.left_frame,
            text=self.nombre,
            **style.STYLELABEL3,
            justify="center"
        )

        self.nombre_label.pack(
            fill=tk.X,
            side=tk.TOP,
            pady=10
        )

        self.porciones_frame = tk.Frame(self.left_frame, bg=style.BACKGROUND)
        self.porciones_frame.pack(side=tk.TOP, fill=tk.X)

        self.porciones_label = tk.Label(
            self.porciones_frame,
            text=" Porciones: " + str(self.porciones) + " ",
            **style.STYLELABEL3,
            justify="center"
        )

        self.porciones_label.pack(
            side=tk.LEFT,
            padx=10,
            pady=10,
            expand=True
        )

        self.porcion_label = tk.Label(
            self.porciones_frame,
            text=" Porción: " + str(self.porcion) + " ",
            **style.STYLELABEL3,
            justify="center"
        )

        self.porcion_label.pack(
            side=tk.LEFT,
            padx=10,
            pady=10,
            expand=True
        )
        try:
            original_image = Image.open("imagenes/" + str(self.nombre) + ".png")
            
            # Ajusta el tamaño de la imagen automáticamente
            width, height = original_image.size
            aspect_ratio = 560/height
            new_width = int(width * aspect_ratio)
            new_height = int(height * aspect_ratio)
            resized_image = original_image.resize((new_width, new_height), PIL.Image.Resampling.LANCZOS)

            self.dulce_image = ImageTk.PhotoImage(resized_image)

            self.imagen = tk.Label(self, image=self.dulce_image)

            self.imagen.pack(
                side=tk.RIGHT,
                padx=10,
                pady=11
            )

        except:
            self.none_label = tk.Label(
                self,
                text=f"No se ha encontrado una vista previa del dulce\n  {self.nombre}. Para\n  "
                    f"añadir su imagen, agrega una imagen .PNG en esta carpeta\n  y ponle el mismo EXACTO nombre que le pusiste al dulce\n"
                    f"Si es una golosina múltiple, nombra a la imagen con una @\nantes del nombre. Si es mixta, nómbrala con % antes del nombre.\nEjemplo: @Kegol Sabores Surtidos Caja",                    
                justify=tk.CENTER
            )
            self.none_label.pack(side=tk.LEFT, padx=20, pady=10, expand=True)


    def partir(self):
        if self.inicio == None:
            self.inicio = time.time()
            self.comenzar.configure(text="Detener cronómetro")
            self.actualizar_tiempo()
        else:
            self.tiempo = time.time() - self.inicio
            self.barra.set(str(round(self.tiempo, 2)) + " segundos")
            self.comenzar.configure(text="Iniciar cronómetro")
            self.inicio = None

    def actualizar_tiempo(self):
        if self.inicio is not None:
            self.tiempo = time.time() - self.inicio
            self.barra.set(str(round(self.tiempo, 2)) + " segundos")
        self.after(100, self.actualizar_tiempo)  # Actualiza cada 100 milisegundos

    def move_to_candy(self):
        self.controller.show_frame(self.controller.candy)