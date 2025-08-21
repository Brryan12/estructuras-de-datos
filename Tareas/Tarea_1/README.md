# 📘 Data Structures Course – 1st assingment 
## Bryan Aguero Mata - 402690986

## Exercises

### Exercise 1: File Reading Methods Comparison

This exercise demonstrates and compares three different methods for reading files:

1. **Character-by-Character Reading**: Reads one character at a time.
   - Slowest method due to high number of file operations
   - Simple implementation

2. **Line-by-Line Reading**: Reads one line at a time.
   - More efficient than character-by-character reading
   - Uses the `end=""` parameter to prevent double line breaks in output

3. **Chunk-based Reading**: Reads the file in larger byte chunks.
   - Fastest method
   - Most memory efficient for large files
   - Uses buffered reading approach

The program creates a large text file (~10MB) for testing and measures the execution time of each method.

### Exercise 2: Binary File Storage for Data Structures

This exercise demonstrates how to store and retrieve Python data structures using binary files:

- Saves a list of dictionaries to a binary file using pickle
- Retrieves the data structure from the file
- Demonstrates various ways to access and manipulate the data

## Usage

Run each exercise file directly with Python:

```bash
python Ejercicio1.py  # For file reading methods comparison
python Ejercicio2.py  # For binary file storage example