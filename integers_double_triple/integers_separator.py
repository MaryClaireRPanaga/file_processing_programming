# Handles the processing integers from a source file into separate output files.
class IntegerProcessor:    
    def __init__(self, filename):
        self.filename = filename
    def process_integers(self):
        # Reads integers.txt, calculates squares/cubes, and writes to files.
        try:
            # 1. Read all numbers from the source file
            with open(self.filename, "r") as f:
                # Using a list comprehension to convert lines to integers
                numbers = [int(line.strip()) for line in f]
            # 2. Open both output files simultaneously using 'with'
            with open("double.txt", "w") as double_f, open("triple.txt", "w") as triple_f:
                # 3. Process each number
                for num in numbers:
                    if num % 2 == 0:
                        # Write square of even numbers to double.txt
                        double_f.write(f"{num**2}\n")
                    else:
                        # Write cube of odd numbers to triple.txt
                        triple_f.write(f"{num**3}\n")
            print("P-4 Success: 'double.txt' and 'triple.txt' have been created.")
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
        except ValueError:
            print("Error: The file must contain only integers.")
# Run Test
if __name__ == "__main__":
    processor = IntegerProcessor("integers.txt")
    processor.process_integers()