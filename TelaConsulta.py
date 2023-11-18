import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


import pandas as pd

janela = Tk()


class TelaConsulta():
    diretorio = ''
    indice = 0


    def __init__(self, diretorio):
        self.diretorio = diretorio
        self.janela = janela
        self.tela_consulta()
        self.btn_envia_vlr()
        janela.mainloop()

    def tela_consulta(self):
        self.janela.geometry("500x350")
        self.janela.title('CALCULADORA DE TARIFA')
        self.janela.configure(background='#A52A2A')
        self.janela.iconbitmap("araujo.ico")
        self.janela.resizable(False, False)

        self.label_valor = Label(self.janela, text="Digite o valor maximo estipulado:", background='#A52A2A')
        self.label_valor.place(x=25, y=75)

        self.entry_valor = Entry(master=self.janela, width=30)
        self.entry_valor.place(x=25, y=100)

        self.vlr = Label(self.janela, text="*CAMPO OBRIGATORIO.",
                         background='#A52A2A')
        self.vlr.place(x=25, y=125)

        self.label_dia = Label(self.janela, text="Digite a quantidade em dias a ser analisado( 31 dias no maximo ):",
                               background='#A52A2A')
        self.label_dia.place(x=25, y=130)

        self.entry_dia = Entry(master=self.janela, width=30)
        self.entry_dia.place(x=25, y=150)


        self.dia = Label(self.janela, text="*CAMPO OBRIGATORIO.",
                         background='#A52A2A')
        self.dia.place(x=25, y=175)
    def btn_envia_vlr(self):
        self.btn_caminho = Button(master=self.janela, text="CONFIRMAR", width=20, background='#0059b3')
        self.btn_caminho.place(x=25, y=285)
        self.btn_caminho.config(command=self.verifica_valores)

    def verifica_valores(self):
        valor_str = self.entry_valor.get()
        dia_str = self.entry_dia.get()

        # Verifique se os campos estão vazios
        if len(valor_str) == 0 or len(dia_str) == 0:
            return messagebox.showerror('error', "Campo(s) vazio(s)!")

        try:
            # Tente converter os valores para float e int
            valor = float(valor_str)
            dia = int(dia_str)

            # Verifique se os valores convertidos são válidos
            if valor > 0 and 0 < dia < 32:
                self.tela_resultado()
            else:
                messagebox.showerror('error', "Valores inválidos!")
        except ValueError:
            messagebox.showerror('error', "Erro ao converter para float ou int.")



    def tela_resultado(self):
        self.resultado = tkinter.Toplevel()
        self.resultado.geometry("850x550")
        self.resultado.title("RESULTADO")
        self.resultado.configure(background='#0059b3')
        self.resultado.iconbitmap("araujo.ico")
        self.resultado.resizable(True, False)

        self.btn_carrega_df()

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview",background="#FF6347",foreground="black", rowheight=25, fieldbackground="#FF6347")

        self.colunas = ttk.Treeview(self.resultado, columns=("column1", "column2", "column3", "column4", "column5", "column6"), show='headings', yscrollcommand=True)
        self.colunas.show_lines = False
        self.colunas.show_root_lines = False
        self.colunas.show_node_lines = False

        self.colunas.column("column1", minwidth=0, width=10)
        self.colunas.column("column2", minwidth=0, width=100)
        self.colunas.column("column3", minwidth=0, width=275)
        self.colunas.column("column4", minwidth=0, width=70)
        self.colunas.column("column5", minwidth=0, width=70)
        self.colunas.column("column6", minwidth=0, width=125)

        self.colunas.heading("#1", text="")
        self.colunas.heading("#2", text="CHAPA")
        self.colunas.heading("#3", text="NOME")
        self.colunas.heading("#4", text="VALOR")
        self.colunas.heading("#5", text="VIAGENS")
        self.colunas.heading("#6", text=f'TOTAL GASTO EM {self.entry_dia.get()} DIAS')
        self.colunas.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.barra_rolagem = Scrollbar(self.resultado, orient='vertical', command=self.colunas.yview)
        self.colunas.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.place(relx=0.96, rely=0.1, relwidth=0.4, relheight=0.85)

    def ordenar_coluna(self, coluna, reverse=False):
        items = list(self.colunas.get_children())

        def get_valor(item):
            try:
                # Tente converter para float, caso seja um valor numérico
                return float(self.colunas.item(item, 'values')[self.colunas["columns"].index(coluna)])
            except ValueError:
                # Se não puder converter para float, retorne 0
                return 0

        items.sort(key=lambda item: get_valor(item), reverse=reverse)

        for i, item in enumerate(items):
            valores = [float(self.colunas.item(item, 'values')[col]) for col in range(1, 6)]
            total = sum(valores) * int(self.entry_dia.get())
            self.colunas.move(item, '', i)
            self.colunas.item(item, values=(i + 1, *self.colunas.item(item, 'values')[1:], total))
    def btn_carrega_df(self):
        self.btn_carrega_dados = Button(master=self.resultado, text="CARREGAR", width=20, background='#0059b3')
        self.btn_carrega_dados.place(x=25, y=8)
        self.btn_carrega_dados.configure(command=self.chama_df)

    def chama_df(self):
        self.consulta_df()

    def pega_diretorio(self):
        from Tela import TelaDiretorio
        path = TelaDiretorio.obter_diretorio()
        return path
    def consulta_df(self):

        indice_proximo_funcionario = 0  # Adicionando inicialização do índice
        path = self.pega_diretorio()
        df = pd.read_excel(path)

        # REMOVE DUPLICIDADE DE ACORDO COM PARAMETRO CHAPA
        df_nao_duplicada = df.drop_duplicates('CHAPA')
        tam_df_sem_duplicidade = len(df_nao_duplicada)

        # ITERA SOBRE UM NOVO DATA-FRAME SEM DUPLICIDADE
        index = 1
        for j in range(100):
            if indice_proximo_funcionario < len(df_nao_duplicada):
                indice_proximo_funcionario = self.indice

                nr_viagens = 0

                chapa = df_nao_duplicada['CHAPA'].iloc[j]
                funcionario_buscado = df.query(f'CHAPA=="{chapa}"')

                tam = len(funcionario_buscado)

                # SOMA QUANTIDADE DE NUMERO DE VIAGENS DIARIA POR FUNCIONARIO

                for i in range(tam):
                    casting = funcionario_buscado['NROVIAGENS'].iloc[i]
                    nr_viagens = nr_viagens + casting
                nome_funcionario = funcionario_buscado['NOME'].iloc[0]
                chapa = funcionario_buscado['CHAPA'].iloc[0]
                total_passagem = 0.0

                # ITERA SOBRE O FUNCIONARIO BUSCADO E SOMA O VALOR DAS PASSAGENS DE ACORDO COM A QUANTIDADE QUE CONTEM NO DATA-FRAME(FUNCIONARIO BUSCADO)

                for x in range(tam):
                    vlr_passagem = funcionario_buscado["VALOR"].iloc[x]
                    total_passagem = total_passagem + vlr_passagem

                dias_trabalhados = int(self.entry_dia.get())  # Convertendo para int e obtendo valor da entrada
                limite_valor_mes = float(self.entry_valor.get())  # Convertendo para float e obtendo valor da entrada
                total_num_viagem = nr_viagens * dias_trabalhados
                total_gasto = total_num_viagem * total_passagem

                limite_extrapolado = total_gasto > limite_valor_mes
                try:
                    if limite_extrapolado:
                        total_gasto = "{:.2f}".format(total_gasto)
                        total_passagem = "{:.2f}".format(total_passagem)
                        lista = [index, chapa, nome_funcionario, total_passagem, nr_viagens, total_gasto]
                        self.colunas.insert("", END, values=lista)
                        index = index + 1
                        indice_proximo_funcionario = indice_proximo_funcionario + 1
                        self.indice = indice_proximo_funcionario
                except KeyError:
                    pass


