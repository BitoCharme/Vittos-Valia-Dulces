import tkinter as tk
from constantes import style, config
from PIL import ImageTk,Image
import PIL
import os
from screens.Comparison import Comparison

class Calculation(tk.Frame):

    def __init__(self, parent, controller, home_instance, comparison_instance):
        super().__init__(parent)
        self.configure(background="pink")
        self.controller = controller
        self.home_instance = home_instance
        self.comparison_instance = comparison_instance
        self.sabor = tk.StringVar()
        self.duracion = tk.StringVar()
        self.jugueteo = tk.StringVar()
        self.salud = tk.StringVar()
        self.precio = tk.StringVar()
        self.peso = 0
        self.tienda = tk.StringVar() #Aún no cambiamos nada
        self.adicional = tk.StringVar()
        self.calculo = 0
        self.barra = tk.StringVar()
        self.fecha = tk.StringVar()
        self.nombre = ""
        self.nueva_linea = ""
        self.salud_o_no = True
        self.imagen = None
        self.left_frame = None
        self.barra_label = None
        self.x = 0
        self.entries = [self.sabor, self.duracion, self.jugueteo, self.salud, self.precio, self.tienda, self.adicional, self.fecha]
        self.comentarios = tk.StringVar()
        self.parametros = self.controller.comparison.obtener_variable(self.controller.comparison_frame)
        self.porcion = ""
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

    def create_new_widgets(self, new_value, peso):

        if self.left_frame:
            for widget in self.left_frame.winfo_children():
                widget.destroy()
        if self.imagen:
            self.imagen.destroy()
        
        self.configure(background= "pink")
        self.nombre = new_value
        numero = peso.split(" ")
        self.peso = float(numero[0])

        # Frame para que la imagen quede al lado
        if self.left_frame == None:
            self.left_frame = tk.Frame(self, bg=style.BACKGROUND)
            self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Button(
            self.left_frame,
            text= "Calcular",
            command= self.Calculo,
            **style.STYLEBUTTON,
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
            relief= tk.FLAT,
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=8
        )

        tk.Button(
            self.left_frame,
            text= "Registrar datos",
            command= self.Registro,
            **style.STYLEBUTTON,
            relief= tk.FLAT,
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=8
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
            pady=8
        )

        self.current_candy_label = tk.Label(
            self.left_frame,
            text=self.nombre,
            justify=tk.CENTER,
            **style.STYLELABEL3
        )

        self.current_candy_label.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
        )

        comment_frame = tk.Frame(self.left_frame, bg=style.BACKGROUND2)
        comment_frame.pack(side=tk.BOTTOM, padx=5, pady=2, fill=tk.BOTH, expand=True)

        tk.Label(comment_frame, text=" Comentarios (sin tildes ni ñ) ", font=("Light Calibri", 10), **style.STYLECALCULUS, justify="center"
             ).pack(padx=10, pady=3, side=tk.LEFT)
        
        self.comentarios = tk.Text(comment_frame, height=1, width=1)
        self.comentarios.pack(pady=3, padx=5, fill=tk.X, expand=True, side=tk.LEFT)

        # Frame para las etiquetas
        label_frame = tk.Frame(self.left_frame, bg=style.BACKGROUND2)
        label_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Frame para las barras de string
        entry_frame = tk.Frame(self.left_frame, bg=style.BACKGROUND2)
        entry_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Frame para las etiquetas explicativas
        clarification_frame = tk.Frame(self.left_frame, bg=style.BACKGROUND2)
        clarification_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Crear etiquetas
        labels = ["Sabor", "Duración", " Capacidad de jugueteo ", "Salud", "Precio", "Tienda", "Adicional", "Fecha"]
        for label_text in labels:
            tk.Label(
                label_frame,
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
        for textvariables in self.entries:
            tk.Entry(
                entry_frame,
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
        aclaraciones = ["Escala del 1 al 100", "Total, en minutos", "Escala del 1 al 100", "Escala del 1 al 100. ¿Qué tan saludable es?", "El precio actual en pesos", "Tienda en la que lo compraste", " ¿Quieres añadirle valor adicional por algo? ", "La fecha de hoy en formato DD/MM/YYYY"]
        for texto in aclaraciones:
            #Crear frame para colocar el botón de salud a la derecha
            if texto == "Escala del 1 al 100. ¿Qué tan saludable es?":
                    salud_frame = tk.Frame(clarification_frame, bg="grey")
                    salud_frame.pack(pady=5, expand=True, fill=tk.X, padx=10)

                    tk.Label(
                        salud_frame,
                        text=texto,
                        font=("Light Calibri", 8),
                        **style.STYLECALCULUS,
                        justify="center"
                    ).pack(
                        fill=tk.BOTH,
                        side=tk.LEFT,
                        expand=True
                    )
                    #Estética, para separar el botón de la label
                    tk.Label(
                        salud_frame,
                        text="",
                        bg=style.BACKGROUND2,
                    ).pack(
                        fill=tk.BOTH,
                        side=tk.LEFT,
                        expand=True
                    )

                    tk.Button(
                        salud_frame,
                        text="No me importa mi salud",
                        font=("Light Calibri", 8),
                        bg="#FF7192",
                        activebackground= style.COMPONENT4,
                        activeforeground= style.TEXT,
                        command= self.No_salud,
                        relief="flat" #Quitar el bordecito negro
                    ).pack(
                        fill=tk.BOTH,
                        side=tk.LEFT
                    )

            else:
                tk.Label(
                    clarification_frame,
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

        if self.imagen is None or not self.imagen.winfo_exists():
            try:
                original_image = Image.open("imagenes/" + self.nombre + ".png")
                
                # Ajusta el tamaño de la imagen automáticamente
                width, height = original_image.size
                aspect_ratio = 560/height
                new_width = int(width * aspect_ratio)
                new_height = int(height * aspect_ratio)
                resized_image = original_image.resize((new_width, new_height), PIL.Image.Resampling.LANCZOS)
                self.dulce_image = ImageTk.PhotoImage(resized_image)

                self.imagen = tk.Label(self, image=self.dulce_image)
                self.imagen.pack(
                    expand=True,
                    padx=10,
                    pady=10
                )
            except:
                self.imagen = tk.Label(
                    self,
                    text=f"No se ha encontrado una vista previa del dulce\n  {self.nombre}. Para\n  "
                        f"añadir su imagen, agrega una imagen .PNG en esta carpeta\n  y ponle el mismo EXACTO nombre que le pusiste al dulce\n"
                        f"Si es una golosina múltiple, nombra a la imagen con una @\nantes del nombre. Si es mixta, nómbrala con % antes del nombre.\nEjemplo: @Kegol Sabores Surtidos Caja",                    justify=tk.CENTER
                )
                self.imagen.pack(                    
                    expand=True,
                    padx=10,
                    pady=10
                    )
    
    def create_new_widgets_multiples(self, new_value, peso, porcion):
        
        if self.left_frame:
            for widget in self.left_frame.winfo_children():
                widget.destroy()
        if self.imagen:
            self.imagen.destroy()

        self.configure(background= style.BACKGROUND3)
        self.nombre = new_value
        numero = peso.split(" ")
        self.peso = float(numero[0])
        self.porcion = porcion
        # Frame para que la imagen quede al lado
        if self.left_frame == None:
            self.left_frame = tk.Frame(self, bg=style.BACKGROUND)
            self.left_frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)

        tk.Button(
            self.left_frame,
            text= "Calcular",
            command= self.Calculo_multiple,
            **style.STYLEBUTTON,
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
            relief= tk.FLAT,
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=8
        )

        tk.Button(
            self.left_frame,
            text= "Registrar datos",
            command= self.Registro_multiple,
            **style.STYLEBUTTON,
            relief= tk.FLAT,
            activebackground= style.COMPONENT4,
            activeforeground= style.TEXT,
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=22,
            pady=8
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
            pady=8
        )

        self.current_candy_label = tk.Label(
            self.left_frame,
            text=self.nombre,
            justify=tk.CENTER,
            **style.STYLELABEL3
        )

        self.current_candy_label.pack(
            side=tk.TOP,
            fill=tk.X,
            expand=True,
        )

        comment_frame = tk.Frame(self.left_frame, bg=style.BACKGROUND2)
        comment_frame.pack(side=tk.BOTTOM, padx=5, pady=2, fill=tk.BOTH, expand=True)

        tk.Label(comment_frame, text=" Comentarios (sin tildes ni ñ) ", font=("Light Calibri", 10), **style.STYLECALCULUS, justify="center"
             ).pack(padx=10, pady=3, side=tk.LEFT)
        
        self.comentarios = tk.Text(comment_frame, height=1, width=1)
        self.comentarios.pack(pady=3, padx=5, fill=tk.X, expand=True, side=tk.LEFT)

        # Frame para las etiquetas
        label_frame = tk.Frame(self.left_frame, bg=style.BACKGROUND2)
        label_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Frame para las barras de string
        entry_frame = tk.Frame(self.left_frame, bg=style.BACKGROUND2)
        entry_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Frame para las etiquetas explicativas
        clarification_frame = tk.Frame(self.left_frame, bg=style.BACKGROUND2)
        clarification_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Crear etiquetas
        labels = ["Precio", "Tienda", "Adicional", "Fecha"]
        for label_text in labels:
            tk.Label(
                label_frame,
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

        entradas = [self.precio, self.tienda, self.adicional, self.fecha]

        #Crear entries
        for textvariables in entradas:
            tk.Entry(
                entry_frame,
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
        aclaraciones = ["El precio actual en pesos", "Tienda en la que lo compraste", " ¿Quieres añadirle valor adicional por algo? ", "La fecha de hoy en formato DD/MM/YYYY"]
        for texto in aclaraciones:
            tk.Label(
                clarification_frame,
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

        if self.imagen is None or not self.imagen.winfo_exists():
            try:
                original_image = Image.open("imagenes/" + self.nombre + ".png")
                
                # Ajusta el tamaño de la imagen automáticamente
                width, height = original_image.size
                aspect_ratio = 560/height
                new_width = int(width * aspect_ratio)
                new_height = int(height * aspect_ratio)
                resized_image = original_image.resize((new_width, new_height), PIL.Image.Resampling.LANCZOS)
                self.dulce_image = ImageTk.PhotoImage(resized_image)

                self.imagen = tk.Label(self, image=self.dulce_image)
                self.imagen.pack(
                    expand=True,
                    padx=10,
                    pady=10
                )
            except:
                self.imagen = tk.Label(
                    self,
                    text=f"No se ha encontrado una vista previa del dulce\n  {self.nombre}. Para\n  "
                        f"añadir su imagen, agrega una imagen .PNG en esta carpeta\n  y ponle el mismo EXACTO nombre que le pusiste al dulce\n"
                        f"Si es una golosina múltiple, nombra a la imagen con una @\nantes del nombre. Si es mixta, nómbrala con % antes del nombre.\nEjemplo: @Kegol Sabores Surtidos Caja",                    justify=tk.CENTER
                )
                self.imagen.pack(                    
                    expand=True,
                    padx=10,
                    pady=10
                    )

    def create_new_widgets_mixtos(self, new_value, peso):
        pass
    
    def Calculo(self): 
        try:
            self.calculo = round(float(self.peso)**(float(self.parametros["precio"])/100) * (float(self.sabor.get()) * self.parametros["sabor"] + float(self.duracion.get()) * self.parametros["duracion"] * float(self.sabor.get()) * 2 / float(self.peso) + float(self.salud.get()) * self.parametros["salud"] + float(self.jugueteo.get()) * self.parametros["jugueteo"]) / (float(self.precio.get()) ** (float(self.parametros["precio"])/100)) + float(self.adicional.get()) * self.parametros["adicional"], 2)
            self.barra.set("Resultado del cálculo: " + str(self.calculo))
            self.barra_label.config(font=("Light Calibri", 40))
            self.barra_label.config(fg="white")
            self.x = 1
        except Exception as e:
            self.barra_label.config(fg="white")
            self.barra.set("Debes rellenar todos los campos con algún número (Ej: 2.51)")
            self.barra_label.config(font=("Light Calibri", 30))
            self.x = 0

    def Calculo_multiple(self):
        try:
            dulce_nombre = self.porcion
            archivo_path = os.path.join("candy calculation", f"{dulce_nombre}.txt")
            
            if os.path.isfile(archivo_path):
                with open(archivo_path, "r") as archivo:
                    registros = archivo.readlines()
                    registros_dulce = []

                    for linea in registros:
                        datos = linea.strip().split(" ")
                        datos[8] = dulce_nombre
                        datos[6] = datos[6].replace("_", " ")
                        registros_dulce.append(datos)
                    registros_dulce.sort(key=lambda x: config.custom_sort_fecha(x[7]), reverse=True)

                    if len(registros_dulce) == 1:
                        valores_ponderados = [float(val) for val in registros_dulce[0][:6]]
                    elif len(registros_dulce) == 2:
                        ultimo_registro = registros_dulce[0]
                        penultimo_registro = registros_dulce[1]
                        valores_ultimo = [float(val) for val in ultimo_registro[:6]]
                        valores_penultimo = [float(val) for val in penultimo_registro[:6]]
                        valores_ponderados = [0.25 * val_penultimo + 0.75 * val_ultimo for val_penultimo, val_ultimo in zip(valores_penultimo, valores_ultimo)]
                    elif len(registros_dulce) >= 3:
                        tres_ultimos_registros = registros_dulce[:3]
                        valores_ultimos = [[float(val) for val in registro[:6]] for registro in tres_ultimos_registros]
                        valores_ponderados = [0.11 * valores_ultimos[2][i] + 0.23 * valores_ultimos[1][i] + 0.66 * valores_ultimos[0][i] for i in range(6)]
                    else:
                        print("No hay suficientes registros para calcular el promedio.")
                        return

                    sabor, duracion, jugueteo, salud, precio, adicional = valores_ponderados
                    try:
                        self.calculo = round(float(self.peso)**(float(self.parametros["precio"])/100) * (float(sabor) * self.parametros["sabor"] + float(duracion) * self.parametros["duracion"] * float(sabor) * 2 / float(self.peso) + float(salud) * self.parametros["salud"] + float(jugueteo) * self.parametros["jugueteo"]) / (float(self.precio.get()) ** (float(self.parametros["precio"])/100)) + float(self.adicional.get()) * self.parametros["adicional"], 2)
                        self.barra.set("Resultado del cálculo: " + str(self.calculo))
                        self.barra_label.config(font=("Light Calibri", 40))
                        self.barra_label.config(fg="white")
                        self.x = 1
                    except Exception as ex:
                        self.barra_label.config(fg="white")
                        print("Error calculando los datos")
                        print(ex)
                        self.barra.set("Debes rellenar todos los campos con algún número (Ej: 2.51)")
                        self.barra_label.config(font=("Light Calibri", 30))
                        self.x = 0
        except Exception as e:
            self.barra.set("Error añadiendo datos calculados")
            print(e)

    def No_salud(self):
        self.salud.set(50)
        self.salud_o_no = False

    def Registro_multiple(self):
        if self.x == 1:
            archivo = open("candy calculation/" + self.nombre + ".txt","a")
            comentarios = self.comentarios.get("1.0", "end-1c").encode("utf-8")
            nueva_linea = str(self.precio.get()) + ' ' + str(self.adicional.get()) + ' ' + str(self.tienda.get().replace(" ", "_")) + ' ' + str(self.fecha.get()) + ' "' + str(comentarios.decode("utf-8").replace("\n", " ").replace(" ", "_")) + '"'
            if os.path.getsize("candy calculation/" + self.nombre + ".txt") == 0:
                archivo.write(nueva_linea) #El archivo está vacío, escribe la línea sin enter
            else:
                archivo.write("\n" + nueva_linea) #Escribe la nueva línea con enter
            archivo.close()
            self.barra_label.config(fg="green")
            self.x = 2
        else:
            self.barra_label.config(fg="white")
            self.barra.set('Primero debes presionar "Calcular"')
            self.barra_label.config(font=("Light Calibri", 30))


    def Registro(self):
        if self.x == 1:
            archivo = open("candy calculation/" + self.nombre + ".txt","a")
            comentarios = self.comentarios.get("1.0", "end-1c").encode("utf-8")
            nueva_linea = str(self.sabor.get()) + ' ' + str(self.duracion.get()) + ' ' + str(self.jugueteo.get()) + ' ' + str(self.salud.get()) + ' ' + str(self.precio.get()) + ' ' + str(self.adicional.get()) + ' ' + str(self.tienda.get().replace(" ", "_")) + ' ' + str(self.fecha.get() + ' "' + str(comentarios.decode("utf-8").replace("\n", " ").replace(" ", "_")) + '" ' + str(self.salud_o_no))
            if os.path.getsize("candy calculation/" + self.nombre + ".txt") == 0:
                archivo.write(nueva_linea) #El archivo está vacío, escribe la línea sin enter
            else:
                archivo.write("\n" + nueva_linea) #Escribe la nueva línea con enter
            archivo.close()
            self.barra_label.config(fg="green")
            self.x = 2
        else:
            self.barra_label.config(fg="white")
            self.barra.set('Primero debes presionar "Calcular"')
            self.barra_label.config(font=("Light Calibri", 30))

    def move_to_candy(self):
        if self.x == 2:
            self.sabor.set('')
            self.duracion.set('')
            self.jugueteo.set('')
            self.salud.set('')
            self.precio.set('')
            self.tienda.set('')
            self.adicional.set('')
            self.barra.set('')
            self.fecha.set('')
            self.x = 0
        self.barra.set
        if self.nombre[0] == "@":
            #for var in self.entries:
            #    var.set("")
            #self.barra.set("")
            self.controller.multiple.create_new_widgets(self.controller.multiple_frame, self.nombre)
            self.controller.show_frame(self.controller.multiple)
        else:
            #for var in self.entries:
            #    var.set("")
            #self.barra.set("")
            self.controller.candy.create_new_widgets(self.controller.candy_frame, self.nombre)
            self.controller.show_frame(self.controller.candy)