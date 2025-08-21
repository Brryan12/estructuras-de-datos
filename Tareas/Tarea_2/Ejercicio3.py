import json
import sys

def insertar_vip(fila, cliente):
    # Buscar el primer cliente que NO sea VIP
    for i, persona in enumerate(fila):
        if persona['tipo'] != 'VIP':
            fila.insert(i, cliente)
            return
    # Si solo hay VIPs (o lista vacía), agregar al final
    fila.append(cliente)

def insertar_norm(fila, cliente):
    # Buscar el primer BULK
    for i, persona in enumerate(fila):
        if persona['tipo'] == 'BULK':
            fila.insert(i, cliente)
            return
    # Si no hay BULK, agregar al final
    fila.append(cliente)

def procesar(clientes):
    lista = []
    
    for cliente in clientes:
        if cliente['tipo'] == 'VIP':
            insertar_vip(lista, cliente)
        elif cliente['tipo'] == 'NORM':
            insertar_norm(lista, cliente)
        elif cliente['tipo'] == 'BULK':
            # BULK siempre al final absoluto
            lista.append(cliente)
    
    return lista

def main():    
    json_file = sys.argv[1]
    
    try:
        with open(json_file, 'r') as f:
            clientes = json.load(f)
        
        # Procesar la lista según las reglas
        orden_final = procesar(clientes)
        
        # Imprimir el orden final (solo nombres)
        nombres = [cliente['nombre'] for cliente in orden_final]
        print(' '.join(nombres))
        
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{json_file}'")
        sys.exit(1)

if __name__ == "__main__":
    main()  