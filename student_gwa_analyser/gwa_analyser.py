def find_top_student():
    # Ask user for file name
    file_name = input("Enter file name: ")
    try:
        # Read file contents
        with open(file_name, "r") as file:
            students = []
            # Process each line
            for line_number, line in enumerate(file, 1):
                clean_line = line.strip()
                # skip empty lines
                if clean_line == "":
                    continue
                parts = clean_line.split()
                if len(parts) < 2:
                    print(f"Skipped invalid format at line {line_number}")
                    continue
                try:
                    # Extract name and GWA
                    name = " ".join(parts[:-1])
                    gwa = float(parts[-1])
                    # Store as tuple
                    students.append((name, gwa))
                except ValueError:
                    print(f"Invalid GWA at line {line_number}")
                    continue
            # Check if list is not empty
            if students:
                # Find student with lowest GWA (best)
                best_student = min(students, key=lambda x: x[1])
                print("\nTop Student:")
                print("Name:", best_student[0])
                print("GWA:", f"{best_student[1]:.2f}")
            else:
                print("No valid records found.")
    except FileNotFoundError:
        print("File does not exist.")
    except Exception as error:
        print("Unexpected error:", error)
# Run program
if __name__ == "__main__":
    find_top_student()