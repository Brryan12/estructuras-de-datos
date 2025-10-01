import sys

def contar_ocurrencias(texto, caracter):
    if len(texto) == 0:
        return 0
    
    primer_caracter = texto[0]
    resto_texto = texto[1:]
    
    if primer_caracter == caracter:
        return 1 + contar_ocurrencias(resto_texto, caracter)
    else:
        return contar_ocurrencias(resto_texto, caracter)


def main():
    texto = sys.argv[1]
    caracter = sys.argv[2]    
    resultado = contar_ocurrencias(texto, caracter)
    print(resultado)


if __name__ == "__main__":
    main()