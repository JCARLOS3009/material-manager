import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import user  # Importa o módulo user.py

# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('crud_app.db')
c = conn.cursor()

# Criar as tabelas com os campos adicionais
c.execute('''
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    unit TEXT NOT NULL,
    price REAL NOT NULL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL
)
''')
conn.commit()
conn.close()

# Função para abrir a janela de gerenciamento de usuários
def abrir_gerenciamento_usuarios():
    user.open_user_window()

# Função para atualizar a lista de itens exibida
def atualizar_lista_itens():
    lista_box_itens.delete(0, tk.END)
    conn = sqlite3.connect('crud_app.db')
    c = conn.cursor()
    c.execute('SELECT * FROM items')
    for row in c.fetchall():
        lista_box_itens.insert(tk.END, f"{row[1]} (Unidade: {row[2]}, Preço: R${row[3]:.2f})")
    conn.close()

# Função para adicionar um item
def adicionar_item():
    name = entry_name.get()
    unit = entry_unit.get()
    try:
        price = float(entry_price.get())
    except ValueError:
        messagebox.showwarning("Aviso", "Preço deve ser um número válido!")
        return
    
    if name and unit and entry_price.get():
        conn = sqlite3.connect('crud_app.db')
        c = conn.cursor()
        c.execute('INSERT INTO items (name, unit, price) VALUES (?, ?, ?)', (name, unit, price))
        conn.commit()
        conn.close()
        atualizar_lista_itens()
        entry_name.delete(0, tk.END)
        entry_unit.delete(0, tk.END)
        entry_price.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")

# Função para atualizar o item selecionado
def atualizar_item():
    selecionado = lista_box_itens.curselection()
    if selecionado:
        item_id = selecionado[0] + 1  # +1 porque o índice começa do zero
        novo_nome = entry_name.get()
        nova_unidade = entry_unit.get()
        try:
            novo_preco = float(entry_price.get())
        except ValueError:
            messagebox.showwarning("Aviso", "Preço deve ser um número válido!")
            return
        
        if novo_nome and nova_unidade and entry_price.get():
            conn = sqlite3.connect('crud_app.db')
            c = conn.cursor()
            c.execute('UPDATE items SET name = ?, unit = ?, price = ? WHERE id = ?', (novo_nome, nova_unidade, novo_preco, item_id))
            conn.commit()
            conn.close()
            atualizar_lista_itens()
            entry_name.delete(0, tk.END)
            entry_unit.delete(0, tk.END)
            entry_price.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
    else:
        messagebox.showwarning("Aviso", "Nenhum item selecionado!")

# Função para deletar o item selecionado
def deletar_item():
    selecionado = lista_box_itens.curselection()
    if selecionado:
        item_id = selecionado[0] + 1  # +1 porque o índice começa do zero
        conn = sqlite3.connect('crud_app.db')
        c = conn.cursor()
        c.execute('DELETE FROM items WHERE id = ?', (item_id,))
        conn.commit()
        conn.close()
        atualizar_lista_itens()
        entry_name.delete(0, tk.END)
        entry_unit.delete(0, tk.END)
        entry_price.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Nenhum item selecionado!")

# Cria a janela principal
root = tk.Tk()
root.title("Sistema CRUD com Tkinter e SQLite")

# Define o tamanho da janela (largura x altura)
root.geometry("800x600")  # Aumentei a altura para acomodar os novos campos e botões

# Carregar a imagem
imagem = Image.open('logo.png')  # Substitua 'logo.png' pelo nome da sua imagem
imagem = imagem.resize((200, 100), Image.LANCZOS)  # Ajusta o tamanho da imagem
imagem_tk = ImageTk.PhotoImage(imagem)

# Adiciona a imagem à janela
label_imagem = tk.Label(root, image=imagem_tk)
label_imagem.pack(pady=10)  # Adiciona um pouco de espaço ao redor da imagem

# Cria o frame para os campos e botões de itens
frame_itens = tk.Frame(root)
frame_itens.pack(padx=10, pady=10)

# Configura a grid para itens
frame_itens.grid_columnconfigure(0, weight=1)
frame_itens.grid_columnconfigure(1, weight=1)
frame_itens.grid_columnconfigure(2, weight=1)
frame_itens.grid_columnconfigure(3, weight=1)
frame_itens.grid_columnconfigure(4, weight=1)
frame_itens.grid_columnconfigure(5, weight=1)

tk.Label(frame_itens, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_name = tk.Entry(frame_itens, width=15)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_itens, text="Unidade:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
entry_unit = tk.Entry(frame_itens, width=15)
entry_unit.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_itens, text="Preço:").grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)
entry_price = tk.Entry(frame_itens, width=15)
entry_price.grid(row=0, column=5, padx=5, pady=5)

adicionar_btn_itens = tk.Button(frame_itens, text="Adicionar Item", command=adicionar_item)
adicionar_btn_itens.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)

atualizar_btn_itens = tk.Button(frame_itens, text="Atualizar Item", command=atualizar_item)
atualizar_btn_itens.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)

deletar_btn_itens = tk.Button(frame_itens, text="Deletar Item", command=deletar_item)
deletar_btn_itens.grid(row=1, column=4, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)

lista_box_itens = tk.Listbox(frame_itens, width=80, height=10)
lista_box_itens.grid(row=2, column=0, columnspan=6, padx=5, pady=5)

# Adiciona o botão para abrir a nova janela
btn_usuarios = tk.Button(root, text="Gerenciar Usuários", command=abrir_gerenciamento_usuarios)
btn_usuarios.pack(pady=10)

# Inicializa a lista ao iniciar o aplicativo
atualizar_lista_itens()

# Inicia o loop principal do Tkinter
root.mainloop()
