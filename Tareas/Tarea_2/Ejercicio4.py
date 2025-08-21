import json
import sys

def invertir_comando(comando):
    if comando['cmd'] == 'MOVE':
        return f"MOVE_BACK x {comando['x']}"
    elif comando['cmd'] == 'TURN_LEFT':
        return "TURN_RIGHT"
    elif comando['cmd'] == 'TURN_RIGHT':
        return "TURN_LEFT"
    return None

def procesar_comandos(comandos):
    pila_acciones = []
    
    for comando in comandos:
        if comando['cmd'] == 'RETURN':
            # Procesar el retorno: sacar de la pila en orden inverso
            acciones_retorno = []
            while pila_acciones:
                accion = pila_acciones.pop()  # Extrae el último (LIFO)
                accion_inversa = invertir_comando(accion)
                if accion_inversa:
                    acciones_retorno.append(accion_inversa)
            return acciones_retorno
        
        elif comando['cmd'] in ['MOVE', 'TURN_LEFT', 'TURN_RIGHT']:
            pila_acciones.append(comando)
        
        elif comando['cmd'] == 'DROP':
            pass
    
    # Si no hay RETURN, retornar lista vacía
    return []

def main():    
    json_file = sys.argv[1]
    
    try:
        with open(json_file, 'r') as f:
            comandos = json.load(f)
        
        # Procesar comandos y obtener secuencia de retorno
        acciones_retorno = procesar_comandos(comandos)
        
        # Imprimir cada acción de retorno
        for accion in acciones_retorno:
            print(accion)
        
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{json_file}'")
        sys.exit(1)

if __name__ == "__main__":
    main()  