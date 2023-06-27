import random

def seleccionarPalabraAdivinar():
  palabras=["uno","dos","tres"]
  return random.choice(palabras)


def generarCadena(palabraSecreta,letrasAdivinadas):
  cadena=[]
  for letra in palabraSecreta:
    if letra in letrasAdivinadas:
      cadena.append(letra)
    else:
      cadena.append("_")
  return cadena


def verficarSiYaGano(cadena,palabraSecreta):
  if "_" not in cadena:
    print(f"Ganaste, has adivinado la palabra secreta:{palabraSecreta}")
    exit()


def lineasPalabraSecreta(cadena):
    strCadena="".join(cadena)
    for letra in strCadena:
        print(letra,end=" ")
    print("\n")


def pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores):
  letra=input("Ingresa una letra:")
  if letra in letrasProbadas or letra not in palabraSecreta:
    return contadorErrores+1
  else:
    letrasAdivinadas.append(letra)
    letrasProbadas.append(letra)
    return contadorErrores