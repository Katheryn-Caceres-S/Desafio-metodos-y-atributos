from pizza import Pizza

# a. Mostrar atributos de clase
print("Ingredientes vegetales disponibles:", list(Pizza.ingredientes_vegetales.values()))
print("Ingredientes proteicos disponibles:", list(Pizza.ingredientes_proteicos.values()))
print("Tipos de masa disponibles:", list(Pizza.tipo_masa.values()))

# b. Validar si "salsa de tomate" está en la lista
resultado = Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"])
print("¿'Salsa de tomate' está en la lista?:", resultado)

# c. Crear una instancia y realizar un pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d. Mostrar resumen del pedido
print("Resumen del pedido:")
print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
print("Ingredientes vegetales:", mi_pizza.ingredientes_vegetales_seleccionados)
print("Tipo de masa:", mi_pizza.tipo_masa)
print("¿Pizza válida?:", mi_pizza.valida)

# e. Intentar mostrar atributo de instancia desde la clase (provocará error controlado)
print("Prueba de acceso inválido al atributo 'valida' desde la clase (debe generar error):")
try:
    print(Pizza.valida)
except AttributeError:
    print("Error: no se puede acceder a 'valida' desde la clase, solo desde una instancia.")