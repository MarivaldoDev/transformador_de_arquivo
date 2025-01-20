from customtkinter import *



class Conversor:
    def __init__(self):
        self.window = CTk()
        self.window.title("Conversor de Arquivos")
        self.window.geometry("400x300")
        self.window.iconbitmap("images/logo.ico")
        self.window.resizable(False, False)
        self.options()
        self.buttons_positions()
        self.window.mainloop()



    def options(self):
        self.option1 = CTkButton(self.window, 
            text='PDF para DOCX', 
            fg_color='red', 
            text_color='white', 
            hover_color='#A52A2A',
            font=('Verdana', 18),
            height=30
        )

        self.option2 = CTkButton(self.window, 
            text='DOCX para PDF', 
            fg_color='blue', 
            text_color='white', 
            hover_color='#00008B',
            font=('Verdana', 18),
            height=30
        )

        self.option3 = CTkButton(self.window, 
            text='JPG para PDF', 
            fg_color='#008080', 
            text_color='white', 
            hover_color='#2F4F4F',
            font=('Verdana', 18),
            height=30,
            width=155
        )

        self.option4 = CTkButton(self.window, 
            text='XLSX para PDF', 
            fg_color='#2E8B57', 
            text_color='white', 
            hover_color='#006400',
            font=('Verdana', 18),
            height=30,
            width=155
        )


    def buttons_positions(self):
        self.option1.place(x=125, y=50)
        self.option2.place(x=125, y=100)
        self.option3.place(x=125, y=150)
        self.option4.place(x=125, y=200)


    def window_pdf_to_word(self):
        pass




Conversor()