import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage, RIGHT
from PIL import Image, ImageTk
import AnalisaDados as ad
# import  TelaConsulta as tc
from tkinter import messagebox
import os
import pandas as pd

janela = Tk()


class TelaDiretorio():
    limite_ultrapassado = 0
    limite_n_ultrapassado = 0
    data_frame = pd.DataFrame()
    _diretorio = None

    def __init__(self):
        self.janela = janela
        self.tela_diretorio()
        self.frames_da_tela()
        self.btn_envia_diretorio()
        janela.mainloop()

    def tela_diretorio(self):
        # DEFINE AS CONFIGURACOES DA TELA PRINCIPAL
        self.janela.geometry("500x350")
        self.janela.title("Calculadora Araújo")
        self.janela.configure(background='#0059b3')
        self.janela.iconbitmap("araujo.ico")
        self.janela.resizable(False, False)

        # CONFIGURA IMAGEM NO FRAME DA ESQUERDA
        self.img = Image.open("img.png")
        largura, altura = 250, 350
        self.img = self.img.resize((largura, altura))
        self.imagem = ImageTk.PhotoImage(self.img)
        self.label_img = Label(master=janela, image=self.imagem, text="")
        self.label_img.place(x=0, y=0)

    def frames_da_tela(self):
        # CRIACAO DE TELAS ESTILIZADAS COM IMAGEM E SUB-DIVISAO DE TELA

        self.frame_diretorio = Frame(master=janela, width=250, height=396, background='#0059b3')
        self.frame_diretorio.pack(side=RIGHT)

        self.label = Label(self.frame_diretorio, text="Digite o caminho do arquivo:", background='#0059b3')
        self.label.place(x=25, y=75)

        self.diretorio_entry = Entry(master=self.frame_diretorio, width=35)
        self.diretorio_entry.place(x=25, y=105)

        self._diretorio = self.diretorio_entry.get()

        self.caminho = Label(self.frame_diretorio, text="*O campo caminho do arquivo é\n obrigatório.",
                             background='#0059b3')
        self.caminho.place(x=25, y=135)

        self.checkbox = Checkbutton(self.frame_diretorio, text="Lembrar", background='#0059b3')
        self.checkbox.place(x=25, y=200)

    def btn_envia_diretorio(self):
        self.btn_caminho = Button(self.frame_diretorio, text="CONFIRMAR", width=20, background='#A52A2A')
        self.btn_caminho.place(x=25, y=285)
        self.btn_caminho.config(command=self.verifica_diretorio)

    def verifica_diretorio(self):
        # CONFIGURA UMA NOVA JANELA A PARTIR DO CLIQUE CONFIRMAR DA JANELA DO DIRETORIO
        self.diretorio = self.diretorio_entry.get()
        diretorio = self.diretorio_entry.get()
        print(f'DIRETORIO {diretorio}')
        if len(self.diretorio) == 0:
            return messagebox.showerror('error', "Campo vazio!")
        if os.path.exists(diretorio):
            self.janela.quit()
            from TelaConsulta import TelaConsulta
            tela_consulta = TelaConsulta(self.diretorio)
            tela_consulta.tela_consulta()
        else:
            return messagebox.showerror('error', "Digite um diretório válido!")
    @staticmethod
    def obter_diretorio():
        TelaDiretorio._diretorio = TelaDiretorio
        return TelaDiretorio._diretorio


if __name__ == "__main__":
    TelaDiretorio()