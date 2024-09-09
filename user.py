import tkinter as tk
from tkinter import messagebox
import sqlite3

def open_user_window():
    # Cria a nova janela
    user_window = tk.Toplevel()
    user_window.title("Gerenciar Usuários")
    user_window.geometry("400x300")

    # Função para adicionar um usuário
    def adicionar_usuario():
        username = entry_username.get()
        email = entry_email.get()
        
        if username and email:
            conn = sqlite3.connect('crud_app.db')
            c = conn.cursor()
            c.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
            conn.commit()
            conn.close()
            atualizar_lista_usuarios()
            entry_username.delete(0, tk.END)
            entry_email.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")

    # Função para atualizar a lista de usuários exibida
    def atualizar_lista_usuarios():
        lista_box_usuarios.delete(0, tk.END)
        conn = sqlite3.connect('crud_app.db')
        c = conn.cursor()
       
