from Manager import Manager

if __name__ == "__main__":
    app = Manager()
    app.toggle_fullscreen()
    app.update_idletasks()
    app.mainloop()

#La salud podria ser: (100 - A*Calorías - p*Azucares - p*Grasas -B*sodio -C) ingredientes +C adicional   Con A,B constantes, C son constantes, p es su gramaje, todo medido cada 100 g. Acabar con la salud, calcularla bien y que sea única. Sería más inteligente que no exista la variable salud si no el parámetro
#Dejar el *2 de la duración, hacer que la duración sea partido en 100 y que no sea parte de los 4 grandes.
#Ahora quiero: Multiple, arreglar comparison (debe hacer el promedio de precios y adicionales) que puedas ir al dulce desde múltiple, que salga en Comparison, que no salga el @.
# Añadir distintos colroes (ej: modo chocolate), modo copiar colores del dulce. 
#Hacer un buen análisis
#Agregar dulces compuestos? La idea es que su interfaz sea distinta, nuevo tipo de dulce, tienes que colocar registros individuales de los tipos de dulce que contiene, y el promedio de cada registro es el registro que tiene. Se toma como dulce normal.
# Buscador de marcas en Comparison. imágenes en portada
# Calcular caja rouge. Colocar Bombones. Calcular Fini Tubos. La idea es que el dulce se coma con Eating y se anote el dato total al final. Si no, que se agregue cada duración de cada unidad manual
#Crear Eating, poner numero de etiquetas igual a porciones. Al terminar te dan promedio, desviación estándar y botón para ir a stats. Para lo de porciones tiene que alcanzar a 20+
    #Analizar si la formula para la duracion esta bien
    #El comparison necesita mostrar la marca en vez de la tienda
    #Crear tipo de dulce especial que sea hecho de otros dulces (composision de ducles)
    #Si las etiquetas con nombres de dulces son muy largas, hacer algo
    #los comentarios Deberían ordenarse además cuando se cambia el orden de la tabla.
    #Debería haber algo que hable de dulces muy similares, para hacer una buena comparación
    #Corregir nombres
    #Crear una forma de ordenar por fecha y tienda
    #Que funcionen tildes y ñs en: comentarios, nombre dulce, todo
    #Que puedas poner mins y segundos y te lo calcule, o tenga un conversor de segundos a minutos en la colecta de datos
    #Implementar la desv. estándar
    #Quitar el boton de la salud y relacionados
    #Hacer algo al respecto de las porciones horribles porque mal puestas en envase
# tabla. Tengo que cambiar los colores y ordenarla por fecha
    #Que la tabla se actualice al añadir datos sin tener que volver al menú. 
    #Añadir lo del agua, duracion adicional?
    #Opcion borrar dulces y registros
    #Que en comparison veas el precio por gramo
    #Que en comparison puedas variar la relevancia de varias variables para ver los tops
    #Añadir una manera de colocar la imagen directamente en creation
    #Buscar errores en Creation y decirlo.
    
    #Opcional:   
    #mandarla y ver como volverla una app.
    #Podría hacer que las categorías sean presiopnables y te manden a una screen con historia y descripción de la categoría.
    #Añadir las imagenes en menú inicio. #Subir al celular? Subir a un mercado?