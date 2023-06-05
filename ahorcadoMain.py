import moduloDibujosAhorcado
import moduloAhorcado

palabraSecreta = moduloAhorcado.seleccionarPalabraAdivinar()
contadorErrores=0
letrasProbadas=[]
letrasAdivinadas=[]

while True:
    if contadorErrores == 0:
        moduloDibujosAhorcado.error0()
        moduloAhorcado.lineasPalabraSecretaGanador(palabraSecreta,letrasAdivinadas)
        contadorErrores=moduloAhorcado.pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores)
    elif contadorErrores == 1:
        moduloDibujosAhorcado.error1()
        moduloAhorcado.lineasPalabraSecretaGanador(palabraSecreta,letrasAdivinadas)
        contadorErrores=moduloAhorcado.pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores)
    elif contadorErrores == 2:
        moduloDibujosAhorcado.error2()
        moduloAhorcado.lineasPalabraSecretaGanador(palabraSecreta,letrasAdivinadas)
        contadorErrores=moduloAhorcado.pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores)
    elif contadorErrores == 3:
        moduloDibujosAhorcado.error3()
        moduloAhorcado.lineasPalabraSecretaGanador(palabraSecreta,letrasAdivinadas)
        contadorErrores=moduloAhorcado.pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores)
    elif contadorErrores == 4:
        moduloDibujosAhorcado.error4()
        moduloAhorcado.lineasPalabraSecretaGanador(palabraSecreta,letrasAdivinadas)
        contadorErrores=moduloAhorcado.pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores)
    elif contadorErrores == 5:
        moduloDibujosAhorcado.error5()
        moduloAhorcado.lineasPalabraSecretaGanador(palabraSecreta,letrasAdivinadas)
        contadorErrores=moduloAhorcado.pedirLetra(palabraSecreta,letrasAdivinadas,letrasProbadas,contadorErrores)
    elif contadorErrores == 6:
        moduloDibujosAhorcado.error6()