import tkinter as tk
from tkinter import ttk, messagebox

# Dados em memória
pets = []
nest_pet_id = 1

# Configuração da janela principal
root = tk.Tk()
root.title('Sistema de Cadastro de pets')
root.geometry('800x500')

# Frame do formulário
frame_form = ttk.LabelFrame(root,
                            text='Formulário de pet')
frame_form.pack(padx=10, pady=5, fill='x')

# Campos do formulário
ttk.Label(frame_form, text='Tutor:').grid(row=0,
                                          column=0, padx=5,pady=5,
                                        sticky='e')
entry_tutor = ttk.Entry(frame_form,width=40)
entry_tutor.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Nome:').grid(row=1,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_tutor = ttk.Entry(frame_form,width=40)
entry_tutor.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Espécie:').grid(row=2,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_tutor = ttk.Entry(frame_form,width=40)
entry_tutor.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Raça:').grid(row=3,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_tutor = ttk.Entry(frame_form,width=40)
entry_tutor.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Idade:').grid(row=4,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_tutor = ttk.Entry(frame_form,width=40)
entry_tutor.grid(row=4, column=1, padx=5, pady=5)

# Frame de botões
frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=5)

btn_adicionar = ttk.Button(frame_botoes, text='Adicionar', comand=None)
btn_adicionar.grid(row=0, column=0, padx=5)

btn_adicionar = ttk.Button(frame_botoes, text='Editar', comand=None)
btn_adicionar.grid(row=0, column=1, padx=5)

btn_adicionar = ttk.Button(frame_botoes, text='Remover', comand=None)
btn_adicionar.grid(row=0, column=2, padx=5)

btn_adicionar = ttk.Button(frame_botoes, text='Limpar', comand=None)
btn_adicionar.grid(row=0, column=3, padx=5)

# Tabela de pets
frame_tabela = ttk.Frame(root)
frame_tabela.pack(padx=10, pady=5, fill='both', expand=True)

tree = ttk.Treeview(frame_tabela, columns=('ID', 'Tutor', 'Nome', 'Espécie', 'Raça', 'Idade'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Tutor', text='Tutor')
tree.heading('Nome', text='Nome')
tree.heading('Espécie', text='Espécie')
tree.heading('Raça', text='Raça')
tree.heading('Idade', text='Idade')





root. mainloop()