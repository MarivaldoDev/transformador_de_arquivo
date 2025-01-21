import os
from customtkinter import *
from tkinter import filedialog
from functions.main import *
from PIL import Image


class Conversor:
    def __init__(self):
        self.window = CTk()
        self.window.title("Conversor de Arquivos")
        self.window.geometry("400x300")
        self.window.iconbitmap("images/logo.ico")
        self.window.resizable(False, False)
        self.options()
        self.window.mainloop()



    def options(self):
        self.option1 = CTkButton(self.window, 
            text='PDF para DOCX', 
            fg_color='red', 
            text_color='white', 
            hover_color='#A52A2A',
            font=('Verdana', 18),
            height=30,
            command=self.window_pdf_to_docx
        )

        self.option2 = CTkButton(self.window, 
            text='DOCX para PDF', 
            fg_color='blue', 
            text_color='white', 
            hover_color='#00008B',
            font=('Verdana', 18),
            height=30,
            command=self.window_docx_to_pdf
        )

        self.option3 = CTkButton(self.window, 
            text='JPG para PDF', 
            fg_color='#008080', 
            text_color='white', 
            hover_color='#2F4F4F',
            font=('Verdana', 18),
            height=30,
            width=155,
            command=self.window_jpg_to_pdf
        )

        self.option4 = CTkButton(self.window, 
            text='XLSX para PDF', 
            fg_color='#2E8B57', 
            text_color='white', 
            hover_color='#006400',
            font=('Verdana', 18),
            height=30,
            width=155,
            command=self.window_xlsx_to_pdf
        )


        self.option1.place(x=125, y=50)
        self.option2.place(x=125, y=100)
        self.option3.place(x=125, y=150)
        self.option4.place(x=125, y=200)
        

    def pdf_to_docx(self):
        caminho_entrada = self.arquivo
        caminho_saida = self.nome_arquivo.replace(".pdf", ".docx")
        
      
        pdf_to_word(caminho_entrada, caminho_saida)
        self.entrada_arquivo.delete(0, END)
       

    def docx_to_pdf(self):
        caminho_entrada = self.arquivo
        caminho_saida = caminho_entrada.replace(".docx", ".pdf")
        
      
        word_to_pdf(caminho_entrada, caminho_saida)
        self.entrada_arquivo.delete(0, END)


    def jpg_to_pdf(self):
        caminho_entrada = self.arquivo
        caminho_saida = caminho_entrada.replace(".jpg", ".pdf")
        
      
        jpg_to_pdf(caminho_entrada, caminho_saida)
        self.entrada_arquivo.delete(0, END)


    def xlsx_to_pdf(self):
        caminho_entrada = self.arquivo
        caminho_saida = caminho_entrada.replace(".xlsx", ".pdf")
        
      
        excel_to_pdf(caminho_entrada, caminho_saida)
        self.entrada_arquivo.delete(0, END)


    def escolher_arquivo(self):
        self.arquivo = filedialog.askopenfilename(title="Escolha o arquivo")

        if self.arquivo:
            self.nome_arquivo = os.path.basename(self.arquivo)       
            self.entrada_arquivo.insert(0, self.nome_arquivo)


    def window_pdf_to_docx(self):
        window = CTk()
        window.title("PDF para DOCX")
        window.geometry("400x300")

        self.entrada_arquivo = CTkEntry(window, width=250, height=30, border_color='blue')
        self.entrada_arquivo.place(x=70, y=60)

        botao = CTkButton(window, 
            text="Procurar arquivo",
            command=self.escolher_arquivo,
            width=150,
            font=('Verdana', 16)
        )
        botao.place(x=120, y=120)

        converter = CTkButton(window, text="Converter", 
            font=('Verdana', 16), 
            command=self.pdf_to_docx,
            fg_color='#191970',
            hover_color='#000080'
        )
        converter.place(x=120, y=250)

        window.mainloop()


    def window_docx_to_pdf(self):
        window = CTk()
        window.title("DOCX para PDF")
        window.geometry("400x300")

        self.entrada_arquivo = CTkEntry(window, width=250)
        self.entrada_arquivo.place(x=70, y=60)

        botao = CTkButton(window, 
            text="Procurar arquivo",
            command=self.escolher_arquivo,
            width=150,
            font=('Verdana', 16)
        )
        botao.place(x=120, y=120)

        converter = CTkButton(window, text="Converter", 
            font=('Verdana', 16), 
            command=self.pdf_to_docx,
            fg_color='#191970',
            hover_color='#000080'
        )
        converter.place(x=120, y=250)


        window.mainloop()


    def window_jpg_to_pdf(self):
        window = CTk()
        window.title("JPG para PDF")
        window.geometry("400x300")

        self.entrada_arquivo = CTkEntry(window, width=250)
        self.entrada_arquivo.place(x=70, y=60)

        botao = CTkButton(window, 
            text="Procurar arquivo",
            command=self.escolher_arquivo,
            width=150,
            font=('Verdana', 16)
        )
        botao.place(x=120, y=120)

        converter = CTkButton(window, text="Converter", 
            font=('Verdana', 16), 
            command=self.pdf_to_docx,
            fg_color='#191970',
            hover_color='#000080'
        )
        converter.place(x=120, y=250)


        window.mainloop()


    def window_xlsx_to_pdf(self):
        window = CTk()
        window.title("Excel para PDF")
        window.geometry("400x300")

        self.entrada_arquivo = CTkEntry(window, width=250)
        self.entrada_arquivo.place(x=70, y=60)

        botao = CTkButton(window, 
            text="Procurar arquivo",
            command=self.escolher_arquivo,
            width=150,
            font=('Verdana', 16)
        )
        botao.place(x=120, y=120)

        converter = CTkButton(window, text="Converter", 
            font=('Verdana', 16), 
            command=self.pdf_to_docx,
            fg_color='#191970',
            hover_color='#000080'
        )
        converter.place(x=120, y=250)


        window.mainloop()



Conversor()