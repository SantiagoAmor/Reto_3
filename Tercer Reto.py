 # Primero vamos a definir la clase principal que contendrá el menú y los
 # métodos para encontrar el total.
class MenuItem:

    #* Aqui definimos atributos comunes como lo son nombre y precio
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    #* Aqui definimos un método para posteriormente encontrar el precio total
    def encontrar_precio_total(self) -> float:
        return self.precio

 # Ahora vamos a definir las clases para cada tipo de elemento del menú y 
 # haremos que estos hereden de MenuItem.
 # Primero la clase Bebida
class Bebida(MenuItem):

    #* Aqui definimos los atributos comunes y le agregamos el atributo
    #* tamaño, el cual puede ser pequeño, mediano o grande
    def __init__(self, nombre: str, precio: float, tamaño: str):

        #* Con este super llamamos al inicializador de la clase MenuItem
        super().__init__(nombre, precio)
        self.tamaño = tamaño
        
    #* Hacemos lo mismo que en la clase MenuItem
    def encontrar_precio_total(self) -> float:
        return self.precio

 # Ahora definimos la clase Aperitivo
class Aperitivo(MenuItem):
    
    #* Aqui lo mismo que las bebidas pero en vez de tamaño le agregamos
    #* porciones, el cual es un entero que representa la cantidad de porciones
    def __init__(self, nombre: str, precio: float, porciones: int):
        super().__init__(nombre, precio)
        self.porciones = porciones

    #* Aqui hacemos lo mismo pero lo multiplicamos por la cantidad de porciones
    def encontrar_precio_total(self) -> float:
        return self.precio * self.porciones

 # Ahora definimos la clase PlatoPrincipal
class PlatoPrincipal(MenuItem):

    #* Aqui nuevamente lo mismo pero en este caso le agregamos el atributo
    #* acompañamientos, el cual es un entero que representa la cantidad de
    #* acompañamientos
    def __init__(self, nombre: str, precio: float, acompañamientos: int):
        super().__init__(nombre, precio)
        self.acompañamientos = acompañamientos

    #* Aqui nuevamente lo mismo pero le agregamos un costo adicional por cada
    #* acompañamiento, en este caso 2.5. Entonces si no se quieren 
    #* acompañamientos simplemente se le asigna 0 a la variable acompañamientos
    def encontrar_precio_total(self) -> float:
        return self.precio + (self.acompañamientos * 2.5)

 # Ahora definimos la clase Order, la cual contendrá los métodos para
 # agregar elementos al pedido y encontrar el total.
class Order:

    #* Aqui definimos un atributo, en este caso una lista vacia la cual
    #* contendrá los elementos del pedido 
    def __init__(self):
        self.items = []

    #* Aqui definimos un método para agregar elementos al pedido, en este caso
    #* con un append los agregamos a la lista de items
    def agregar_item(self, item: MenuItem):
        self.items.append(item)

    #* Aqui definimos un método para encontrar el total del pedido, en este caso
    #* con un for recorremos la lista de items y sumamos el precio total de 
    #* cada uno
    def encontrar_total(self) -> float:
        return sum(item.encontrar_precio_total() for item in self.items)

    #* Aqui definimos un método para aplicar un descuento al total del pedido
    #* en este caso simplemente multiplicamos el total por el porcentaje
    def aplicar_descuento(self, porcentaje: float) -> float:

        #* En este caso creamos la variable total la cual tendra lo que resulto
        #*  del metodo encontrar_total
        total = self.encontrar_total()
        return total - (total * (porcentaje / 100))


# Aqui tenemos un ejemplo de uso de estas clases
if __name__ == "__main__":

    #* Aqui creamos Algunos de los elementos del menú
    bebida1 = Bebida("Coca Cola", 8.0, "Grande")
    bebida2 = Bebida("Jugo de Naranja", 3.5, "Mediano")
    bebida3 = Bebida("Agua", 1.0, "Pequeño")
    bebida4 = Bebida("Cerveza", 4.0, "Mediano")
    aperitivo1 = Aperitivo("Papas Francesas", 1.5, 2)
    aperitivo2 = Aperitivo("Alitas de Pollo", 5.0, 1)
    aperitivo3 = Aperitivo("Nachos", 4.0, 3)
    aperitivo4 = Aperitivo("Taquitos", 3.5, 1)
    plato1 = PlatoPrincipal("Hamburguesa", 18.0, 2)
    plato2 = PlatoPrincipal("Pizza", 15.0, 1)
    plato3 = PlatoPrincipal("Mojarra", 17.0, 0)
    plato4 = PlatoPrincipal("Churrasco", 16.0, 1)

    # Aqui creamos un pedido y agregamos los elementos
    pedido = Order()
    pedido.agregar_item(bebida1)
    pedido.agregar_item(bebida2)
    pedido.agregar_item(aperitivo1)
    pedido.agregar_item(aperitivo2)
    pedido.agregar_item(plato1)
    pedido.agregar_item(plato2)

    # Aqui ya definimos el total del pedido y lo imprimimos
    total = pedido.encontrar_total()
    print(f"Total sin descuento: ${total:.2f}")

    # Aqui aplicamos un descuento del 10% y lo imprimimos
    total_con_descuento = pedido.aplicar_descuento(10)  # 10% de descuento
    print(f"Total con descuento: ${total_con_descuento:.2f}") 