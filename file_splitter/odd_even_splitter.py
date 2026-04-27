# Handles separating even and odd numbers from a file
class EvenOddProcessor:
    # Constructor
    def __init__(self, filename):
        self.filename = filename
    # Performs all operations
    def separate_numbers(self):
        try:
            # Read numbers from file
            with open(self.filename, "r") as file:
                numbers = [int(line.strip()) for line in file]
            # Optional check if exactly 20 integers
            if len(numbers) != 20:
                print(f"Warning: Expected 20 numbers, found {len(numbers)}")
            # Lists to store even and odd numbers
            even_numbers = []
            odd_numbers = []
            # Separate numbers
            for num in numbers:
                if num % 2 == 0:
                    even_numbers.append(num)
                else:
                    odd_numbers.append(num)
            # Write even numbers to even.txt
            with open("even.txt", "w") as even_file:
                for num in even_numbers:
                    even_file.write(str(num) + "\n")
            # Write odd numbers to odd.txt
            with open("odd.txt", "w") as odd_file:
                for num in odd_numbers:
                    odd_file.write(str(num) + "\n")
            print("Done! Numbers have been separated into even.txt and odd.txt.")
        # Error handling if file not found
        except FileNotFoundError:
            print("Error: numbers.txt file not found.")
        # Error handling if data is not integer
        except ValueError:
            print("Error: Make sure all lines in numbers.txt are integers.")
# Test Driver (main program)
def main():
    processor = EvenOddProcessor("numbers.txt")
    processor.separate_numbers()
# Run the program
main()