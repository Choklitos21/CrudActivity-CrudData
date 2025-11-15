# CrudActivity-CrudData
Estructuras de Datos en Python

1. Listas
   + Qué son: Una lista es una colección ordenada y mutable de elementos en Python
   + Por qué son mutables: Las listas son mutables porque, una vez creadas, se pueden cambiar su contenido en el 
   mismo objeto de memoria
   + Situaciones donde resultan útiles:
     + Almacenar colecciones de datos heterogéneos
     + Trabajar con datos que cambian a menudo
     + Implementar estructuras de datos abstractas
     + Manejar secuencias de elementos
     + Ordenar y buscar datos
   + Ejemplos:
    + Creacion
        ~~~
        frutas = ['manzana', 'banana', 'naranja', '']
        print(f"Lista creada: {frutas}")
        ~~~
    + Lectura
        ~~~
        primer_fruta = frutas[0]
        ultima_fruta = frutas[-1]
        print(f"Primera fruta: {primer_fruta}")
        print(f"Última fruta: {ultima_fruta}")
        ~~~
    + Modificación
        ~~~
        frutas[2] = 'kiwi'
        print(f"Lista después de la modificación: {frutas}")

        frutas.append('naranja')
        print(f"Lista después de añadir: {frutas}")
        ~~~
    + Eliminación
        ~~~
        frutas.remove('uva')
        print(f"Lista después de eliminar 'uva': {frutas}")
        ~~~
2. Tuplas
    + Qué son: Una tupla es una colección ordenada e inmutable de elementos
    + Por qué son inmutables: Las tuplas son inmutables porque, una vez que se han creado, no se pueden modificar,
      añadir, o eliminar elementos
    + Situaciones donde resultan utiles: 
      + Valores Constantes
      + Retorno de Funciones
      + Desempaquetado
      + Datos Heterogéneos Estructurados
    + Un ejemplo de acceso y recorrido:
      + Acceso:
        ~~~
        producto = ('Laptop Pro', 1299.99, 15) # Nombre, Precio, Stock)
        print(f"Nombre del producto: {producto[0]}")
        print(f"Precio: ${producto[1]}")
        print(f"Stock disponible: {producto[2]} unidades")
        ~~~
      + Recorrido:
        ~~~
        print("Recorrido de la tupla 'colores':")
        for color in colores:
            print(f"- {color}")
        ~~~
3. Diccionarios
    + Qué son y cómo almacenan información: Un diccionario en Python es una colección desordenada y mutable de 
    elementos que almacenan información en pares de clave-valor
    + Diferencias clave frente a listas y tuplas: La principal diferencia entre los diccionarios y las listas/tuplas 
    radica en el modo de acceso y la estructura de los datos
    + Ejemplos:
      + Agregar:
      ~~~
      libro["editorial"] = "Editorial Sudamericana"
      print(f"Después de agregar: {libro}")
      ~~~
      + Consultar:
      ~~~
      autor = libro["autor"]
      paginas = libro["paginas"]
      print(f"El autor es: {autor}")
      print(f"Número de páginas: {paginas}")
      ~~~
      + Modificar:
      ~~~
      libro["año_publicacion"] = 1968
      print(f"Después de modificar el año: {libro}")
      ~~~
      + Eliminar:
      ~~~
      paginas_eliminadas = libro.pop("paginas")
      print(f"Páginas eliminadas: {paginas_eliminadas}")
      ~~~
4. Match-case
    + Qué es y desde que version existe en python: El match-case es una estructura de control de flujo en Python 
   utilizada para la comparación de patrones, el match-case fue introducido en Python a partir de la versión 3.10
    + Para qué se usa: Se utiliza para tomar decisiones basadas en la estructura y el valor de los datos de entrada. 
   En su forma más sencilla, compara una expresión con una serie de patrones definidos
    + Diferencias entre 'if' y 'elif': Aunque tanto if/elif como match/case se utilizan para tomar decisiones, 
   difieren en su enfoque y capacidad, el match/case se enfoca en la estructura de los datos como tuplas, listas, 
   diccionarios y los if/elif se enfoca en sí una condición es True o False.
    + Situaciones donde usarlo puede ser más claro: Manejo de comandos/opciones, desestructuración de Tuplas y Listas,
   implementación de Máquinas de Estado
    + Ejemplo:
    ~~~
    match data:
        case 1:
            print("Entra opcion 1")
        case 2:
            print("Entra opcion 2")
        case 3:
            print("Entra opcion 3")
        case _:
            print("Entra a opción base si no entra a ninguna otra antes")
    ~~~
