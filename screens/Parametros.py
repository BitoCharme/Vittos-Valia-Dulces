import tkinter as tk
from constantes import style

class Parametros(tk.Frame):

    def __init__(self, parent, controller, comparison_instance):
        super().__init__(parent)
        self.configure(background= style.COMPONENT)
        self.controller = controller
        self.comparison_instance = comparison_instance
        self.parametros = self.controller.comparison.obtener_variable(self.controller.comparison_frame)
        self.sabor = tk.StringVar()
        self.duracion = tk.StringVar()
        self.salud = tk.StringVar()
        self.jugueteo = tk.StringVar()
        self.precio = tk.StringVar()
        self.adicional = tk.StringVar()
        self.sabor_actual = tk.StringVar()
        self.duracion_actual = tk.StringVar()
        self.salud_actual = tk.StringVar()
        self.jugueteo_actual = tk.StringVar()
        self.precio_actual = tk.StringVar()
        self.adicional_actual = tk.StringVar()
        self.entries = [self.sabor, self.duracion, self.salud, self.jugueteo, self.precio, self.adicional]
        self.actuales = [self.sabor_actual, self.duracion_actual, self.salud_actual, self.jugueteo_actual, self.precio_actual, self.adicional_actual]
        self.barra_label = None
        self.barra = tk.StringVar()
        self.etiquetas_parametros = {}
        self.sabor_actual.set(str(self.parametros["sabor"]))
        self.duracion_actual.set(str(self.parametros["duracion"]))
        self.salud_actual.set(str(self.parametros["salud"]))
        self.jugueteo_actual.set(str(self.parametros["jugueteo"]))
        self.precio_actual.set(str(self.parametros["precio"]))
        self.adicional_actual.set(str(self.parametros["adicional"]))
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
            text= "Volver a la fórmula",
            command= self.move_to_formula,
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
            text= "Alterar parámetros",
            command= self.alterar,
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
        label_frame = tk.Frame(self, bg=style.BACKGROUND2)
        label_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

        # Frame para los parametros
        parametros_frame = tk.Frame(self, bg=style.BACKGROUND2)
        parametros_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH)

        # Frame para las barras de string
        entry_frame = tk.Frame(self, bg=style.BACKGROUND2)
        entry_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        texto = 'Los parámetros de sabor, duración, capacidad de jugueteo y salud\ndeben sumar 100, de manera en la que cada parámetro es su porcentaje de\nrelevancia. De la misma forma, el parámetro del precio debe ser un número\nentre 0 y 100 para representar su porcentaje de relevancia. Si te es\nirrelevante la salud o el jugueteo te recomiendo dejarlos en 0.\nRecomiendo que el parámetro del adicional sea más grande\nmientras más pequeño sea el parámetro del precio para que el adicional\nsiga teniendo un efecto. Por último, recomiendo modificar los\nparámetros con el objetivo de que tus dulces favoritos\nsean los mejores, y así se adaptarán mejor a tus gustos.\nAlgunos ejemplos de parámetros para guiarse:\n\n"Me muero de inanición": Sabor = 60, Duración = 15,\nSalud = 15, Jugueteo = 10, Precio = 100, Adicional = 3\n\n"Parámetros del autor": Sabor = 66, Duración = 10,\nSalud = 15, Jugueteo = 9, Precio = 25, Adicional = 15\n\n"Soy billonario y no me importa mi salud": Sabor = 70, Duración = 20,\nSalud = 0, Jugueteo = 10, Precio = 0, Adicional = 20'

        # Label para explicaciones
        explicaciones = tk.Label(self, bg=style.BACKGROUND2, font=style.FONT3, text=texto)
        explicaciones.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Crear etiquetas
        labels = ["Sabor", "Duración", "Salud", " Jugueteo ", "Precio", "Adicional"]
        tk.Label(
            label_frame,
            text="Datos",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
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

        # Crear parametros
        tk.Label(
            parametros_frame,
            text=" Parámetros actuales ",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )

        self.etiquetas_parametros = []  # Lista para almacenar las etiquetas creadas

        for valor_parametro in self.actuales:
            etiqueta = tk.Label(
                parametros_frame,
                textvariable=valor_parametro,  # Usa la variable de texto directamente
                font=("Light Calibri", 18),
                **style.STYLECALCULUS,
                justify="center"
            )
            etiqueta.pack(
                fill=tk.X,
                expand=True,
                padx=10,
                pady=3
            )
            self.etiquetas_parametros.append(etiqueta)  # Agrega la etiqueta a la lista de etiquetas

        #Crear entries
        tk.Label(
            entry_frame,
            text="Nuevos parámetros",
            **style.STYLETOP,
            justify="center"
        ).pack(
            fill=tk.X,
            expand=True,
        )
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

    def move_to_comparison(self):
        self.controller.show_frame(self.controller.comparison)
        self.barra.set("")

    def move_to_formula(self):
        self.controller.show_frame(self.controller.formula)
        self.barra.set("")

    def alterar(self):
        try:
            suma_total = float(self.sabor.get()) + float(self.duracion.get()) + float(self.salud.get()) + float(self.jugueteo.get())
            if suma_total != 100:
                self.barra_label.config(fg="white")
                self.barra.set('Los parámetros no suman 100')
                return
            if float(self.precio.get()) < 0 or float(self.precio.get()) > 100:
                self.barra_label.config(fg="white")
                self.barra.set('El parámetro del precio no está entre 0 y 100')
                return
            nuevos_parametros = f'{{"sabor": ({self.sabor.get()}), "duracion": ({self.duracion.get()}), "salud": ({self.salud.get()}), "jugueteo": ({self.jugueteo.get()}), "precio": ({self.precio.get()}), "adicional": ({self.adicional.get()})}}'
            with open("Parametros.txt", "w") as archivo:
                archivo.write(nuevos_parametros)
            archivo.close()
            self.barra.set("Parámetros actualizados")
            self.actualizar_parametros()
            for var in self.entries:
                var.set("")
        except Exception as e:
            self.barra_label.config(fg="white")
            self.barra.set('Hubo algún error con los datos proporcionados')
            print(e)

    def actualizar_parametros(self):
        self.parametros = self.controller.comparison.obtener_variable(self.controller.comparison_frame)
        # Actualizar las etiquetas de los parámetros actuales con los nuevos valores
        for i, valor_parametro in enumerate(self.actuales):
            valor_parametro.set(str(self.parametros[list(self.parametros.keys())[i]]))

