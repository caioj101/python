import tkinter as tk
root = tk.Tk()
root.config(bg="blue")
root.title("Ex01 – Primeiro comando")
root.geometry("350x100")
lbl = tk.Label(
    root,
    text="Olá, Mundo!",
    font=("Arial", 32, "bold"),   # família, tamanho, estilo
    fg="white",                    # texto em branco
    bg="blue"                      # fundo azul
)
lbl.pack(pady=20, fill="both", expand=True)

root.mainloop()

