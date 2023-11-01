from tkinter import *
import os
import AnalisaDados as ad
def nova_janela():
    exec(open())

def janela_menu():
    janela = Tk()
    janela.geometry("500x350")
    janela.title("Calculadora Araújo")
    janela.iconbitmap("araujo.ico")
    janela.resizable(False, False)

    matricula_label = Label(master=janela, text="Digite a matricula do funcionário")
    matricula_label.place(x=25, y=0)

    matricula_entry = Entry(master=janela, width=40)
    matricula_entry.place(x=25, y=30)

    vlr_maximo_label = Label(master=janela, text="Digite o valor maximo para esse funcionário")
    vlr_maximo_label.place(x=25, y=60)

    vlr_maximo_entry = Entry(master=janela, width=40)
    vlr_maximo_entry.place(x=25, y=90)

    def obter_gasto():
        matricula = matricula_entry.get()
        return ad.consulta_df()





    frame = Frame(master=janela, width=250, height=396)
    frame.pack(side=RIGHT)

    label = Label(frame, text="Valor:")
    label.place(x=25, y=75)

    valor = Label(frame, text="Funcionarios: ")

    btn_obter_gasto = Button(frame, text="CONFIRMAR", width=200)
    btn_obter_gasto.place(x=25, y=210)
    def on_click():
        valor.config(text=obter_gasto())
        janela.update()

    btn_obter_gasto.config(command=on_click())

    # Label(janela, text="Busca funcionarios")
    # texto = Text(janela)
    # texto.place(x=25, y=120, width=250)


    janela.mainloop()

janela_menu()