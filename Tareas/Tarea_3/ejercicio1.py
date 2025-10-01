import sys


def binarioToDecimal(n):
    if n == 0 or n == 1:
        return n
    
    # último dígito
    ultimo_digito = n % 10
    
    # Quitar último dígito
    resto = n // 10 
    return ultimo_digito + 2 * binarioToDecimal(resto)

def main():
    n = int(sys.argv[1])
    print(binarioToDecimal(n))

if __name__ == "__main__":
    main()
