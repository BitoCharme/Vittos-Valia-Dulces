import tkinter as tk
from constantes import style

class Creation(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background= "white")
        self.controller = controller
        self.nombre = tk.StringVar()
        self.categorias = tk.StringVar()
        self.marca = tk.StringVar()
        self.energia_total = 0
        self.energia_100 = tk.StringVar()
        self.peso = tk.StringVar()
        self.porciones = tk.StringVar()
        self.porcion = tk.StringVar()
        self.entries = [self.nombre, self.categorias, self.marca, self.energia_100, self.peso, self.porciones, self.porcion]
        self.entries2 = [self.nombre, self.categorias, self.marca, self.energia_100, self.peso, self.porciones, self.porcion]
        self.entries3 = [self.nombre, self.porcion, self.porciones]
        self.barra_label = None
        self.barra = tk.StringVar()
        self.modo = 0
        self.init_widgets()

    def init_widgets(self):
        self.volver_boton = tk.Button(
            self,
            text= "Volver al inicio",
            command= self.move_to_home,
            **style.STYLEBUTTON,
            relief= tk.FLAT,            
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        )
        self.volver_boton.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

        self.normal_frame = tk.Frame(self, bg=style.BACKGROUND)
        self.normal_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=22, pady=11)

        tk.Button(
            self.normal_frame,
            text= "Golosina individual",
            command= self.dulce_normal,
            **style.STYLEBUTTON,
            relief= tk.FLAT,            
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        ).pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        self.normal_label = tk.Label(
            self.normal_frame,
            text="Seleccione esta opción\npara crear golosinas únicas\nque no contienen más\ngolosinas en su paquete",
            justify=tk.CENTER,
            **style.STYLELABEL
        )
        self.normal_label.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)


        self.mixta_frame = tk.Frame(self, bg=style.BACKGROUND)
        self.mixta_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=22, pady=11)

        tk.Button(
            self.mixta_frame,
            text= "Golosina mixta",
            command= self.dulce_mixto,
            **style.STYLEBUTTON,
            relief= tk.FLAT,            
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        ).pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        self.mixta_label = tk.Label(
            self.mixta_frame,
            text="Seleccione esta opción\npara crear dulces que tienen\ngolosinas distintas\ndentro de su paquete",
            justify=tk.CENTER,
            **style.STYLELABEL
        )
        self.mixta_label.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)


        self.multiple_frame = tk.Frame(self, bg=style.BACKGROUND)
        self.multiple_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=22, pady=11)

        tk.Button(
            self.multiple_frame,
            text= "Golosina múltiple",
            command= self.dulce_multiple,
            **style.STYLEBUTTON,
            relief= tk.FLAT,
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        ).pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=10
        )

        self.multiple_label = tk.Label(
            self.multiple_frame,
            text="Seleccione esta opción para\ncrear golosinas que tienen\nsolo golosinas iguales\ndentro de su paquete.\nPara crear este tipo\nde golosina, tienes que\nhaber creado anteriormente\nla golosina individual que\nestá contenida en este paquete",
            justify=tk.CENTER,
            **style.STYLELABEL
        )
        self.multiple_label.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)
        
    def move_to_home(self):
        self.controller.show_frame(self.controller.home)
        self.barra.set("")

    def dulce_normal(self):
        self.modo = 1
        self.volver_boton.destroy()
        for widget in self.normal_frame.winfo_children():
            widget.destroy()
        self.normal_frame.destroy()
        self.normal_frame = None 
        for widget in self.multiple_frame.winfo_children():
            widget.destroy()
        self.multiple_frame.destroy()
        self.multiple_frame = None 
        for widget in self.mixta_frame.winfo_children():
            widget.destroy()
        self.mixta_frame.destroy()
        self.mixta_frame = None

        self.crear_boton = tk.Button(
            self,
            text= "Crear",
            command= self.crear,
            **style.STYLEBUTTON,
            relief= tk.FLAT,
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        )
        self.crear_boton.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

        self.cambiar_boton = tk.Button(
            self,
            text= "Cambiar tipo de golosina",
            command= self.destroy_normal,
            **style.STYLEBUTTON,
            relief= tk.FLAT,            
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        )
        self.cambiar_boton.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

        self.volver2_boton = tk.Button(
            self,
            text= "Volver al inicio",
            command= self.move_to_home,
            **style.STYLEBUTTON,
            relief= tk.FLAT,            
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        )
        self.volver2_boton.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

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

        # Frame para las etiquetas
        self.label_frame = tk.Frame(self, bg=style.BACKGROUND2)
        self.label_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

        # Frame para las barras de string
        self.entry_frame = tk.Frame(self, bg=style.BACKGROUND2)
        self.entry_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Frame para las etiquetas explicativas
        self.clarification_frame = tk.Frame(self, bg=style.BACKGROUND2)
        self.clarification_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

        # Frame para las etiquetas ejemplificativas
        self.example_frame = tk.Frame(self, bg=style.BACKGROUND2)
        self.example_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

        # Crear etiquetas
        labels = ["Nombre", "Categorías", "Marca", " Energía (100 g) ", "Peso (g)", "Porciones", "Porción"]
        tk.Label(
            self.label_frame,
            text="Datos",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
        for label_text in labels:
            tk.Label(
                self.label_frame,
                text=label_text,
                font=("Light Calibri", 18),
                **style.STYLECALCULUS,
                justify="center"
            ).pack(
                fill=tk.X,
                expand=True,
                padx=10,
                pady=3
            )

        #Crear entries
        tk.Label(
            self.entry_frame,
            text="Ingresa aquí los datos",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
        for textvariables in self.entries:
            tk.Entry(
                self.entry_frame,
                width=10,
                **style.STYLECALCULUS,
                font=("Light Calibri", 19),
                justify="center",
                textvariable=textvariables
            ).pack(
                fill=tk.X,
                expand=True,
                padx=10,
                pady=3
            )

        #Crear aclaraciones
        aclaraciones = ["Nombre del dulce, sin tildes", "Separadas por comas", "Identificación comercial", "Kilocalorías en 100 gramos", "Peso total en gramos", " Cantidades de porciones indicadas en el envase ", "¿Qué es una porción de este dulce?"]
        tk.Label(
            self.clarification_frame,
            text="Aclaraciones",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
        for texto in aclaraciones:
            tk.Label(
                self.clarification_frame,
                text=texto,
                font=("Light Calibri", 12),
                **style.STYLECALCULUS,
                justify="center"
            ).pack(
                expand=True,
                fill=tk.X,
                padx=10,
                pady=5
            )

        #Crear ejemplos
        ejemplos = ["Kegol Sabores Surtidos Acidos 200 g", " Navideno,Acido ", "Buono Cuore", "375", "80", "4", "1 Unidad (20 g)"]
        tk.Label(
            self.example_frame,
            text="Ejemplos",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
        for texto in ejemplos:
            tk.Label(
                self.example_frame,
                text=texto,
                font=("Light Calibri", 12),
                **style.STYLECALCULUS,
                justify="center"
            ).pack(
                expand=True,
                fill=tk.X,
                padx=10,
                pady=5
            )

    def dulce_mixto(self):
        self.modo = 2
        self.volver_boton.destroy()
        for widget in self.normal_frame.winfo_children():
            widget.destroy()
        self.normal_frame.destroy()
        self.normal_frame = None 
        for widget in self.multiple_frame.winfo_children():
            widget.destroy()
        self.multiple_frame.destroy()
        self.multiple_frame = None 
        for widget in self.mixta_frame.winfo_children():
            widget.destroy()
        self.mixta_frame.destroy()
        self.mixta_frame = None

        self.crear_boton = tk.Button(
            self,
            text= "Crear",
            command= self.crear,
            **style.STYLEBUTTON,
            relief= tk.FLAT,
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        )
        self.crear_boton.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

        self.cambiar_boton = tk.Button(
            self,
            text= "Cambiar tipo de golosina",
            command= self.destroy_normal,
            **style.STYLEBUTTON,
            relief= tk.FLAT,            
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        )
        self.cambiar_boton.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

        self.volver2_boton = tk.Button(
            self,
            text= "Volver al inicio",
            command= self.move_to_home,
            **style.STYLEBUTTON,
            relief= tk.FLAT,            
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        )
        self.volver2_boton.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

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

        # Frame para las etiquetas
        self.label_frame = tk.Frame(self, bg=style.BACKGROUND2)
        self.label_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

        # Frame para las barras de string
        self.entry_frame = tk.Frame(self, bg=style.BACKGROUND2)
        self.entry_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Frame para las etiquetas explicativas
        self.clarification_frame = tk.Frame(self, bg=style.BACKGROUND2)
        self.clarification_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

        # Frame para las etiquetas ejemplificativas
        self.example_frame = tk.Frame(self, bg=style.BACKGROUND2)
        self.example_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

        # Crear etiquetas
        labels = ["Nombre", "Categorías", "Marca", " Energía (100 g) ", "Peso (g)", "Porciones", "Porción"]
        tk.Label(
            self.label_frame,
            text="Datos",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
        for label_text in labels:
            tk.Label(
                self.label_frame,
                text=label_text,
                font=("Light Calibri", 18),
                **style.STYLECALCULUS,
                justify="center"
            ).pack(
                fill=tk.X,
                expand=True,
                padx=10,
                pady=3
            )

        #Crear entries
        tk.Label(
            self.entry_frame,
            text="Ingresa aquí los datos",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
        for textvariables in self.entries2:
            tk.Entry(
                self.entry_frame,
                width=10,
                **style.STYLECALCULUS,
                font=("Light Calibri", 19),
                justify="center",
                textvariable=textvariables
            ).pack(
                fill=tk.X,
                expand=True,
                padx=10,
                pady=3
            )

        #Crear aclaraciones
        aclaraciones = ["Nombre del dulce, sin tildes", "Separadas por comas", "Identificación comercial", "Kilocalorías en 100 gramos", "Peso total en gramos", " Cantidades de porciones indicadas en el envase ", "¿Qué es una porción de este dulce?"]
        tk.Label(
            self.clarification_frame,
            text="Aclaraciones",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
        for texto in aclaraciones:
            tk.Label(
                self.clarification_frame,
                text=texto,
                font=("Light Calibri", 12),
                **style.STYLECALCULUS,
                justify="center"
            ).pack(
                expand=True,
                fill=tk.X,
                padx=10,
                pady=5
            )

        #Crear ejemplos
        ejemplos = ["Kegol Sabores Surtidos Acidos 200 g", " Navideno,Acido ", "Buono Cuore", "375", "80", "4", "1 Unidad (20 g)"]
        tk.Label(
            self.example_frame,
            text="Ejemplos",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
        for texto in ejemplos:
            tk.Label(
                self.example_frame,
                text=texto,
                font=("Light Calibri", 12),
                **style.STYLECALCULUS,
                justify="center"
            ).pack(
                expand=True,
                fill=tk.X,
                padx=10,
                pady=5
            )

    def dulce_multiple(self):
        self.modo = 3
        self.volver_boton.destroy()
        for widget in self.normal_frame.winfo_children():
            widget.destroy()
        self.normal_frame.destroy()
        self.normal_frame = None 
        for widget in self.multiple_frame.winfo_children():
            widget.destroy()
        self.multiple_frame.destroy()
        self.multiple_frame = None 
        for widget in self.mixta_frame.winfo_children():
            widget.destroy()
        self.mixta_frame.destroy()
        self.mixta_frame = None

        self.crear_boton = tk.Button(
            self,
            text= "Crear",
            command= self.crear,
            **style.STYLEBUTTON,
            relief= tk.FLAT,
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        )
        self.crear_boton.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

        self.cambiar_boton = tk.Button(
            self,
            text= "Cambiar tipo de golosina",
            command= self.destroy_normal,
            **style.STYLEBUTTON,
            relief= tk.FLAT,            
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        )
        self.cambiar_boton.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

        self.volver2_boton = tk.Button(
            self,
            text= "Volver al inicio",
            command= self.move_to_home,
            **style.STYLEBUTTON,
            relief= tk.FLAT,            
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        )
        self.volver2_boton.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=11
        )

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

        # Frame para las etiquetas
        self.label_frame = tk.Frame(self, bg=style.BACKGROUND2)
        self.label_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

        # Frame para las barras de string
        self.entry_frame = tk.Frame(self, bg=style.BACKGROUND2)
        self.entry_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Frame para las etiquetas explicativas
        self.clarification_frame = tk.Frame(self, bg=style.BACKGROUND2)
        self.clarification_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

        # Frame para las etiquetas ejemplificativas
        self.example_frame = tk.Frame(self, bg=style.BACKGROUND2)
        self.example_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

        # Crear etiquetas
        labels = ["Nombre", "Porción", "Porciones"]
        tk.Label(
            self.label_frame,
            text="Datos",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
        for label_text in labels:
            tk.Label(
                self.label_frame,
                text=label_text,
                font=("Light Calibri", 18),
                **style.STYLECALCULUS,
                justify="center"
            ).pack(
                fill=tk.X,
                expand=True,
                padx=10,
                pady=3
            )

        #Crear entries
        tk.Label(
            self.entry_frame,
            text="Ingresa aquí los datos",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
        for textvariables in self.entries3:
            tk.Entry(
                self.entry_frame,
                width=10,
                **style.STYLECALCULUS,
                font=("Light Calibri", 19),
                justify="center",
                textvariable=textvariables
            ).pack(
                fill=tk.X,
                expand=True,
                padx=10,
                pady=3
            )

        #Crear aclaraciones
        aclaraciones = ["Nombre de la golosina, sin tildes", " Escribe la golosina que contiene este paquete ", "¿Cuántas golosinas lleva el paquete?"]
        tk.Label(
            self.clarification_frame,
            text="Aclaraciones",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
        for texto in aclaraciones:
            tk.Label(
                self.clarification_frame,
                text=texto,
                font=("Light Calibri", 12),
                **style.STYLECALCULUS,
                justify="center"
            ).pack(
                expand=True,
                fill=tk.X,
                padx=10,
                pady=5
            )

        #Crear ejemplos
        ejemplos = ["Chocman Black Caja 32x33 g", " Chocman Black 33 g ", "32"]
        tk.Label(
            self.example_frame,
            text="Ejemplos",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
        for texto in ejemplos:
            tk.Label(
                self.example_frame,
                text=texto,
                font=("Light Calibri", 12),
                **style.STYLECALCULUS,
                justify="center"
            ).pack(
                expand=True,
                fill=tk.X,
                padx=10,
                pady=5
            )


    def crear(self):
        if self.modo == 1:
            try:
                self.energia_total = round(float(self.energia_100.get())/100*float(self.peso.get()), 2)
                archivo = open("candy data/" + self.nombre.get() + ".txt","w+")
                nueva_linea = str(self.categorias.get()) + "\n" + str(self.marca.get()) + "\n" + str(self.energia_total) + " kcal" + "\n" + str(self.energia_100.get()) + " kcal" + "\n" + str(self.peso.get()) + " g" + "\n" + str(self.porciones.get()) + "\n" + str(self.porcion.get())
                archivo.write(nueva_linea)
                archivo.close()
                archivo = open("candy calculation/" + self.nombre.get() + ".txt","w+")
                archivo.close()
                archivo = open("Dulces.txt","a")
                archivo.write("\n" + str(self.nombre.get()))
                self.barra.set("Dulce añadido. Agrega la imagen manualmente")
                for var in self.entries:
                    var.set("")
            except Exception as e:
                self.barra_label.config(fg="white")
                self.barra.set('Hubo algún error con los datos proporcionados')
        elif self.modo == 2:
            pass
        elif self.modo == 3:
            try:
                archivo_path = "candy data/" + str(self.porcion.get()) + ".txt"
                archivo = open(archivo_path,"r")
                categorias = archivo.readline().rstrip().split(",")
                marca = archivo.readline().rstrip()
                energía_individual= archivo.readline().rstrip()
                energia_100 = archivo.readline().rstrip()
                peso = archivo.readline().rstrip()
                archivo.close()

                archivo = open("candy data/@" + self.nombre.get() + ".txt","w+")
                porciones = str(self.porciones.get())
                energía_individual = str(energía_individual).split()[0]
                peso = str(peso).split()[0]
                energía_total = round(float(energía_individual)*float(porciones),2)
                peso_total = round(float(peso)*float(porciones),2)
                if peso_total.is_integer():
                    peso_total = int(peso_total)
                if energía_total.is_integer():
                    energía_total = int(energía_total)
                categorias = "Golosina multiple," + str(categorias).translate(str.maketrans("", "", "'[]")).replace(", ", ",")
                nueva_linea = str(categorias) + "\n" + str(marca) + "\n" + str(energía_total) + " kcal" + "\n" + str(energia_100) + "\n" + str(peso_total) + " g" + "\n" + str(self.porciones.get()) + "\n" + str(self.porcion.get())
                archivo.write(nueva_linea)
                archivo.close()
                archivo = open("candy calculation/@" + self.nombre.get() + ".txt","w+")
                archivo.close()
                archivo = open("Dulces.txt","a")
                archivo.write("\n" + str("@" + self.nombre.get()))
                self.barra.set("Golosina múltiple añadida. Agrega la imagen manualmente")
                for var in self.entries3:
                    var.set("")
            except Exception as e:
                self.barra_label.config(fg="white")
                self.barra.set('Hubo algún error con los datos proporcionados')
        
    def destroy_normal(self):
        if self.cambiar_boton:
            self.cambiar_boton.destroy()
        if self.crear_boton:
            self.crear_boton.destroy()
        if self.volver2_boton:
            self.volver2_boton.destroy()
        if self.barra_label:
            self.barra_label.destroy()
        for widget in self.label_frame.winfo_children():
            widget.destroy()
        if self.label_frame:
            self.label_frame.destroy()
            self.label_frame = None 
        for widget in self.clarification_frame.winfo_children():
            widget.destroy()
        if self.clarification_frame:
            self.clarification_frame.destroy()
            self.clarification_frame = None 
        for widget in self.entry_frame.winfo_children():
            widget.destroy()
        if self.entry_frame:
            self.entry_frame.destroy()
            self.entry_frame = None 
        for widget in self.example_frame.winfo_children():
            widget.destroy()
        if self.example_frame:
            self.example_frame.destroy()
            self.example_frame = None
        self.init_widgets()