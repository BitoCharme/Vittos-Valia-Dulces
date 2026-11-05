import tkinter as tk
from constantes import style, config
from tkinter import ttk
import os

class Comparison(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background= style.COMPONENT2_1)
        self.controller = controller
        self.parametros_calculo = self.obtener_variable()
        self.comparison_table = None
        self.category_frame = None
        self.categorias = ["Almendra","Aro","Arroz","Barquillo","Barra de proteina","Barra de cereal","Barra de chocolate","Bite","Bizcocho","Bombon","Caramelo","Centro liquido","Cereal","Chocolate","Chocolate blanco","Chocolate relleno","Chocolatina","Cinta","Confite","Dragee","Galleta","Galleton","Gel dulce en forma de tubo","Golosina multiple","Gomita","Gusano","Huevito de chocolate", "Malvavisco","Mani","Masticable","Mazapan","Medicinal", "Mix", "Osito", "Papa frita", "Papa frita corte liso", "Personal", "Picante", "Regalo", "Salado", "Sin gluten", "Tortilla de maiz", "Trufa", "Turron", "Vegano"]
        self.init_widgets()
    def init_widgets(self):
        tk.Button(
            self,
            text= "Cambiar parámetros",
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


        # Crear un frame para contener el canvas y la scrollbar
        container_frame = tk.Frame(self, bg=style.COMPONENT4, padx=22, pady=11)
        container_frame.pack(side=tk.TOP, fill=tk.X)

        # Crear un canvas
        canvas = tk.Canvas(container_frame, bg=style.COMPONENT5, height=40)
        canvas.pack(side=tk.TOP, fill=tk.X,)

        # Crear una scrollbar horizontal y asociarla con el canvas
        hsb = tk.Scrollbar(container_frame, orient="horizontal", command=canvas.xview)
        hsb.pack(side=tk.TOP, fill=tk.X)
        canvas.configure(xscrollcommand=hsb.set)

        # Crear un frame dentro del canvas para contener los botones
        self.category_frame = tk.Frame(canvas, bg=style.COMPONENT)
        canvas.create_window((0, 0), window=self.category_frame, anchor="nw")

        tk.Button(
            self.category_frame,
            text="Restablecer tabla",
            command=lambda: self.comparison_table.cargar_datos(self.parametros_calculo),
            **style.STYLEBUTTON2,
            relief=tk.FLAT,
            activebackground=style.COMPONENT4,
            activeforeground=style.TEXT,
        ).pack(
            side=tk.LEFT,
            fill=tk.X,
            #expand=True,
            padx=7,
            pady=5
        )

        for categoria in self.categorias:
            tk.Button(
                self.category_frame,
                text=categoria,
                command=lambda cat=categoria: self.comparison_table.cargar_datos(self.parametros_calculo, cat),
                **style.STYLEBUTTON3,
                relief=tk.FLAT,
                activebackground=style.COMPONENT4,
                activeforeground=style.TEXT,
            ).pack(
                side=tk.LEFT,
                fill=tk.X,
                #expand=True,
                padx=7,
                pady=5
            )

        # Configurar el tamaño del canvas para ajustarse a los botones
        self.category_frame.update_idletasks()  # Asegurarse de que el tamaño del frame se haya actualizado
        canvas.config(scrollregion=canvas.bbox("all"))

        # Asegurarse de que el tamaño del frame se actualice automáticamente
        #self.category_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

        self.comparison_table = ComparisonTable(self)
        self.comparison_table.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.comparison_table.cargar_datos(self.parametros_calculo)

    def obtener_variable(self):
        with open("Parametros.txt", "r") as archivo:
            contenido = archivo.read()
            self.parametros_calculo = eval(contenido)
        return self.parametros_calculo

    def move_to_formula(self):
        self.controller.show_frame(self.controller.formula)

    def move_to_home(self):
        self.controller.show_frame(self.controller.home)

class ComparisonTable(ttk.Treeview):
    def __init__(self, parent):
        super().__init__(parent)
        self.lineas_agregadas = 0
        self.posiciones_dulces = {}
        self["columns"] = ("Valía", "Sabor", "Duración / Gramaje", "Capacidad de jugueteo", "Salud", "Precio / Gramaje", "Adicional", "Última tienda", "Última fecha", "Nombre", "Posición")

        # Configurar columnas y encabezados
        self.column("#0", width=0, stretch=tk.NO)
        self.column("Valía", anchor=tk.W, width=70)
        self.column("Sabor", anchor=tk.W, width=40)
        self.column("Duración / Gramaje", anchor=tk.W, width=60)
        self.column("Capacidad de jugueteo", anchor=tk.W, width=70)
        self.column("Salud", anchor=tk.W, width=50)
        self.column("Precio / Gramaje", anchor=tk.W, width=80)
        self.column("Adicional", anchor=tk.W, width=70)
        self.column("Última tienda", anchor=tk.W, width=130)
        self.column("Última fecha", anchor=tk.W, width=100)
        self.column("Nombre", anchor=tk.W, width=400)
        self.column("Posición", anchor=tk.W, width=60)

        # Encabezados
        self.heading("#0", text="", anchor=tk.W)
        self.heading("Valía", text="Valía", anchor=tk.W, command=lambda: config.ordenar_por_valia(self))
        self.heading("Sabor", text="Sabor", anchor=tk.W, command=lambda: config.ordenar_por_sabor(self))
        self.heading("Duración / Gramaje", text="Duración / Gramaje", anchor=tk.W, command=lambda: config.ordenar_por_duracion(self))
        self.heading("Capacidad de jugueteo", text="Cap. jugueteo", anchor=tk.W, command=lambda: config.ordenar_por_jugueteo(self))
        self.heading("Salud", text="Salud", anchor=tk.W, command=lambda: config.ordenar_por_salud(self))
        self.heading("Precio / Gramaje", text="Precio / Gramaje", anchor=tk.W, command=lambda: config.ordenar_por_precio(self))
        self.heading("Adicional", text="Adicional", anchor=tk.W, command=lambda: config.ordenar_por_adicional(self))
        self.heading("Última tienda", text="Última tienda", anchor=tk.W, command=lambda: config.ordenar_por_tienda(self))
        self.heading("Última fecha", text="Última fecha", anchor=tk.W, command=lambda: config.ordenar_por_fecha(self))
        self.heading("Nombre", text="Nombre", anchor=tk.W, command=lambda: config.ordenar_por_nombre(self))
        self.heading("Posición", text="Posición", anchor=tk.W, command=lambda: self.actualizar_posiciones())

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
        
    def cargar_datos(self, parametros_calculo, categoria_filtrada=None):
        self.limpiar_tabla()
        try:
            with open("Dulces.txt", "r") as dulces_file:
                dulces = dulces_file.readlines()
                for dulce_nombre in dulces:
                    dulce_nombre = dulce_nombre.strip()
                    archivo_path = os.path.join("candy calculation", f"{dulce_nombre}.txt")
                    if os.path.isfile(archivo_path):
                        archivo_path_2 = os.path.join("candy data", f"{dulce_nombre}.txt")
                        with open(archivo_path_2, "r") as archivo:
                            categorias = archivo.readline().strip().split(",")
                            if categoria_filtrada and categoria_filtrada not in categorias:
                                continue
                            marca = archivo.readline().strip()
                            energia_total = archivo.readline().strip()
                            energia_100g = archivo.readline().strip()
                            peso = archivo.readline().strip()
                            num_unidades = archivo.readline().strip()
                            unidad = archivo.readline().strip()
                        if dulce_nombre.startswith('@'):
                            archivo_path = os.path.join("candy calculation", f"{unidad}.txt")
                        self.cargar_datos_dulce(archivo_path, peso, parametros_calculo, dulce_nombre, num_unidades)
            if categoria_filtrada == None:
                self.entregar_posiciones()
            else:
                self.actualizar_posiciones()
        except Exception as e:
            print(f"Error al cargar datos de dulces: {e}")

    def cargar_datos_dulce(self, archivo_path, peso, parametros, dulce_nombre, num_unidades):
        try:
            nuevo_peso = float(peso.split(" ")[0])

            with open(archivo_path, "r") as archivo:
                registros = archivo.readlines()
                registros_dulce = []

                for linea in registros:
                    datos = linea.strip().split(" ")
                    datos[8] = dulce_nombre
                    datos[6] = datos[6].replace("_", " ")
                    registros_dulce.append(datos)

                registros_dulce.sort(key=lambda x: config.custom_sort_fecha(x[7]), reverse=True)

                if len(registros_dulce) == 2:
                    ultimo_registro = registros_dulce[0]
                    penultimo_registro = registros_dulce[1]
                    valores_ultimo = [float(val) for val in ultimo_registro[:6]]
                    valores_penultimo = [float(val) for val in penultimo_registro[:6]]
                    valores_ponderados = [0.25 * val_penultimo + 0.75 * val_ultimo for val_penultimo, val_ultimo in zip(valores_penultimo, valores_ultimo)]
                    nombre = ultimo_registro[8]
                    tienda = ultimo_registro[6]
                    sabor, duracion, jugueteo, salud, precio, adicional = valores_ponderados
                    if dulce_nombre.startswith('@'):
                        archivo_path_at = os.path.join("candy calculation", f"{dulce_nombre}.txt")
                        with open(archivo_path_at, "r") as archivo:
                            registros_at = archivo.readlines()
                            precios = []
                            adicionales = []
                            for linea in registros_at:
                                datos = linea.strip().split(" ")
                                precios.append(float(datos[0]))
                                adicionales.append(float(datos[1]))

                            # Aplicar ponderación dependiendo de la cantidad de registros
                            if len(precios) == 1:
                                precio = precios[0]
                                adicional = adicional + adicionales[0]
                            elif len(precios) == 2:
                                precio = 0.75 * precios[0] + 0.25 * precios[1]
                                adicional = adicional + 0.75 * adicionales[0] + 0.25 * adicionales[1]
                            elif len(precios) >= 3:
                                precio = 0.66 * precios[0] + 0.23 * precios[1] + 0.11 * precios[2]
                                adicional = adicional + 0.66 * adicionales[0] + 0.23 * adicionales[1] + 0.11 * adicionales[2]

                            valores_ponderados[-1] = adicional
                            valores_ponderados[-2] = precio
                            valores_ponderados[1] = float(duracion) * float(num_unidades)

                    valia = round(float(nuevo_peso)**(float(parametros["precio"]) / 100) *
                                (sabor * parametros["sabor"] +
                                duracion * parametros["duracion"] * sabor * 2 / float(nuevo_peso) +
                                salud * parametros["salud"] +
                                jugueteo * parametros["jugueteo"]) /
                                (float(precio) ** (float(parametros["precio"]) / 100)) +
                                adicional * parametros["adicional"], 2)
                    self.agregar_registro_promedio(valia, valores_ponderados, tienda, penultimo_registro[7], nombre, nuevo_peso)
                elif len(registros_dulce) == 1:
                    self.agregar_registro(registros_dulce[0], dulce_nombre, nuevo_peso, parametros, num_unidades)
                elif len(registros_dulce) >= 3:
                    tres_ultimos_registros = registros_dulce[:3]
                    valores_ultimos = [[float(val) for val in registro[:6]] for registro in tres_ultimos_registros]
                    valores_ponderados = [0.11 * valores_ultimos[2][i] + 0.23 * valores_ultimos[1][i] + 0.66 * valores_ultimos[0][i] for i in range(6)]
                    nombre = tres_ultimos_registros[0][8]
                    tienda = tres_ultimos_registros[0][6]
                    sabor, duracion, jugueteo, salud, precio, adicional = valores_ponderados
                    if dulce_nombre.startswith('@'):
                        archivo_path_at = os.path.join("candy calculation", f"{dulce_nombre}.txt")
                        with open(archivo_path_at, "r") as archivo:
                            registros_at = archivo.readlines()
                            precios = []
                            adicionales = []
                            for linea in registros_at:
                                datos = linea.strip().split(" ")
                                precios.append(float(datos[0]))
                                adicionales.append(float(datos[1]))

                            # Aplicar ponderación dependiendo de la cantidad de registros
                            if len(precios) == 1:
                                precio = precios[0]
                                adicional = adicional + adicionales[0]
                            elif len(precios) == 2:
                                precio = 0.75 * precios[0] + 0.25 * precios[1]
                                adicional = adicional + 0.75 * adicionales[0] + 0.25 * adicionales[1]
                            elif len(precios) >= 3:
                                precio = 0.66 * precios[0] + 0.23 * precios[1] + 0.11 * precios[2]
                                adicional = adicional + 0.66 * adicionales[0] + 0.23 * adicionales[1] + 0.11 * adicionales[2]

                            valores_ponderados[-1] = adicional
                            valores_ponderados[-2] = precio
                            valores_ponderados[1] = float(duracion) * float(num_unidades)

                    valia = round(float(nuevo_peso)**(float(parametros["precio"]) / 100) *
                                (sabor * parametros["sabor"] +
                                duracion * parametros["duracion"] * sabor * 2 / float(nuevo_peso) +
                                salud * parametros["salud"] +
                                jugueteo * parametros["jugueteo"]) /
                                (float(precio) ** (float(parametros["precio"]) / 100)) +
                                adicional * parametros["adicional"], 2)
                    self.agregar_registro_promedio(valia, valores_ponderados, tienda, tres_ultimos_registros[0][7], nombre, nuevo_peso)

        except Exception as e:
            print(f"Error al cargar datos en Comparison para {dulce_nombre}: {e}, contenido de datos: {datos}")

    def agregar_registro_promedio(self, valia, valores_ponderados, tienda, fecha, nombre, nuevo_peso):
        valores_ponderados = [round(val, 2) for val in valores_ponderados]
        valia = round(valia, 2)
        precio_por_peso = round(valores_ponderados[4] / nuevo_peso, 2)
        duracion_por_peso = round(valores_ponderados[1] / nuevo_peso, 3) 
        valores_ponderados[4] = precio_por_peso
        valores_ponderados[1] = duracion_por_peso 
        self.insert("", "end", values=[valia] + valores_ponderados + [tienda, fecha, nombre, ""])  # Agregar una posición temporal

    def agregar_registro(self, datos, dulce_nombre, nuevo_peso, parametros, num_unidades):
        # Calcular la valía con los datos del registro y agregarlo a la tabla
        sabor, duracion, jugueteo, salud, precio, adicional = map(float, datos[:6])
        if dulce_nombre.startswith('@'):
            archivo_path_at = os.path.join("candy calculation", f"{dulce_nombre}.txt")
            with open(archivo_path_at, "r") as archivo:
                registros = archivo.readlines()
                precios = []
                adicionales = []
                for linea in registros:
                    otros_datos = linea.strip().split(" ")
                    precios.append(float(otros_datos[0]))
                    adicionales.append(float(otros_datos[1]))

                # Aplicar ponderación dependiendo de la cantidad de registros
                if len(precios) == 1:
                    precio = precios[0]
                    adicional = adicional + adicionales[0]
                elif len(precios) == 2:
                    precio = 0.75 * precios[0] + 0.25 * precios[1]
                    adicional = adicional + 0.75 * adicionales[0] + 0.25 * adicionales[1]
                elif len(precios) >= 3:
                    precio = 0.66 * precios[0] + 0.23 * precios[1] + 0.11 * precios[2]
                    adicional = adicional + 0.66 * adicionales[0] + 0.23 * adicionales[1] + 0.11 * adicionales[2]

                duracion = duracion * float(num_unidades)

        precio_por_peso = round(precio / nuevo_peso, 2)  # Calcular el precio por peso
        duracion_por_peso = round(duracion / nuevo_peso, 3)  # Calcular el precio por peso
        valia = round(float(nuevo_peso)**(float(parametros["precio"])/100) * 
                    (sabor * parametros["sabor"] + 
                    duracion * parametros["duracion"] * sabor * 2 / float(nuevo_peso) + 
                    salud * parametros["salud"] + 
                    jugueteo * parametros["jugueteo"]) / 
                    (float(precio) ** (float(parametros["precio"])/100)) + 
                    adicional * parametros["adicional"], 2)
        self.insert("", "end", values=[valia, sabor, duracion_por_peso, jugueteo, salud, precio_por_peso, adicional, datos[6].replace("_", " "), datos[7], dulce_nombre, ""])  # Agregar una posición temporal

    def entregar_posiciones(self):
        try:
            dulces = [(float(self.item(item, "values")[0]), item) for item in self.get_children()]
            
            dulces_sorted = sorted(dulces, key=lambda x: x[0], reverse=True)
            
            for pos, (_, item) in enumerate(dulces_sorted, start=1):
                valores = list(self.item(item, "values"))
                valores[-1] = f"{pos}°"  # Actualizar la última columna con la posición
                self.item(item, values=valores)
                nombre_dulce = valores[-2]  # Obtener el nombre del dulce
                self.posiciones_dulces[nombre_dulce] = f"{pos}°"

        except Exception as e:
            print(f"Error al entregar posiciones: {e}")

    def actualizar_posiciones(self):
        try:
            dulces = [(float(self.item(item, "values")[0]), item) for item in self.get_children()]
            
            dulces_sorted = sorted(dulces, key=lambda x: x[0], reverse=True)
            
            for pos, (_, item) in enumerate(dulces_sorted, start=1):
                valores = list(self.item(item, "values"))
                nombre_dulce = valores[-2]  # Obtener el nombre del dulce
                valores[-1] = f"{self.posiciones_dulces[nombre_dulce]}"  # Actualizar la última columna con la posición
                self.item(item, values=valores)

        except Exception as e:
            print(f"Error al actualizar posiciones: {e}")

    def limpiar_tabla(self):
        # Eliminar todos los registros en la tabla
        for item in self.get_children():
            self.delete(item)