import PyPDF2
from src.logger import logging

# Reading the input data file
def read_input_file(file_name):
    # checking the file type
    if file_name.name.endswith(".pdf"):
        # Input file is a PDF
        try:
            # Reading the PDF file
            pdf_reader = PyPDF2.PdfFileReader(file_name)
            text = ""
            # Extracting text from each page and adding to text
            for page in pdf_reader.pages:
                text += page.extract_text()
            del pdf_reader
            logging.info('Input PDF file was raed')
            return text
        except:
            raise Exception("Error while reading input PDF file.")
    elif file_name.name.endswith(".txt"):
        # Input file is a text
        logging.info('Input Text file was raed')
        return file_name.read().decode('utf-8')
    else:
        # raise exception
        raise Exception("Unsupported file format. Only PDF and Text files are supported.")