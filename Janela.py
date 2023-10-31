from tkinter import PhotoImage, RIGHT
from PIL import Image, ImageTk
import customtkinter as tk

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

def verifica_caminho():
    print("Caminho")

def janela_caminho():
    janela = tk.CTk()
    janela.geometry("500x350")
    janela.title("Calculadora Araújo")
    janela.iconbitmap("araujo.ico")
    janela.resizable(False, False)

    img = Image.open("img.png")
    largura, altura = 250, 350
    img = img.resize((largura, altura))  # Corrigido o argumento aqui
    imagem = ImageTk.PhotoImage(img)
    label_img = tk.CTkLabel(master=janela, image=imagem, text="")
    label_img.place(x=0, y=0)

    frame = tk.CTkFrame(master=janela, width=250, height=396)
    frame.pack(side=RIGHT)

    caminho = tk.CTkLabel(frame, text="Digite o caminho do arquivo")
    caminho.place(x=30, y=30)
    caminho.pack(padx=10, pady=10)
    path = tk.CTkEntry(frame, width=int(200), placeholder_text="C:\\EXEMPLO\\EXEMPLO.XLSX")
    path.pack(padx=10, pady=10)
    btn = tk.CTkButton(frame, text="Ok", command=verifica_caminho)
    btn.pack(padx=10, pady=10)
    janela.mainloop()

janela_caminho()
