from pdf2docx import Converter
from docx import Document
from docx2pdf import convert


def pdf_to_word(pdf_file, word_file):
    converter = Converter(pdf_file)
    converter.convert(word_file, start=0, end=None)
    
    converter.close()
    
    print(f"Arquivo convertido para word: {word_file}")


def word_to_pdf(word_file, pdf_file):
   convert(word_file, pdf_file)

   print(f"Arquivo convertido para PDF: {pdf_file}")


# word_to_pdf("documents/grupo primeiro de maio.docx", "documents/teste.pdf")
pdf_to_word("documents/profile.pdf", "documents/teste.docx")