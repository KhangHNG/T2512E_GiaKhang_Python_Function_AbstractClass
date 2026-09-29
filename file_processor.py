from abc import abstractmethod

class FileProcessor:
    student_list = []
    
    def __init__(self):
        pass

    def print_student_list(self):
        for student in self.student_list:
            print(student)

    @abstractmethod
    def read_file(self, file_path):
        pass