import random

def seleccionarPalabraAdivinar():
    palabras=["uno","dos","tres"]
    numeroRandom=random.randint(0,len(palabras)-1)
    return palabras[numeroRandom]
