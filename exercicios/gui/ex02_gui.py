import tkinter as tk

# 1) Criar janela principal
root = tk.Tk()
root.config(bg="#E8DFE4")
root.title("Ex02 – Respondendo ao usuário")
root.geometry("400x200")


# 2) Definir widgets (Labels, Entry, Button)
#    – Label de instrução
lbl = tk.Label(
    root, text="Digite o seu nome: "
    font=("Arial", 32, "bold"),   # família, tamanho, estilo
    fg="white",                    # texto em branco
    bg="blue"                      # fundo azul
)

#    – Entry para o nome
#    – Button para “enviar”
#    – Label de saída (inicialmente vazio)

# 3) Função callback do botão
def saudar():
    # ler o texto da Entry
    # montar a mensagem formatada
    # atualizar o Label de saída com .config(text=…)

# 4) Organizar (pack/grid) todos os widgets

# 5) Iniciar loop
    root.mainloop()