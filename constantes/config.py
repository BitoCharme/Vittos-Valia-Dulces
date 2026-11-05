DULCES = {}

def actualizar_dulces():
    global DULCES
    DULCES.clear()
    with open("Dulces.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.rstrip()
            DULCES[linea.upper()] = linea
    DULCES = dict(sorted(DULCES.items()))

def custom_sort(value):
    if value == 'Irrelevante':
        return float('-inf')  # Tratar 'Irrelevante' como el valor más bajo posible
    else:
        return float(value)

def ordenar_por_valia(self):
    elementos = [(self.item(item)["values"], item) for item in self.get_children()]
    elementos_ordenados = sorted(elementos, key=lambda x: custom_sort(x[0][0]), reverse=True)

    self.limpiar_tabla()
    for valores, item in elementos_ordenados:
        self.insert("", "end", values=valores)

def ordenar_por_sabor(self):
    elementos = [(self.item(item)["values"], item) for item in self.get_children()]
    elementos_ordenados = sorted(elementos, key=lambda x: custom_sort(x[0][1]), reverse=True)
    self.limpiar_tabla()
    for valores, item in elementos_ordenados:
        self.insert("", "end", values=valores)

def ordenar_por_duracion(self):
    elementos = [(self.item(item)["values"], item) for item in self.get_children()]
    elementos_ordenados = sorted(elementos, key=lambda x: custom_sort(x[0][2]), reverse=True)
    self.limpiar_tabla()
    for valores, item in elementos_ordenados:
        self.insert("", "end", values=valores)

def ordenar_por_jugueteo(self):
    elementos = [(self.item(item)["values"], item) for item in self.get_children()]
    elementos_ordenados = sorted(elementos, key=lambda x: custom_sort(x[0][3]), reverse=True)
    self.limpiar_tabla()
    for valores, item in elementos_ordenados:
        self.insert("", "end", values=valores)

def ordenar_por_salud(self):
    elementos = [(self.item(item)["values"], item) for item in self.get_children()]
    elementos_ordenados = sorted(elementos, key=lambda x: custom_sort(x[0][4]), reverse=True)
    self.limpiar_tabla()
    for valores, item in elementos_ordenados:
        self.insert("", "end", values=valores)

def ordenar_por_precio(self):
    elementos = [(self.item(item)["values"], item) for item in self.get_children()]
    elementos_ordenados = sorted(elementos, key=lambda x: custom_sort(x[0][5]), reverse=True)
    self.limpiar_tabla()
    for valores, item in elementos_ordenados:
        self.insert("", "end", values=valores)

def ordenar_por_adicional(self):
    elementos = [(self.item(item)["values"], item) for item in self.get_children()]
    elementos_ordenados = sorted(elementos, key=lambda x: custom_sort(x[0][6]), reverse=True)
    self.limpiar_tabla()
    for valores, item in elementos_ordenados:
        self.insert("", "end", values=valores)

def ordenar_por_tienda(self): #Arreglar esto
    elementos = [(self.item(item)["values"], item) for item in self.get_children()]
    elementos_ordenados = sorted(elementos, key=lambda x: custom_sort(x[0][7]), reverse=True)
    self.limpiar_tabla()
    for valores, item in elementos_ordenados:
        self.insert("", "end", values=valores)

def custom_sort_fecha(fecha):
    # Convertir la fecha al formato "año-mes-día" para facilitar la comparación
    partes_fecha = fecha.split("/")
    return partes_fecha[2], partes_fecha[1], partes_fecha[0]

def ordenar_por_fecha(self):
    elementos = [(self.item(item)["values"], item) for item in self.get_children()]
    elementos_ordenados = sorted(elementos, key=lambda x: custom_sort_fecha(x[0][8]), reverse=True)
    self.limpiar_tabla()
    for valores, item in elementos_ordenados:
        self.insert("", "end", values=valores)

def ordenar_por_nombre(self): #Arreglar esto
    elementos = [(self.item(item)["values"], item) for item in self.get_children()]
    elementos_ordenados = sorted(elementos, key=lambda x: custom_sort(x[0][9]), reverse=True)
    self.limpiar_tabla()
    for valores, item in elementos_ordenados:
        self.insert("", "end", values=valores)