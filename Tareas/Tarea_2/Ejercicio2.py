import json
import sys

def tiempo_a_minutos(tiempo_str):
    """Convierte tiempo en formato HH:MM a minutos"""
    horas_str, minutos_str = tiempo_str.split(':')
    horas = int(horas_str)
    minutos = int(minutos_str)
    return horas * 60 + minutos

def minutos_a_tiempo(minutos):
    """Convierte minutos a formato HH:MM"""
    horas = minutos // 60
    mins = minutos % 60
    return f"{horas:02d}:{mins:02d}"

def comprimir_eventos(eventos):
    """Comprime eventos consecutivos de la misma sala."""
    if not eventos:
        return []
    
    resultado = []
    
    for evento in eventos:
        if not resultado:
            resultado.append(evento.copy())
        else:
            ultimo = resultado[-1]
            
            # Convertir tiempos
            ultimo_fin = tiempo_a_minutos(ultimo['inicio']) + ultimo['duracion']
            evento_inicio = tiempo_a_minutos(evento['inicio'])

            # Fusionar si se puede
            if ultimo['sala'] == evento['sala'] and ultimo_fin == evento_inicio:
                resultado[-1]['duracion'] += evento['duracion']
            else:
                resultado.append(evento.copy())
    
    return resultado

def main():    
    json_file = sys.argv[1]
    
    try:
        # Leer el archivo JSON
        with open(json_file, 'r') as f:
            eventos = json.load(f)
        
        # Comprimir los eventos
        eventos_comprimidos = comprimir_eventos(eventos)
        
        # Imprimir el resultado como JSON
        print(json.dumps(eventos_comprimidos, indent=2))
        
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{json_file}'")
        sys.exit(1)

if __name__ == "__main__":
    main()