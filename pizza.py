

class Pizza:

    precio = 10000
    tamaño = "familiar"

    tipo_masa = {
        1: "tradicional",
        2: "delgada"
    }

    ingredientes_vegetales ={
        1: {"tomate"},
        2: {"aceitunas"},
        3: {"champiñones"}
    }
    ingredientes_proteicos = {
        1: {"pollo"},
        2: {"carne"},
        3: {"carne vegetal"}
    }

    """validador"""
    validador_masa = list(tipo_masa.values())
    validador_vegetales = list(ingredientes_vegetales)
    validador_proteicos = list(ingredientes_proteicos)

    def __init__(self):
        self.ingredientes_proteicos= None
        self.ingredientes_vegetales_seleccionados = []
        self.tipo_masa = None
        self.valido =False

    @staticmethod
    def validar_elemento(elemento, opciones):
        return elemento in opciones
    