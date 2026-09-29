import csv
from file_processor import FileProcessor
from student import Student

class CSVProcessor(FileProcessor):
    def read_file(self, file_path):
        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                student = Student(
                    rollnumber=row['roll_number'],
                    fullname=row['ten'],
                    dob=row['dob']
                )
                self.student_list.append(student)