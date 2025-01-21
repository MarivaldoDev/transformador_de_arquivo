from tkinter import messagebox
from pdf2docx import Converter
import win32com.client
from docx2pdf import convert
from PIL import Image


def pdf_to_word(pdf_file, word_file):
    converter = Converter(pdf_file)
    try:
        converter.convert(word_file, start=0, end=None)
    except:
       messagebox.showerror("Erro!", "Algo deu errado!")
    else:
        messagebox.showinfo("Sucesso!", "Arquivo convertido para docx")
        converter.close()
    
    
def word_to_pdf(word_file, pdf_file):
   try:
    convert(word_file, pdf_file)
   except:
      messagebox.showerror("Erro!", "Algo deu errado!")
   else:
       messagebox.showinfo("Sucesso!", "Arquivo convertido para pdf")


def jpg_to_pdf(jpg_file, pdf_file):
    image = Image.open(jpg_file)

    try:
        image.save(pdf_file)
    except:
        messagebox.showerror("Erro!", "Algo deu errado!")
    else:
        messagebox.showinfo("Sucesso!", "Arquivo convertido para pdf")


def excel_to_pdf(excel_file, pdf_file):
    # Inicia o aplicativo Excel
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = False  # Não exibe o Excel durante a execução

    # Abre o arquivo Excel
    workbook = excel.Workbooks.Open(excel_file)

    try:
        # Exporta para PDF
        workbook.ExportAsFixedFormat(
            Type=0,  # 0 indica PDF
            Filename=pdf_file,
            Quality=0,  # Qualidade padrão
            IncludeDocProperties=True,
            IgnorePrintAreas=False,
            OpenAfterPublish=False  # Não abre o PDF após salvar
        )
        messagebox.showinfo("Sucesso!", "Arquivo convertido para pdf")
    except Exception as e:
        print(f"Erro ao converter Excel para PDF: {e}")
    finally:
        # Fecha o workbook e encerra o Excel
        workbook.Close(False)
        excel.Quit()