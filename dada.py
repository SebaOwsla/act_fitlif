# Crear un diccionario vacío para almacenar las traducciones
diccionario_traduccion = {}

# Solicitar al usuario que ingrese las palabras en español e inglés hasta que ingrese una cadena vacía
print("Ingrese las palabras en español e inglés (deje vacío para terminar):")
while True:
    palabra_espanol = input("Palabra en español: ")
    if palabra_espanol == "":
        break
    palabra_ingles = input("Palabra en inglés: ")
    diccionario_traduccion[palabra_espanol] = palabra_ingles

# Solicitar al usuario que ingrese una frase en español
frase_espanol = input("Ingrese una frase en español: ")

# Dividir la frase en palabras
palabras = frase_espanol.split()

# Traducir cada palabra de la frase si está presente en el diccionario, de lo contrario, dejarla sin traducir
frase_traducida = []
for palabra in palabras:
    if palabra in diccionario_traduccion:
        frase_traducida.append(diccionario_traduccion[palabra])
    else:
        frase_traducida.append(palabra)

# Unir las palabras traducidas o sin traducir en una frase
frase_traducida = " ".join(frase_traducida)

# Mostrar la frase traducida
print("Frase traducida:", frase_traducida)
