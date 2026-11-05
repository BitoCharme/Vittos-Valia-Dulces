import tkinter as tk
from tkinter import ttk
from constantes import style, config
from PIL import ImageTk,Image
import PIL

class Candy(tk.Frame):

    def __init__(self, parent, controller, home_instance, comparison_instance):
        super().__init__(parent)
        self.configure(background= "pink")
        self.controller = controller
        self.home_instance = home_instance
        self.comparison_instance = comparison_instance
        self.dulce_image = None
        self.imagen = None
        self.none_label = None
        self.current_candy_label = None
        self.nombre = ""
        self.left_frame = None
        self.tree = None
        self.tree2 = None
        self.category_frame_big = None
        self.primera = None
        self.category_frame = None
        self.data_frame = None
        self.porciones = 0
        self.porciones = ""
        self.peso = "X g"
        self.parametros = self.controller.comparison.obtener_variable(self.controller.comparison_frame)
        self.init_widgets()

    def init_widgets(self):
        self.left_frame = tk.Frame(self, bg=style.BACKGROUND)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.table_frame = tk.Frame(self.left_frame, bg=style.BACKGROUND)
        self.table_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        tk.Button(
            self.left_frame,
            text= "Añadir estadísticas",
            command= self.move_to_calculation,
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
            self.left_frame,
            text= "Comer",
            command= self.move_to_eating,
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
            self.left_frame,
            text= "Volver al inicio",
            command= self.move_to_home,
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

        self.tree = CandyTable(self.table_frame)
        self.tree.pack(expand=True, side=tk.LEFT, fill=tk.BOTH, padx=7, pady=11)
        self.tree2 = CommentTable(self.table_frame)
        self.tree2.pack(expand=False, side=tk.LEFT, fill=tk.BOTH, ipadx=40, padx=7, pady=11)

    def create_new_widgets(self, new_value):
        if self.imagen:
            self.imagen.destroy()
        if self.none_label:
            self.none_label.destroy()
        if self.current_candy_label:
            self.current_candy_label.destroy()
        if self.category_frame:
            if hasattr(self, "vsb"):
                self.vsb.destroy()
            for widget in self.category_frame.winfo_children():
                widget.destroy()
            self.category_frame.destroy()
            self.category_frame = None 
            for widget in self.data_frame.winfo_children():
                widget.destroy()

        if str(new_value)[0] == "@":
            self.configure(background= style.BACKGROUND3)
            modo = 2
        elif str(new_value)[0] == "%":
            self.configure(background= style.BACKGROUND4)
            modo = 3
        else:
            self.configure(background= "pink")
            modo = 1


        self.current_candy_label = tk.Label(
            self.left_frame,
            text=new_value,
            justify=tk.CENTER,
            **style.STYLELABEL3
        )
        self.current_candy_label.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=False,
        )

        self.nombre = new_value

        try:
            original_image = Image.open("imagenes/" + str(self.nombre) + ".png")
            
            # Ajusta el tamaño de la imagen automáticamente
            width, height = original_image.size
            aspect_ratio = 620/height
            if width * aspect_ratio > 520:
                aspect_ratio = 520/width
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
                text=f"No se ha encontrado una vista previa de la golosina\n  {self.nombre}.\n  "
                    f"Para añadir su imagen, agrega una imagen .PNG en esta carpeta\n y ponle el mismo EXACTO nombre que le pusiste a la golosina. \nSi es una golosina múltiple, nombra a la imagen con una @\nantes del nombre. Si es mixta, nómbrala con % antes del nombre.\nEjemplo: @Kegol Sabores Surtidos Caja",
                justify=tk.CENTER
            )
            self.none_label.pack(side=tk.LEFT, padx=20, pady=10, expand=True)

                #Empiezan las categorías
        if self.category_frame_big == None:
            self.category_frame_big = tk.Frame(self.left_frame, bg=style.BACKGROUND2)
            self.category_frame_big.pack(side=tk.BOTTOM, padx=10, fill=tk.BOTH)

        if self.primera == None:
            self.primera = tk.Label(
                self.category_frame_big,
                text= '🍬 Categorías:',
                justify= tk.CENTER,
                **style.STYLELABEL
            )
            self.primera.pack(
                side= tk.LEFT,
                padx= 18,
                pady= 20,
            )

        if self.category_frame is None or not self.category_frame.winfo_exists():
            self.category_frame = tk.Text(self.category_frame_big, wrap="word", background=style.BACKGROUND2)
            self.category_frame.pack(side=tk.BOTTOM, padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.vsb = tk.Scrollbar(self.category_frame, command=self.category_frame.yview)
        self.vsb.pack(side="right", fill="y")
        self.category_frame["yscrollcommand"] = self.vsb.set

        try:
            archivo_path = "candy data/" + str(self.nombre) + ".txt"
            archivo = open(archivo_path,"r")
            categorías = archivo.readline().rstrip().split(",")
            marca = archivo.readline().rstrip()
            energía_total = archivo.readline().rstrip()
            energía_100g = archivo.readline().rstrip()
            self.peso = archivo.readline().rstrip()
            self.porciones = archivo.readline().rstrip()
            self.porcion = archivo.readline().rstrip()
            archivo.close()
        except:
            categorías = "?"
            marca = "?"
            energía_total = "?"
            energía_100g = "?"
            self.peso = "?"
            self.porciones = "?"
            self.porción = "?"

        for categoría in categorías:
            nueva = tk.Label(
                self.category_frame,
                text=" " + categoría + " ",
                font=("Light Calibri", 18),
                **style.STYLECATEGORY,
                justify="center"
            )
            nueva.pack(
                fill=tk.X,
                side=tk.LEFT,
                expand=True,
                padx=10,
            )
            self.category_frame.configure(state="normal")
            self.category_frame.window_create("insert", window=nueva, padx=18, pady=10)
            self.category_frame.configure(state="disabled")

        if self.data_frame == None:
            self.data_frame = tk.Frame(self.left_frame, bg=style.BACKGROUND2)
            self.data_frame.pack(side=tk.BOTTOM, padx=10, pady=5, fill=tk.BOTH)

        labels = {"Marca":marca, "Energía total":energía_total, "Energía 100g":energía_100g, "Peso":self.peso, "Porciones":self.porciones, "Porción":self.porcion}
        for label_text in labels:
            data_mini_frame = tk.Frame(self.data_frame, bg=style.COMPONENT2)
            data_mini_frame.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

            tk.Label(
                data_mini_frame,
                text=label_text,
                font=("Light Calibri", 18),
                **style.STYLECALCULUS,
                justify="center"
            ).pack(
                fill=tk.X,
                side=tk.TOP,
                expand=True,
            )

            tk.Label(
                data_mini_frame,
                text=labels[label_text],
                **style.STYLELABEL,
                justify="center"
            ).pack(
                fill=tk.X,
                side=tk.TOP,
                expand=True,
            )
        #Terminan las categorías
            
        # Llama al método cargar_datos con la ruta del archivo de texto
        archivo_path = "candy calculation/" + str(self.nombre) + ".txt"
        self.tree.cargar_datos(archivo_path, self.peso, self.parametros)
        self.tree2.cargar_datos(archivo_path)


    def move_to_home(self):
        self.tree.limpiar_tabla()
        self.tree2.limpiar_tabla()
        self.controller.show_frame(self.controller.home)

    def move_to_calculation(self):
        self.tree.limpiar_tabla()
        self.tree2.limpiar_tabla()
        buen_peso = self.peso.split()
        if str(self.nombre)[0] == "@":
            self.controller.calculation.create_new_widgets_multiples(self.controller.calculation_frame, self.nombre, buen_peso[0])
        elif str(self.nombre)[0] == "%":
            self.controller.calculation.create_new_widgets_mixtos(self.controller.calculation_frame, self.nombre, buen_peso[0])
        else:
            self.controller.calculation.create_new_widgets(self.controller.calculation_frame, self.nombre, buen_peso[0])
        self.controller.show_frame(self.controller.calculation)

    def move_to_eating(self):
        self.controller.eating.create_new_widgets(self.controller.eating_frame, self.nombre, self.porciones, self.porcion)
        self.controller.show_frame(self.controller.eating)

class CandyTable(ttk.Treeview):
    def __init__(self, parent):
        super().__init__(parent)
        self["columns"] = ("Valía", "Sabor", "Duración", "Capacidad de jugueteo", "Salud", "Precio", "Adicional", "Tienda", "Fecha")

        # Configurar columnas y encabezados
        self.column("#0", width=0, stretch=tk.NO)
        self.column("Valía", anchor=tk.W, width=70)
        self.column("Sabor", anchor=tk.W, width=40)
        self.column("Duración", anchor=tk.W, width=60)
        self.column("Capacidad de jugueteo", anchor=tk.W, width=100)
        self.column("Salud", anchor=tk.W, width=50)
        self.column("Precio", anchor=tk.W, width=60)
        self.column("Adicional", anchor=tk.W, width=70)
        self.column("Tienda", anchor=tk.W, width=130)
        self.column("Fecha", anchor=tk.W, width=120)

        # Encabezados
        self.heading("#0", text="", anchor=tk.W)
        self.heading("Valía", text="Valía", anchor=tk.W, command=lambda: config.ordenar_por_valia(self))
        self.heading("Sabor", text="Sabor", anchor=tk.W, command=lambda: config.ordenar_por_sabor(self))
        self.heading("Duración", text="Duración", anchor=tk.W, command=lambda: config.ordenar_por_duracion(self))
        self.heading("Capacidad de jugueteo", text="Cap. jugueteo", anchor=tk.W, command=lambda: config.ordenar_por_jugueteo(self))
        self.heading("Salud", text="Salud", anchor=tk.W, command=lambda: config.ordenar_por_salud(self))
        self.heading("Precio", text="Precio", anchor=tk.W, command=lambda: config.ordenar_por_precio(self))
        self.heading("Adicional", text="Adicional", anchor=tk.W, command=lambda: config.ordenar_por_adicional(self))
        self.heading("Tienda", text="Tienda", anchor=tk.W, command=lambda: config.ordenar_por_tienda(self))
        self.heading("Fecha", text="Fecha", anchor=tk.W, command=lambda: config.ordenar_por_fecha(self))

        # Barra de desplazamiento vertical
        y_scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.yview)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.configure(yscrollcommand=y_scrollbar.set)

        # Barra de desplazamiento horizontal
        x_scrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.xview)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.configure(xscrollcommand=x_scrollbar.set)

        # Estilo
        self.style = ttk.Style(parent)
        self.style.theme_use("clam")
        self.style.configure("Treeview", **style.STYLETABLA)
        self.style.map("Treeview", background=[("selected", style.TEXT2)], foreground=[("selected", style.TEXT)])
        
    def cargar_datos(self, archivo_path, peso, parametros):
        try:
            nuevo_peso = peso.split(" ")
            nuevo_peso = float(nuevo_peso[0])
            with open(archivo_path, "r") as archivo:
                for i, linea in enumerate(archivo):
                    datos = linea.strip().split(" ")
                    datos[6] = datos[6].replace("_", " ")
                    if datos[9] == 'False':
                        datos[3] = "Irrelevante"
                    sabor = datos[0]
                    duracion = datos[1]
                    jugueteo = datos[2]
                    salud = datos[3]
                    precio = datos[4]
                    adicional = datos[5]
                    valia = round(float(nuevo_peso)**(float(parametros["precio"])/100) * (float(sabor) * parametros["sabor"] + float(duracion) * parametros["duracion"] * float(sabor) * 2 / float(nuevo_peso) + float(salud) * parametros["salud"] + float(jugueteo) * parametros["jugueteo"]) / (float(precio) ** (float(parametros["precio"])/100)) + float(adicional) * parametros["adicional"], 2)
                    self.insert("", "end", values=[valia] + datos, iid=i)
                archivo.close()
        except Exception as e:
            print(f"Error al cargar datos en Candy: {e}")

    def limpiar_tabla(self):
        for item in self.get_children():
            self.delete(item)

class CommentTable(ttk.Treeview):
    def __init__(self, parent):
        super().__init__(parent)
        self["columns"] = ("Comentarios")

        # Configurar columnas y encabezados
        self.column("#0", width=0, stretch=tk.NO)
        self.column("Comentarios", anchor=tk.W, width=200)  # Cambié el ancho para dar espacio al botón

        # Encabezados
        self.heading("#0", text="", anchor=tk.W)
        self.heading("Comentarios", text="Comentarios", anchor=tk.W)

        # Barra de desplazamiento vertical
        y_scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.yview)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.configure(yscrollcommand=y_scrollbar.set)

        # Estilo. Por algún motivo copia el estilo de la otra.

        # Asociar la función de mostrar comentarios al clic en la columna de "Comentarios"
        self.bind("<ButtonRelease-1>", self.mostrar_comentarios)
        
        #Para luego cerrarlas
        self.ventanas_emergentes = {}

    def cargar_datos(self, archivo_path):
        try:
            with open(archivo_path, "r") as archivo:
                for i in enumerate(archivo):
                    self.insert("", "end", values="Mostrar", iid=i)
                archivo.close()
        except Exception as e:
            print(f"Error al cargar datos 1: {e}")

    def limpiar_tabla(self):
        for item in self.get_children():
            self.delete(item)

    def mostrar_comentarios(self, event):
        item = self.selection()
        item2 = item[0].strip().split(" ")
        if item2:
            # Obtener los comentarios de la línea seleccionada (última columna)
            comentarios = item2[-2]
            comentarios = comentarios.replace("_", " ").replace("_", " ")

            # Definir la cantidad máxima de palabras por línea
            palabras_por_linea = 13

            # Dividir el comentario en palabras
            palabras = comentarios.split()

            # Crear líneas de texto con el número máximo de palabras por línea
            lineas = []
            for i in range(0, len(palabras), palabras_por_linea):
                linea = " ".join(palabras[i:i + palabras_por_linea])
                lineas.append(linea)

            # Obtener la posición del clic
            x, y = event.x_root, event.y_root
            for ventana in self.ventanas_emergentes.values():
                ventana.destroy()
            self.ventanas_emergentes = {}

            # Mostrar los comentarios en una ventana emergente cerca de la posición del clic
            ventana_emergente = tk.Toplevel(self)
            ventana_emergente.title("Comentario")
            ventana_emergente.geometry(f"+{x}+{y}")  # Establecer la posición de la ventana emergente

            # Mostrar cada línea en un widget Label dentro de la ventana emergente
            for linea in lineas:
                tk.Label(ventana_emergente, text=linea).pack(padx=10, pady=2)

            self.ventanas_emergentes[item] = ventana_emergente
