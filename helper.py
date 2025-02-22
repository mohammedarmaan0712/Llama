import PyPDF2
import os

def parce_pdf_to_text(pdf_name):
    # Check if pdf_name.txt exists:
   ''' if not (os.path.exists(pdf_name+".pdf")):
        raise ValueError("PDF name should refer to a file in the project directory.")  # Custom error message

    filename = pdf_name+".txt"

    if os.path.exists(filename):
        with open(filename, "a", encoding="utf-8") as file:
            #Locate PDF
            with open(pdf_name+".pdf", "rb") as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    file.write(page.extract_text())
    else:
        with open(filename, "w", encoding="utf-8") as file:
            #Locate PDF
            with open(pdf_name+".pdf", "rb") as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    file.write(page.extract_text())'''
   filename = pdf_name+".txt"
   try:
       with open(pdf_name+".pdf", "rb") as pdf_file:
            with open(filename, return_open_mode_for_txt_files(filename), encoding="utf-8") as file:
                 reader = PyPDF2.PdfReader(pdf_file)
                 for page_num in range(len(reader.pages)):
                     page = reader.pages[page_num]
                     file.write(page.extract_text())
   except FileNotFoundError:
       print(f"Error: The file '{pdf_name}' was not found.")
       return

def return_open_mode_for_txt_files(filename):
    if os.path.exists(filename):
        return 'a'
    else:
        return 'w'
