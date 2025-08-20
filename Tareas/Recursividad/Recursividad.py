import sys
import math
def Imprimir(n):
    if(n<1):
        return
    else:
        print(f"Llamada : {n}")
        Imprimir(n-1)


def Sumatoria(n):
    if(n==1):
        return 1
    else:
        return n + Sumatoria(n-1)

def Factorial(n):
    if(n<=1):
        return 1
    else:
        return n * Factorial(n-1)
    
def CantLetras(Palabra):
    if Palabra == "":
        return 0
    else: return 1 + CantLetras(Palabra[1:])


def main():
    # Verificar si hay suficientes argumentos
    if len(sys.argv) < 2:
        print("Uso: python Recursividad.py <modo> <numero|palabra>")
        print("Modos disponibles: 1(imprimir), 2(sumatoria), 3(factorial), 4(contar letras)")
        return
    
    # Obtener el modo
    modo = sys.argv[1]
    
    try:
        # Verificar si hay suficientes argumentos
        if len(sys.argv) < 3:
            print(f"El modo {modo} requiere un argumento adicional")
            return
            
        # Ejecutar la función según el modo
        if modo == "1":
            numero = int(sys.argv[2])
            Imprimir(numero)
        elif modo == "2":
            numero = int(sys.argv[2])
            resultado = Sumatoria(numero)
            print(f"Sumatoria de {numero} = {resultado}")
        elif modo == "3":
            numero = int(sys.argv[2])
            resultado = Factorial(numero)
            print(f"Factorial de {numero} = {resultado}")
        elif modo == "4":
            palabra = sys.argv[2]  # Usar el segundo argumento como palabra
            resultado = CantLetras(palabra)
            print(f"Número de letras en '{palabra}' = {resultado}")
        else:
            print(f"Modo '{modo}' no reconocido")
            print("Modos disponibles: 1(imprimir), 2(sumatoria), 3(factorial), 4(contar letras)")
    
    except ValueError:
        # Si hay error al convertir a entero y estamos en modo 4, tratar como palabra
        if modo == "4":
            palabra = sys.argv[2]
            resultado = CantLetras(palabra)
            print(f"Número de letras en '{palabra}' = {resultado}")
        else:
            print("Por favor, ingrese un número entero válido para los modos 1, 2 y 3.")

if __name__ == "__main__":
    main()