from tkinter import PhotoImage, RIGHT
from PIL import Image, ImageTk
import customtkinter as tk
import AnalisaDados as ad

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

def verifica_caminho(caminho):
    print(caminho)

def janela_caminho():
    janela = tk.CTk()
    janela.geometry("500x350")
    janela.title("Calculadora Araújo")
    janela.iconbitmap("araujo.ico")
    janela.resizable(False, False)

    img = Image.open("img.png")
    largura, altura = 250, 350
    img = img.resize((largura, altura))
    imagem = ImageTk.PhotoImage(img)
    label_img = tk.CTkLabel(master=janela, image=imagem, text="")
    label_img.place(x=0, y=0)

    frame = tk.CTkFrame(master=janela, width=250, height=396)
    frame.pack(side=RIGHT)

    label = tk.CTkLabel(frame, text="Digite o caminho do arquivo:")
    label.place(x=25, y=75)

    entry = tk.CTkEntry(master=frame, placeholder_text="C:\\EXEMPLO\\EXEMPLO.XLSX", width=200)
    entry.place(x=25, y=105)
    caminho = tk.CTkLabel(frame, text="*O campo caminho do arquivo é\n obrigatório.", text_color="green")
    caminho.place(x=25, y=135)

    checkbox = tk.CTkCheckBox(frame, text="Lembrar")
    checkbox.place(x=25, y=200)

    btn_caminho = tk.CTkButton(frame, text="CONFIRMAR", width=200)
    btn_caminho.place(x=25, y=285)

    def on_click():
        caminho_arquivo = entry.get()
        # if caminho_arquivo != None:
        #     ad.ler_arquivo(caminho_arquivo)
        print(caminho_arquivo)

    btn_caminho.configure(command=on_click())
    janela.mainloop()


janela_caminho()
