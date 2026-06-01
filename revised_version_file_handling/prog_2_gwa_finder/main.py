import os
from student_classes import StudentAnalyzer 
def main():
    # Changed from "students.txt" to "class_file.txt" to match your actual file name
    file_path = "class_file.txt"
    analyzer = StudentAnalyzer()
    if analyzer.load_students_from_file(file_path):
        analyzer.display_top_student()
    else:
        # Looks inside the subfolder if the terminal path is pointing at the parent directory
        parent_file_path = os.path.join("prog_2_gwa_finder", "class_file.txt")
        if analyzer.load_students_from_file(parent_file_path):
            analyzer.display_top_student()
if __name__ == "__main__":
    main()