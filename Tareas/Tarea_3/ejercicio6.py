import sys

def permutaciones(cadena):
    if len(cadena) <= 1:
        return [cadena]
    
    resultado = []
    
    for i, caracter in enumerate(cadena):
        resto = cadena[:i] + cadena[i+1:]
        
        for p in permutaciones(resto):
            resultado.append(caracter + p)
    
    return resultado

def main():
    cadena = sys.argv[1]
    resultado = permutaciones(cadena)
    print(resultado)

if __name__ == "__main__":
    main()