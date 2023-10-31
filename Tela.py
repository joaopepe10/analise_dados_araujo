import tkinter as tk

class CalculadoraPassagem(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Calculadora de Passagem")

        # label do usuário
        self.label_usuario = tk.Label(self, text="Usuário:")
        self.label_usuario.grid(row=0, column=0)

        # entrada de usuário
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.grid(row=0, column=1)

        # label da tarifa
        self.label_tarifa = tk.Label(self, text="Tarifa:")
        self.label_tarifa.grid(row=1, column=0)

        # entrada de tarifa
        self.entry_tarifa = tk.Entry(self)
        self.entry_tarifa.grid(row=1, column=1)

        # label do local de moradia
        self.label_moradia = tk.Label(self, text="Local de moradia:")
        self.label_moradia.grid(row=2, column=0)

        # entrada do local de moradia
        self.entry_moradia = tk.Entry(self)
        self.entry_moradia.grid(row=2, column=1)

        # label do local de trabalho
        self.label_trabalho = tk.Label(self, text="Local de trabalho:")
        self.label_trabalho.grid(row=3, column=0)

        # entrada do local de trabalho
        self.entry_trabalho = tk.Entry(self)
        self.entry_trabalho.grid(row=3, column=1)

        # label da quantidade de passagens
        self.label_passagens = tk.Label(self, text="Quantidade de passagens:")
        self.label_passagens.grid(row=4, column=0)

        # entrada da quantidade de passagens
        self.entry_passagens = tk.Entry(self)
        self.entry_passagens.grid(row=4, column=1)

        # label da soma
        self.label_soma = tk.Label(self, text="Soma:")
        self.label_soma.grid(row=5, column=0)

        # entrada da soma das tarfifas
        self.entry_soma = tk.Entry(self)
        self.entry_soma.grid(row=5, column=1)

        # label da economia
        self.label_economia = tk.Label(self, text="Economia:")
        self.label_economia.grid(row=6, column=0)

        # entrada para economia de gastos
        self.entry_economia = tk.Entry(self)
        self.entry_economia.grid(row=6, column=1)

        # botão de calcular
        self.botao_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.botao_calcular.grid(row=7, column=0)

    def calcular(self):
        # obtém os dados do usuário
        usuario = self.entry_usuario.get()
        tarifa = float(self.entry_tarifa.get())
        local_moradia = self.entry_moradia.get()
        local_trabalho = self.entry_trabalho.get()
        quantidade_passagens = int(self.entry_passagens.get())

        # calcula a soma
        soma = tarifa * quantidade_passagens

        # calcula a economia
        economia = 0
        if soma > 100:
            economia = soma * 0.1

        # atualiza os labels
        self.entry_soma.delete(0, "end")
        self.entry_soma.insert(0, soma)
        self.entry_economia.delete(0, "end")
        self.entry_economia.insert(0, economia)


if __name__ == "__main__":
    root = tk.Tk()
    CalculadoraPassagem(root).pack()
    root.mainloop()