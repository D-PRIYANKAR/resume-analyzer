# import PyPDF2

# def extract_text_from_pdf(file_path):
#     text = ""
#     with open(file_path, "rb") as file:
#         reader = PyPDF2.PdfReader(file)
#         for page in reader.pages:
#             content = page.extract_text()
#             if content:
#                 text += content
#     return text

import pdfplumber

def extract_text_from_pdf(file_path):
    text = ""
    
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content
    
    return text