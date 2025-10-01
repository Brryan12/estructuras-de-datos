import sys

def decimalToBinario(n):
    if n == 0 or n == 1:
        return n
    
    return decimalToBinario(n // 2) * 10 + (n % 2)

def main():
    numero = int(sys.argv[1])
    print(decimalToBinario(numero))


if __name__ == "__main__":
    main()