cesta_compra = {}

while True:

    print(f"""
    |  Cesta de compra |
    |==================|
    """)

    producto = input('ingrese el nombre del producto (deje en blanco para terminar) : ')
    if producto == '':
        break
    precio = float(input('ingrese el precio del producto : '))
    cesta_compra[producto] = precio

print("Lista de la compra:")
total = 0

for articulo, precio in cesta_compra.items():
    print(f"""
    |  Cesta de compra |
    |==================|
    """)
    print(f'{producto}:          ${precio}')
    total += precio
    print('Costo total: ${:.2f}'.format(total))