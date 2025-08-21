import time

# Create a large text file for testing
with open("Tarea/large_text.txt", "w") as f:
    for _ in range(228000):  # ~10MB total
        f.write("The quick brown fox jumps over the lazy dog.\n")

#file path of the large text file
file_path = "Tarea/large_text.txt"

# Function to read the file character by character
def read_file_char():
    try:
        with open(file_path, "r") as file:
            while True:
                char = file.read(1)
                if not char:
                    break
                print(char)

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")

# Function to read the file line by line
def read_file_line():
    try:
        with open(file_path, "r") as file:
            for line in file:
                print(line, end="")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")

# Function to read the file bytes
def read_file_bytes():
    try:
        with open(file_path, "rb") as file:
            byte_size = 4096
            while True:
                chunk =  file.read(byte_size)
                if not chunk:
                    break
                #print(f"Read chunk of {len(chunk)} bytes:")
                print(chunk.decode('utf-8', errors='ignore'))  # Decode to text, handling errors

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")

if __name__ == "__main__":
    start_time = time.perf_counter()
    read_file_char()
    charBychar = f"Execution time of char by char: {time.perf_counter() - start_time:.2f} seconds"

    start_time = time.perf_counter()
    read_file_line()
    lineByline = f"Execution time of line by line: {time.perf_counter() - start_time:.2f} seconds"

    start_time = time.perf_counter()
    read_file_bytes()
    byteChunk = f"Execution time of byte chunk: {time.perf_counter() - start_time:.2f} seconds"

    print(charBychar)
    print(lineByline)     
    print(byteChunk) 