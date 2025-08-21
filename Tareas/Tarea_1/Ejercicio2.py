import pickle

# Function to save data to a binary file
def save_bin(data, filename="Tarea/data.dat"):
    with open(filename, "wb") as f:
        pickle.dump(data, f)
    print("Data saved to binary file.")

# Function to load data from a binary file
def load_bin(filename="Tarea/data.dat"):
    try:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            return data
    except FileNotFoundError:
        print("No data file found.")
        return []

if __name__ == "__main__":
    # List of dictionaries key-value pairs
    lista_diccionarios = [
        {"a":"10", "b":"20"},
        {"c":"30", "d":"40"},
        {"e":"50", "f":"60"}
    ]
    save_bin(lista_diccionarios)
    data = load_bin()
    print("Loaded Data:")
    
    for i, dictionary in enumerate(data):
        print(f"Dictionary {i+1}: {dictionary}")
        
    # More ways to print the loaded data
    '''
    for item in data:
        for key, value in item.items():
          print(f"{key} - {value}")

    for i, dictionary in enumerate(data):
        print(f"Dictionary {i+1}:")
        for key, value in dictionary.items():
            print(f"  Key: {key}, Value: {value}")
      
    for i,item in enumerate(data):
        print(f"{item} - {i+1}")
        '''

        
