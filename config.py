from reportlab.pdfgen import canvas
from tkinter import * 
from reportlab.lib.pagesizes import A4
from datetime import datetime
import os


class Funcs():
    def limpa_tela(self):
        self.nome_med_entry.delete(0, END)
        self.mg_entry.delete(0, END)
        self.lote_entry.delete(0, END)
        self.validade_entry.delete(0, END)

    def variaveis(self):
        self.nome_med = self.nome_med_entry.get().title()
        self.mg = self.mg_entry.get()
        self.lote = self.lote_entry.get().upper()
        self.validade = self.validade_entry.get()
        self.espaco = '     '

    def dowloads_path(self):
        ''' names the pdf and  local for the file  '''
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M")  # Formato: ano-mês-dia_hora-minuto
        self.file_path = os.path.join(downloads_path, f"fracionamento_{current_time}.pdf")

    def config_page(self):
        self.dowloads_path()
        # Determines the page size select font and font size
        self.c = canvas.Canvas(self.file_path,  pagesize=A4)
        self.c.setFont ("Times-Roman", 7.0)
        self.w, self.h = A4
        self.x_offset = 0
        self.y_offset = 0

    def export_to_pdf_and_open(self):
    
        self.dowloads_path()
        self.config_page()

        #Sets the number of columns 
        row_height = (self.h - 2 * self.y_offset)/ 18
        column_width = (self.w - 2 * self.x_offset)/ 14 

        # Create xlist with x position for the column and  ylist y position for the row
        xlist = [self.x_offset + i * column_width for i in range(15)]
        ylist = [self.h - self.y_offset - i * row_height for i in range(19)]
        
        # Recupera os valores dos widgets de entrada
        self.variaveis()

        # Create the data with the nunber of times the data will be repeat
        data = [f"""{self.espaco}\n{self.nome_med}\n{self.mg}\n{self.lote}\n Val: {self.validade}\n{self.espaco}"""] * 15 * 19

        #design the grid 
        self.c.grid(xlist, ylist)
        
        # fill the cell with information 
        for row in range(19):
            for col in range(15):
                x = xlist[col] + column_width / 2 # Calculates cell center position
                y = ylist[row] + row_height / 2 # Subtract the index from the line to draw from the base upwards
                
                text = data[row * 15 + col] # Centerlize the text in the cell and calculate the width of text
                lines = text.split("\n") # Determine the split of the line 

                line_height = 10 # Determine the height between the lines
                total_text_height = len(lines) * line_height
                start_y = y - total_text_height / 2 + line_height * (len(lines) - 1) #Calulate the initial position of the design

                #Design each text's line from background of the cell
                for idx, line in enumerate(lines):
                    line_y = start_y - idx * line_height
                    text_width = self.c.stringWidth(line, "Times-Roman", 7.0)
                    self.c.drawString(x - text_width/2, line_y, line)
        self.c.save()
        os.startfile(self.file_path)

    def sobre_app(self):
        self.dowloads_path()
        self.config_page()

        textobject = self.c.beginText()
        textobject.setTextOrigin(30, 700)

        self.c.setFont ("Times-Roman", 12.0)
        textobject.setLeading(20)
        textobject.textLines("""
                            Esse aplicativo foi desenvolvido com o intuito de facilicar a criação de etiquetas para fracionamento 
                            de comprimidos em acordo com a resolução da diretoria colegiada - RDC n°80 de 2006.
                             E a resolução RDC n°67 de 2007 que dispõe sobra Boas Práticas de Manipulação de Preparações Magistrais
                             e Oficinais para Uso Humano em farmácias.
                            
                              """)
        self.c.drawText(textobject)

        self.c.setFont ("Times-Roman", 10.0)
        self.c.drawString(300, 100, """Desenvolvido por: Alicia Santos de Lima no ano de 2024.""")
        

        self.c.save()
        os.startfile(self.file_path)
        