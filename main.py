from file_processor import FileProcessor
from csv_processor import CSVProcessor
from excel_processor import ExcelProcessor

if __name__ == "__main__":
    processor: FileProcessor = None
    print("Input file path")
    file_path = input().strip()
    print(f"File path entered: {file_path}")
    if file_path.endswith('.csv'):
        processor = CSVProcessor()
    elif file_path.endswith('.xlsx'):
        processor = ExcelProcessor()
    else:
        print("Unsupported file type.")
    processor.read_file(file_path)
    processor.print_student_list()