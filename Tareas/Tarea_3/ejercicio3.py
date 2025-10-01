import sys

def division_recursiva(dividendo, divisor):

    if dividendo < divisor:
        return 0
    
    if dividendo == divisor:
        return 1
    
    return 1 + division_recursiva(dividendo - divisor, divisor)


def main():    
    dividendo = int(sys.argv[1])
    divisor = int(sys.argv[2])
    
    if divisor == 0:
        print("Error: No se puede dividir por cero")
        return
    
    resultado = division_recursiva(dividendo, divisor)
    print(resultado)


if __name__ == "__main__":
    main()