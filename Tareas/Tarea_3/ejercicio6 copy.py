import sys

def permutaciones(cadena):
    if len(cadena) <= 1:
        return [cadena]
    
    resultado = []
    
    # Tomamos cada carácter como el primero y calculamos las permutaciones del resto
    for i in range(len(cadena)):
        # Carácter actual que será el primero en esta permutación
        caracter_actual = cadena[i]
        
        # Resto de la cadena sin el carácter actual
        resto_cadena = cadena[:i] + cadena[i+1:]
        
        # Calculamos recursivamente las permutaciones del resto de la cadena
        permutaciones_resto = permutaciones(resto_cadena)
        
        # Añadimos el carácter actual al principio de cada permutación del resto
        for p in permutaciones_resto:
            resultado.append(caracter_actual + p)
    
    return resultado

def main():
    
    cadena = sys.argv[1]
    resultado = permutaciones(cadena)
    print(resultado)

if __name__ == "__main__":
    main()