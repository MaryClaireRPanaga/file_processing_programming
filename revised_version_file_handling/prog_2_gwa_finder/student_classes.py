class Student:
    """Represents an individual student with a name and GWA."""
    def __init__(self, name: str, gwa: float):
        self.name = name
        self.gwa = gwa
class StudentAnalyzer:
    """Handles reading student data from files and analyzing records."""
    def __init__(self):
        self.students = []
    def load_students_from_file(self, file_name: str) -> bool:
        """Reads and parses student records from the given file path."""
        try:
            with open(file_name, "r") as file:
                for line in file:
                    # Strip spaces and clean up inline commas
                    clean_line = line.strip().replace(",", " ")
                    if not clean_line:
                        continue
                    parts = clean_line.split()
                    if len(parts) < 2:
                        continue
                    try:
                        name = " ".join(parts[:-1])
                        gwa = float(parts[-1])
                        self.students.append(Student(name, gwa))
                    except ValueError:
                        continue
            return True        
        except FileNotFoundError:
            return False
        except Exception:
            return False
    def get_top_student(self) -> Student:
        """Returns the student with the lowest numerical GWA (highest rank)."""
        if not self.students:
            return None
        return min(self.students, key=lambda student: student.gwa)
    def display_top_student(self):
        """Prints exclusively the single required output line."""
        top_student = self.get_top_student()
        if top_student:
            print(f"Student with Highest GWA: {top_student.name}, {top_student.gwa:.2f}")