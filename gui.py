from config import Funcs
from tkinter import * 

window = Tk()

# Cria a janela principal
class Application(Funcs):
    def __init__(self):
        self.window = window
        self.config_page()
        self.config_tk()
        self.tela()
        self.frame_da_tela()
        self.widgets_frame()
        self.menu()
        window.mainloop()

    def config_tk(self):
        ''' Configuração para as Label, Entry e Button'''

        self.cor_fundo = "#4B0082"
        self.fundo_frame = "#9370DB"
        self.cor_fonte = "#000000"
        self.fundo_botao = "#8A2BE2"
        self.fundo_sucesso = '#3CB371'	
        self.fundo_fracasso = '#CD5C5C'
        self.fonte_padrao = 'Courier',12,'bold'
        self.fonte_titulo = 'Courier',14,'bold'
        self.fonte_meu_nome = 'Courier',9,'bold'

    def tela(self):
           
        self.window.title("Fracionamento de Comprimidos")
        self.window.iconbitmap("icon.ico")
        self.window.configure(background=self.cor_fundo)
        self.window.geometry("500x500")
        self.window.maxsize(width=900, height=700) #TAMANHO MÁXIMO 
        self.window.minsize(width=500, height=400) #TAMANHO MÍNIMO 

    def frame_da_tela(self):

        self.frame = Frame(self.window, bd=4, bg=self.fundo_frame, highlightbackground=self.fundo_frame, 
                             highlightthickness=3)
        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight= 0.96)

    def widgets_frame(self):
        self.lb_nome_med = Label(self.frame, text="Nome do medicamento:", bg=self.fundo_frame, fg=self.cor_fonte, 
                                 font=(self.fonte_padrao))
        self.lb_nome_med.place(relx=0.05, rely=0.05)

        self.nome_med_entry = Entry(self.frame, font=(self.fonte_padrao))
        self.nome_med_entry.place(relx=0.05, rely=0.10, relwidth=0.8, relheight=0.07)

        self.lb_mg = Label(self.frame, text="Dosagem (mg):", bg=self.fundo_frame, fg=self.cor_fonte, 
                                 font=(self.fonte_padrao))
        self.lb_mg.place(relx=0.05, rely=0.25)

        self.mg_entry = Entry(self.frame, font=(self.fonte_padrao))
        self.mg_entry.place(relx=0.05, rely=0.30, relwidth=0.8, relheight=0.07)

        self.lb_lote = Label(self.frame, text="Lote:", bg=self.fundo_frame, fg=self.cor_fonte, 
                                 font=(self.fonte_padrao))
        self.lb_lote.place(relx=0.05, rely=0.45)

        self.lote_entry = Entry(self.frame, font=(self.fonte_padrao))
        self.lote_entry.place(relx=0.05, rely=0.50, relwidth=0.8, relheight=0.07)

        self.lb_validade = Label(self.frame, text="Validade:", bg=self.fundo_frame, fg=self.cor_fonte, 
                                 font=(self.fonte_padrao))
        self.lb_validade.place(relx=0.05, rely=0.65)

        self.validade_entry = Entry(self.frame, font=(self.fonte_padrao))
        self.validade_entry.place(relx=0.05, rely=0.70, relwidth=0.8, relheight=0.07)

        self.lb_identity =  Label(text="Desenvolvido por Alicia Lima", bg=self.fundo_frame, fg=self.cor_fonte, 
                                 font=(self.fonte_meu_nome))
        self.lb_identity.place(relx=0.55, rely=0.93)

        self.bt_gera_pdf = Button(self.frame, text="Gerar PDF", bd=4, bg=self.fundo_botao, fg=self.cor_fonte,  font=(self.fonte_padrao),
                                  command=lambda:self.export_to_pdf_and_open())
        self.bt_gera_pdf.place(relx=0.20, rely=0.85, relwidth=0.22, relheight=0.10)

        self.bt_limpa_entrada = Button(self.frame, text="Limpar", bd=4, bg=self.fundo_botao, fg=self.cor_fonte,  font=(self.fonte_padrao),
                                       command=self.limpa_tela())
        self.bt_limpa_entrada.place(relx=0.60, rely=0.85, relwidth=0.22, relheight=0.10)

    def menu(self):
        menubar = Menu(self.window)
        self.window.config(menu=menubar)

        filemenu = Menu(menubar)
        menubar.add_command(label="Sobre", command=self.sobre_app)

    def mensagem_de_fracasso(self):
        self.lb_men_suc = Label(self.frame, text="Data Invalida", bg=self.fundo_fracasso, fg=self.cor_fonte,
                                         font=(self.fonte_padrao))
        self.lb_men_suc.place(relx=0.05, rely=0.01)
        self.window.after(1000, self.clear_message)

    def clear_message(self):
        self.lb_men_suc.config(text="", bg=self.fundo_frame)

# Executa o loop principal da janela
Application()

