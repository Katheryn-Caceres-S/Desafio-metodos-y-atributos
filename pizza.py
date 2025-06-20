class Pizza:

    precio = 10000
    tamaño = "familiar"

    tipo_masa = {
        1: "tradicional",
        2: "delgada"
    }

    ingredientes_vegetales = {
        1: "tomate",
        2: "aceitunas",
        3: "champiñones"
    }

    ingredientes_proteicos = {
        1: "pollo",
        2: "carne",
        3: "carne vegetal"
    }

    def __init__(self):
        self.ingrediente_proteico = None
        self.ingredientes_vegetales_seleccionados = []
        self.tipo_masa = None
        self.valida = False

    @staticmethod
    def validar_elemento(elemento, opciones):
        return elemento in opciones

    def realizar_pedido(self):
        print("Menú de ingredientes proteicos:")
        for key, val in Pizza.ingredientes_proteicos.items():
            print(f"{key}. {val}")
        try:
            proteico_opcion = int(input("Selecciona el número del ingrediente proteico: "))
            proteico = Pizza.ingredientes_proteicos[proteico_opcion]
        except (ValueError, KeyError):
            proteico = None

        print("\nMenú de ingredientes vegetales:")
        for key, val in Pizza.ingredientes_vegetales.items():
            print(f"{key}. {val}")
        try:
            vegetal1_opcion = int(input("Selecciona el número del primer vegetal: "))
            vegetal2_opcion = int(input("Selecciona el número del segundo vegetal: "))
            vegetal1 = Pizza.ingredientes_vegetales[vegetal1_opcion]
            vegetal2 = Pizza.ingredientes_vegetales[vegetal2_opcion]
        except (ValueError, KeyError):
            vegetal1, vegetal2 = None, None

        print("\nTipos de masa disponibles:")
        for key, val in Pizza.tipo_masa.items():
            print(f"{key}. {val}")
        try:
            masa_opcion = int(input("Selecciona el número del tipo de masa: "))
            masa = Pizza.tipo_masa[masa_opcion]
        except (ValueError, KeyError):
            masa = None

        self.ingrediente_proteico = proteico
        self.ingredientes_vegetales_seleccionados = [vegetal1, vegetal2]
        self.tipo_masa = masa

        if proteico and vegetal1 and vegetal2 and masa:
            self.valida = True
            print("\nPedido registrado con éxito:")
            print(f"- Ingrediente proteico: {proteico}")
            print(f"- Ingredientes vegetales: {vegetal1} y {vegetal2}")
            print(f"- Tipo de masa: {masa}")
            print(f"- Tamaño: {Pizza.tamaño}")
            print(f"- Precio: ${Pizza.precio}")
        else:
            self.valida = False
            print("\nPedido inválido. Verifica que todas las opciones sean válidas.")
