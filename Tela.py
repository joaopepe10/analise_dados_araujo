import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage, RIGHT
from PIL import Image, ImageTk
import AnalisaDados as ad
from tkinter import messagebox
import os
import pandas as pd

janela = Tk()


class Aplicacao():
    limite_ultrapassado = 0
    limite_n_ultrapassado = 0

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

        self.caminho = Label(self.frame_diretorio, text="*O campo caminho do arquivo é\n obrigatório.",
                             background='#0059b3')
        self.caminho.place(x=25, y=135)

        self.checkbox = Checkbutton(self.frame_diretorio, text="Lembrar", background='#0059b3')
        self.checkbox.place(x=25, y=200)

    def btn_envia_diretorio(self):
        self.btn_caminho = Button(self.frame_diretorio, text="CONFIRMAR", width=20, background='#A52A2A')
        self.btn_caminho.place(x=25, y=285)
        self.btn_caminho.config(command=self.verifica_diretorio)

    def btn_envia_vlr(self):
        self.btn_caminho = Button(self.analise, text="CONFIRMAR", width=20, background='#0059b3')
        self.btn_caminho.place(x=25, y=285)

        self.btn_caminho.config(command=self.consulta_df)

    def consulta_df(self):
        contador_funcionario_limite = 0
        contador_funcionario_normal = 0
        # path = self.diretorio_entry.get()
        df = pd.read_excel(self.diretorio)

        # REMOVE DUPLICIDADE DE ACORDO COM PARAMETRO CHAPA
        df_nao_duplicada = df.drop_duplicates('CHAPA')
        tam_df_sem_duplicidade = len(df_nao_duplicada)

        # ITERA SOBRE UM NOVO DATA-FRAME SEM DUPLICIDADE

        for j in range(tam_df_sem_duplicidade):
            nr_viagens = 0
            if 0 <= j < len(df_nao_duplicada):
                # BUSCA PELA QUANTIDADE DE VEZ QUE O FUNCIONARIO REPETE TODOS OS DADOS DO MESMO CONTIDO NA TABELA, PARA MANIPULAR OS DADOS

                chapa = df_nao_duplicada['CHAPA'].iloc[j]
                funcionario_buscado = df.query(f'CHAPA=="{chapa}"')
            tam = len(funcionario_buscado)

            # SOMA QUANTIDADE DE NUMERO DE VIAGENS DIARIA POR FUNCIONARIO

            for i in range(tam):
                casting = funcionario_buscado['NROVIAGENS'].iloc[i]
                nr_viagens = nr_viagens + casting
            nome_funcionario = funcionario_buscado['NOME'].iloc[0]

            total_passagem = 0.0

            # ITERA SOBRE O FUNCIONARIO BUSCADO E SOMA O VALOR DAS PASSAGENS DE ACORDO COM A QUANTIDADE QUE CONTEM NO DATA-FRAME(FUNCIONARIO BUSCADO)

            for x in range(tam):
                vlr_passagem = funcionario_buscado["VALOR"].iloc[x]
                total_passagem = total_passagem + vlr_passagem

            dias_trabalhados = self.entry_dia
            total_num_viagem = nr_viagens * dias_trabalhados
            limite_valor_mes = self.entry_valor
            total_gasto = total_num_viagem * total_passagem

            limite_extrapolado = total_gasto > limite_valor_mes
            if limite_extrapolado:
                print(f'VALOR LIMITE: R$ {limite_valor_mes}')
                print(f'VALOR GASTO POR FUNCIONÁRIO: R$ {format(total_gasto, ".2f")}')
                print(
                    f'O limite do valor gasto por mês foi ultrapassado, portanto, funcionário(a) {nome_funcionario} é recomendando mudar de loja!')
                contador_funcionario_limite += 1
            else:
                print(
                    f'O limite não foi ultrapassado, portanto, funcionário(a) {nome_funcionario} não precisará mudar de loja!')
                contador_funcionario_normal += 1
        self.limite_ultrapassado = contador_funcionario_limite
        self.limite_n_ultrapassado = contador_funcionario_normal

    # def calcula_valor_limite(self):

    def cria_nova_janela(self):
        self.analise = tkinter.Toplevel()
        self.analise.geometry("500x350")
        self.analise.title('CALCULADORA DE TARIFA')
        self.analise.configure(background='#A52A2A')
        self.analise.iconbitmap("araujo.ico")
        self.analise.resizable(False, False)

        # self.frame_valor = Frame(master=self.analise, width=250, height=396, background='#0059b3')
        # self.frame_valor.pack(side=RIGHT)

        self.label_valor = Label(self.analise, text="Digite o valor maximo estipulado:", background='#A52A2A')
        self.label_valor.place(x=25, y=75)

        self.entry_valor = Entry(master=self.analise, width=30)
        self.entry_valor.place(x=25, y=100)

        self.vlr = Label(self.analise, text="*CAMPO OBRIGATORIO.",
                         background='#A52A2A')
        self.vlr.place(x=25, y=125)

        self.label_dia = Label(self.analise, text="Digite a quantidade em dias a ser analisado( 31 dias no maximo ):",
                               background='#A52A2A')
        self.label_dia.place(x=25, y=130)

        self.entry_dia = Entry(master=self.analise, width=30)
        self.entry_dia.place(x=25, y=150)

        self.dia = Label(self.analise, text="*CAMPO OBRIGATORIO.",
                         background='#A52A2A')
        self.dia.place(x=25, y=175)

        self.btn_envia_vlr()

    def verifica_diretorio(self):
        # CONFIGURA UMA NOVA JANELA A PARTIR DO CLIQUE CONFIRMAR DA JANELA DO DIRETORIO

        diretorio = self.diretorio_entry.get()
        print(f'DIRETORIO {diretorio}')
        if len(diretorio) == 0:
            return messagebox.showerror('error', "Campo vazio!")
        if os.path.exists(diretorio):
            self.cria_nova_janela()

        else:
            return messagebox.showerror('error', "Digite um diretório válido!")


Aplicacao()
