import sys

def invertir_numero(n, invertido=0):
    if n == 0:
        return invertido
    else:
#        print(n // 10)
#        print(f"El valor de invertido * 10 + n % 10 es: {invertido * 10 + n % 10}")
#        print(f"El valor de invertido * 10 es: {invertido * 10}")
#        print(f"El valor de n % 10 es: {n % 10}")
        return invertir_numero(n // 10, invertido * 10 + n % 10)

def main():
    n = int(sys.argv[1])
    print(invertir_numero(n))
            
if __name__ == "__main__":
    main()