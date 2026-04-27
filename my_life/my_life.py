# Class that handles writing multiple lines to a file
class MyLife:
    def __init__(self, filename):
        self.filename = filename
    def write_lines(self):
        try:
            # Open file in write mode
            with open(self.filename, "w") as file:
                while True:
                    # Ask user for input
                    line = input("Enter line: ")
                    file.write(line + "\n")
                    # Ask if user wants to continue
                    choice = input("Are there more lines y/n? ").lower()
                    if choice == 'n':
                        break
            print("Data successfully written to", self.filename)
        except Exception as e:
            print("Error:", e)
# Run Test
def main():
    writer = MyLife("mylife.txt")
    writer.write_lines()
main()