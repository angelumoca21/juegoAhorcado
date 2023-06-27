import moduloDibujosAhorcado
import moduloAhorcado
import os

palabraSecreta = moduloAhorcado.seleccionarPalabraAdivinar()
contadorErrores=0
letrasProbadas=[]
letrasAdivinadas=[]
avanceActualPalabra=[]

while True:
  if contadorErrores == 0:
    avanceActualPalabra=moduloAhorcado.generarCadena(palabraSecreta,letrasAdivinadas)
    moduloAhorcado.verficarSiYaGano(avanceActualPalabra,palabraSecreta)
    moduloDibujosAhorcado.error0()
    moduloAhorcado.lineasPalabraSecreta(avanceActualPalabra)
    contadorErrores=moduloAhorcado.pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores)
    os.system ("clear")
  elif contadorErrores == 1:
    avanceActualPalabra=moduloAhorcado.generarCadena(palabraSecreta,letrasAdivinadas)
    moduloAhorcado.verficarSiYaGano(avanceActualPalabra,palabraSecreta)
    moduloDibujosAhorcado.error1()
    moduloAhorcado.lineasPalabraSecreta(avanceActualPalabra)
    contadorErrores=moduloAhorcado.pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores)
    os.system ("clear")
  elif contadorErrores == 2:
    avanceActualPalabra=moduloAhorcado.generarCadena(palabraSecreta,letrasAdivinadas)
    moduloAhorcado.verficarSiYaGano(avanceActualPalabra,palabraSecreta)
    moduloDibujosAhorcado.error2()
    moduloAhorcado.lineasPalabraSecreta(avanceActualPalabra)
    contadorErrores=moduloAhorcado.pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores)
    os.system ("clear")
  elif contadorErrores == 3:
    avanceActualPalabra=moduloAhorcado.generarCadena(palabraSecreta,letrasAdivinadas)
    moduloAhorcado.verficarSiYaGano(avanceActualPalabra,palabraSecreta)
    moduloDibujosAhorcado.error3()
    moduloAhorcado.lineasPalabraSecreta(avanceActualPalabra)
    contadorErrores=moduloAhorcado.pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores)
    os.system ("clear")
  elif contadorErrores == 4:
    avanceActualPalabra=moduloAhorcado.generarCadena(palabraSecreta,letrasAdivinadas)
    moduloAhorcado.verficarSiYaGano(avanceActualPalabra,palabraSecreta)
    moduloDibujosAhorcado.error4()
    moduloAhorcado.lineasPalabraSecreta(avanceActualPalabra)
    contadorErrores=moduloAhorcado.pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores)
    os.system ("clear")
  elif contadorErrores == 5:
    avanceActualPalabra=moduloAhorcado.generarCadena(palabraSecreta,letrasAdivinadas)
    moduloAhorcado.verficarSiYaGano(avanceActualPalabra,palabraSecreta)
    moduloDibujosAhorcado.error5()
    moduloAhorcado.lineasPalabraSecreta(avanceActualPalabra)
    contadorErrores=moduloAhorcado.pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores)
    os.system ("clear")
  elif contadorErrores == 6:
    moduloDibujosAhorcado.error6()