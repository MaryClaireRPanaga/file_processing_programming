class MyLife:
    def __init__(self, filename):
        self.filename = filename
    def write_lines(self):
        try:
            with open(self.filename, "w") as file:
                while True:
                    line = input("Enter line: ")
                    file.write(line + "\n")
                    choice = input("Are there more lines y/n? ").lower()
                    if choice == 'n':
                        break
            print("Data successfully written to", self.filename)
        except Exception as e:
            print("Error:", e)