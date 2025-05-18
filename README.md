# Reto_3

```mermaid
classDiagram
    class MenuItem {
        -nombre: str
        -precio: float
        +encontrar_precio_total(): float
    }

    class Bebida {
        -tamaño: str
        +encontrar_precio_total(): float
    }

    class Aperitivo {
        -porciones: int
        +encontrar_precio_total(): float
    }

    class PlatoPrincipal {
        -acompañamientos: int
        +encontrar_precio_total(): float
    }

    class Order {
        -items: List~MenuItem~
        +agregar_item(item: MenuItem)
        +encontrar_total(): float
        +aplicar_descuento(porcentaje: float): float
    }

    MenuItem <|-- Bebida
    MenuItem <|-- Aperitivo
    MenuItem <|-- PlatoPrincipal
    Order --> "1..*" MenuItem : agrega
