import tkinter as tk
from tkinter import ttk
from constantes import style, config
from PIL import ImageTk,Image
import PIL
import os

class Multiple(tk.Frame):

    def __init__(self, parent, controller, home_instance, comparison_instance):
        super().__init__(parent)
        self.configure(background= style.BACKGROUND3)
        self.controller = controller
        self.home_instance = home_instance
        self.comparison_instance = comparison_instance
        self.dulce_image = None
        self.dulce_image_2 = None
        self.imagen = None
        self.imagen_2 = None
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
        self.original_frame = None
        self.porciones = 0
        self.porcion = ""
        self.peso = "X g"
        self.sabor = 0
        self.duracion = 0
        self.adicional = 0
        self.salud = 0
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

        self.tree = MultipleTable(self.table_frame)
        self.tree.pack(expand=True, side=tk.LEFT, fill=tk.BOTH, padx=7, pady=11)
        self.tree2 = CommentTable(self.table_frame)
        self.tree2.pack(expand=False, side=tk.LEFT, fill=tk.BOTH, ipadx=40, padx=7, pady=11)
        self.original_frame = tk.Frame(self.table_frame, bg=style.BACKGROUND2)
        self.original_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, ipadx=40, padx=7, pady=11)
        self.original_frame_a = tk.Frame(self.original_frame, bg=style.BACKGROUND2)
        self.original_frame_a.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.original_frame_e = tk.Frame(self.original_frame, bg=style.BACKGROUND2)
        self.original_frame_e.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.original_frame_i = tk.Frame(self.original_frame, bg="pink")
        self.original_frame_i.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

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

        self.current_candy_label = tk.Label(
            self.left_frame,
            text=new_value[1:-1],
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
            self.porcion = "?"

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

        labels = {"Marca":marca, "Energía total":energía_total, "Energía 100g":energía_100g, "Peso":self.peso, "Porciones":self.porciones}
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
        self.tree.cargar_datos(archivo_path, self.peso, self.parametros, self.nombre, self.porcion)
        self.tree2.cargar_datos(archivo_path)


        self.mostrar_datos_promedio()

    def move_to_home(self):
        self.tree.limpiar_tabla()
        self.tree2.limpiar_tabla()
        self.controller.show_frame(self.controller.home)

    def move_to_calculation(self):
        self.tree.limpiar_tabla()
        self.tree2.limpiar_tabla()
        buen_peso = self.peso.split()
        self.controller.calculation.create_new_widgets_multiples(self.controller.calculation_frame, self.nombre, buen_peso[0], self.porcion)
        self.controller.show_frame(self.controller.calculation)

    def mostrar_datos_promedio(self):
        if self.imagen_2:
            self.imagen_2.destroy()
        for widget in self.original_frame_e.winfo_children():
            widget.destroy()
        for widget in self.original_frame_a.winfo_children():
            widget.destroy()

        dulce_nombre = self.porcion
        sabor,duracion,jugueteo,salud,precio,adicional = self.conseguir_datos_promedio()     
        jugueteo = round(jugueteo,2)
        archivo_path_3 = os.path.join("candy data", f"{self.nombre}.txt")
        with open(archivo_path_3, "r") as archivo: 
            datos = archivo.readlines()
            num_unidades = float(datos[-2]) #Necesitamos este número ya que self.peso es el grande
        precio_por_peso = round((precio * num_unidades / float(self.peso.split(" ")[0])), 2)
        duracion_por_peso = round((duracion * num_unidades / float(self.peso.split(" ")[0])), 2)

        # Mostrar los datos promedio en etiquetas dentro de self.original_frame
        etiqueta = tk.Label(self.original_frame_a, text=dulce_nombre, **style.STYLELABEL,)
        etiqueta.pack(side=tk.TOP, anchor="w", padx=5, pady=2, expand=True, fill=tk.X)

        etiqueta = tk.Label(self.original_frame_e, text="Datos promedio", bg=style.COMPONENT6, fg="white", font=("Light Calibri", 13))
        etiqueta.pack(side=tk.TOP, anchor="w", padx=5, expand=True, fill=tk.X)


        etiquetas = [
        ("Sabor", sabor),
        ("Duración por peso", duracion_por_peso),
        ("Jugueteo", jugueteo),
        ("Salud", salud),
        ("Precio por peso", precio_por_peso),
        ("Adicional", adicional)
    ]

        for nombre, valor in etiquetas:
            data_mini_frame = tk.Frame(self.original_frame_e, bg=style.COMPONENT6)
            data_mini_frame.pack(side=tk.TOP, padx=5, pady=2, fill=tk.BOTH, expand=True)

            etiqueta = tk.Label(data_mini_frame, text=nombre, bg=style.COMPONENT2, fg="white")
            etiqueta.pack(side=tk.LEFT, anchor="w", padx=5, pady=5, expand=True, fill=tk.X)

            numero = tk.Label(data_mini_frame, text=str(valor))
            numero.pack(side=tk.RIGHT, anchor="w", padx=5, pady=5, expand=False)

        # Cargar y mostrar la imagen del dulce
        try:
            original_image_2 = Image.open(f"imagenes/{dulce_nombre}.png")
            
            # Ajusta el tamaño de la imagen automáticamente
            width, height = original_image_2.size
            aspect_ratio = 280 / height #310
            if width * aspect_ratio > 260:
                aspect_ratio = 260 / width
            new_width = int(width * aspect_ratio)
            new_height = int(height * aspect_ratio)
            resized_image = original_image_2.resize((new_width, new_height), PIL.Image.Resampling.LANCZOS)

            self.dulce_image_2 = ImageTk.PhotoImage(resized_image)

            self.imagen_2 = tk.Label(self.original_frame_i, image=self.dulce_image_2)
            self.imagen_2.pack(side=tk.LEFT, padx=5, pady=5, expand=True)

        except:
            none_label = tk.Label(
                self.original_frame_i,
                text=f"No se ha encontrado una vista previa de la golosina\n  {dulce_nombre}.\n  "
                    f"Para añadir su imagen, agrega una imagen .PNG en esta carpeta\n y ponle el mismo EXACTO nombre que le pusiste a la golosina. \nSi es una golosina múltiple, nombra a la imagen con una @\nantes del nombre. Si es mixta, nómbrala con % antes del nombre.\nEjemplo: @Kegol Sabores Surtidos Caja",
                justify=tk.CENTER
            )
            none_label.pack(side=tk.LEFT, padx=20, pady=10, expand=True)

    def conseguir_datos_promedio(self):
        try:
            dulce_nombre = self.porcion  # Obtener el nombre del dulce desde self.porcion
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
                        print("No hay suficientes registros para calcular el promedio consiguiendo datos.")
                        return

                    sabor, duracion, jugueteo, salud, precio, adicional = valores_ponderados
                    return sabor,duracion,jugueteo,salud,precio,adicional
            else:
                print("No se encontró el archivo del dulce.")
        except Exception as e:
            print(f"Error al buscar datos promedio: {e}")        
        
class MultipleTable(ttk.Treeview):
    def __init__(self, parent):
        super().__init__(parent)
        self["columns"] = ("Valía", "Precio", "Adicional", "Tienda", "Fecha")

        # Configurar columnas y encabezados
        self.column("#0", width=0, stretch=tk.NO)
        self.column("Valía", anchor=tk.W, width=70)
        self.column("Precio", anchor=tk.W, width=60)
        self.column("Adicional", anchor=tk.W, width=70)
        self.column("Tienda", anchor=tk.W, width=130)
        self.column("Fecha", anchor=tk.W, width=120)

        # Encabezados
        self.heading("#0", text="", anchor=tk.W)
        self.heading("Valía", text="Valía", anchor=tk.W, command=lambda: config.ordenar_por_valia(self))
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
        
    def cargar_datos(self, archivo_path, peso, parametros, nombre, porcion):
        try:
            nuevo_peso = peso.split(" ")
            nuevo_peso = float(nuevo_peso[0])
            try:
                dulce_nombre = nombre  # Obtener el nombre del dulce desde self.nombre
                archivo_path = os.path.join("candy calculation", f"{porcion}.txt")
                
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
                            print("No hay suficientes registros para calcular el promedio en la tabla.")
                            return

                        sabor, duracion, jugueteo, salud, precio, adicional = valores_ponderados
                else:
                    print("No se encontró el archivo del dulce en la tabla.")
            except Exception as e:
                print(f"Error al buscar datos promedio para la tabla: {e}")        

            archivo_path_2 = os.path.join("candy calculation", f"{nombre}.txt")
            archivo_path_3 = os.path.join("candy data", f"{nombre}.txt")

            with open(archivo_path_3, "r") as archivo: 
                datos = archivo.readlines()
                duracion = float(duracion)*float(datos[-2])  # La duracion por el numero de unidades
            with open(archivo_path_2, "r") as archivo:
                for i, linea in enumerate(archivo):
                    datos = linea.strip().split(" ")
                    datos[2] = datos[2].replace("_", " ")
                    precio = datos[0]  # Este es el precio de la caja
                    adicional += float(datos[1])
                    valia = round(float(nuevo_peso)**(float(parametros["precio"])/100) * (float(sabor) * parametros["sabor"] + float(duracion) * parametros["duracion"] * float(sabor) * 2 / float(nuevo_peso) + float(salud) * parametros["salud"] + float(jugueteo) * parametros["jugueteo"]) / (float(precio) ** (float(parametros["precio"])/100)) + float(adicional) * parametros["adicional"], 2)
                    self.insert("", "end", values=[valia] + datos, iid=i)

            # El archivo se cierra automáticamente después de salir del bloque with, no es necesario cerrarlo manualmente.
        except Exception as e:
            print(f"Error al cargar datos en la tabla múltiple: {e}")

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
            print(f"Error al cargar datos de comentarios: {e}")

    def limpiar_tabla(self):
        for item in self.get_children():
            self.delete(item)

    def mostrar_comentarios(self, event):
        item = self.selection()
        item2 = item[0].strip().split(" ")
        if item2:
            # Obtener los comentarios de la línea seleccionada (última columna)
            comentarios = item2[-1]
            comentarios = comentarios.replace("_", " ").replace("_", " ")[:-1]

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