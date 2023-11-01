import tkinter as tk
from tkinter import PhotoImage, RIGHT
from PIL import Image, ImageTk
import AnalisaDados as ad

# tk.set_appearance_mode("dark")
# tk.set_default_color_theme("dark-blue")

def verifica_caminho(caminho):
    print(caminho)

def janela_caminho():
    janela = tk.Tk()
    janela.geometry("500x350")
    janela.title("Calculadora Araújo")
    janela.iconbitmap("araujo.ico")
    janela.resizable(False, False)

    img = Image.open("img.png")
    largura, altura = 250, 350
    img = img.resize((largura, altura))
    imagem = ImageTk.PhotoImage(img)
    label_img = tk.Label(master=janela, image=imagem, text="")
    label_img.place(x=0, y=0)

    frame = tk.Frame(master=janela, width=250, height=396)
    frame.pack(side=RIGHT)

    label = tk.Label(frame, text="Digite o caminho do arquivo:")
    label.place(x=25, y=75)

    entry = tk.Entry(master=frame, width=200)
    entry.place(x=25, y=105)

    caminho = tk.Label(frame, text="*O campo caminho do arquivo é\n obrigatório.")
    caminho.place(x=25, y=135)

    checkbox = tk.Checkbutton(frame, text="Lembrar")
    checkbox.place(x=25, y=200)

    def on_click():
        caminho_arquivo = entry.get()
        ad.ler_arquivo(caminho_arquivo)
        print(caminho_arquivo)

    btn_caminho = tk.Button(frame, text="CONFIRMAR", width=200)
    btn_caminho.place(x=25, y=285)
    btn_caminho.config(command=on_click)

    janela.mainloop()
    return entry.get()

janela_caminho()
