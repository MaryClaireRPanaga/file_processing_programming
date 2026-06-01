class NumberProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.even_file = "even.txt"
        self.odd_file = "odd.txt"
    def separate_numbers(self):
        even_numbers = []
        odd_numbers = []
        try:
            with open(self.input_file, "r") as file:
                for line in file:
                    number = int(line.strip())
                    if number % 2 == 0:
                        even_numbers.append(str(number))
                    else:
                        odd_numbers.append(str(number))
            with open(self.even_file, "w") as even:
                even.write("\n".join(even_numbers))
            with open(self.odd_file, "w") as odd:
                odd.write("\n".join(odd_numbers))
            print("Done!")
            print("Even:", even_numbers)
            print("Odd:", odd_numbers)
        except Exception as error:
            print("Error:", error)