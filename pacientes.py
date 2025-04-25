import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json

def carregar_de_json():
    global pacientes, next_nome_id

    arquivo = filedialog.askopenfilename(filetypes=[('Arquivos JSON', '*.json')],
                                         title='Selecionar arquivo JSON para carregar')
    
    if not arquivo: # Seo usuário cancelar
        return
    try:
        with open(arquivo, 'r', encoding= 'utf-8') as f:
            pacientes_carregar = json.load(f)

        # Atualiza a lista de pacientes e o próximo ID
        pacientes = pacientes_carregar
        if pacientes:
            next_nome_id=max(nome['ID']
                            for nome in pacientes)+1
        else:
            next_nome_id = 1

        carregar_pacientes()

        messagebox.showinfo('Sucesso', f'Dados carregados com sucesso de: \n{arquivo}')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao carregar: \n{str(e)}')


def salvar_para_json():
    if not pacientes:
        messagebox.showwarning('Aviso', 'Não há pacientes!')
        return
    
        #Abre a janela para selecionar onde salvar o arquivo.
    arquivo = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[('Arquivo JSON', '*.json')], 
                                           title='Salvar lista de pacientes como JSON')
    if not arquivo: #Se o usuário cancelar
        return
    
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(pacientes, f, ensure_ascii=False, indent=4)
            messagebox.showinfo('Sucesso', f'Dados salvos com suscesso em:')
    
    except Exception as e:
        messagebox.showerror('Erro', f"Ocorreu um erro ao salvar:\n{str(e)}")

def carregar_pacientes(pacientes_list=None):
    for item in tree.get_children():
        tree.delete(item)

    pacientes_to_load = pacientes_list if pacientes_list is not None else pacientes

    for nome in pacientes_to_load:
        tree.insert('', 'end', values=(nome['ID'],
                                       nome['Nome'], nome['Data de nascimento'], nome['Gênero'], nome['Estado civil'], nome['Profissão'], nome['Celular'],))

def adicionar_nome():
    global next_nome_id
    nome = entry_nome.get()
    data_de_nascimento = entry_data_de_nascimento.get()
    gênero = entry_genero.get()
    estado_civil = entry_estado_civil.get()
    profissao = entry_profissao.get()
    celular = entry_celular.get()

    if not nome or not nome:
        messagebox.showerror('Erro', 'Nome e nome de nome são obrigatórios!')
        return
    try:
        profissao_int = int(profissao) if profissao else 0 
    except ValueError:
        messagebox.showerror('Erro', 
                             'Profissao não deve conter número!')
        return
    
    novo_nome = { 'ID': next_nome_id, 'Nome': nome, 'Data de nascimento': data_de_nascimento, 'Gênero': gênero, 'Estado civil': estado_civil, 'Profissao': profissao, 'Celular': celular_int}

    pacientes.append(novo_nome)
    next_nome_id += 1 

    messagebox.showinfo('Sucesso', 'pacientes cadastro com sucesso!')
    limpar_campos
    carregar_pacientes()

def selecionar_nome(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    
    values = tree.item(selected_item)['values']
    limpar_campos()

    entry_nome.insert(0,values[1])
    entry_data_de_nascimento.insert(0,values[2])
    entry_genero.insert(0,values[3])
    entry_estado_civil.insert(0,values[4])
    entry_profissao.insert(0,values[5])
    entry_celular.insert(0, str(values[6])

def limpar_campos():
    entry_nome.delete(0, 'end')
    entry_data_de_nascimento.delete(0, 'end')
    entry_genero.delete(0, 'end')
    entry_estado_civil.delete(0, 'end')
    entry_profissao.delete(0, 'end')
    entry_celular.delete(0, 'end')

def editar_nome():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione um nome para editar!')
        return
    nome_id = tree.item(selected_item)['values'][0]
    nome = entry_nome.get()
    data_de_nascimento = entry_data_de_nascimento.get()
    gênero = entry_gênero.get()
    estado_civil = entry_estado_civil.get()
    profissao = entry_profissao.get()
    celular = entry_celular.get()

    if not nome or not nome:
        messagebox.showerror('Erro', 'Nome e nome do nome são obrigatórios!')
        return
    
    try:
        profissao_int = int(profissao) if profissao else 0
    except ValueError:
        messagebox.showerror('Erro', 'Profissao não deve conter número!')
        return
    for nome in pacientes:
        if nome['ID'] == nome_id:
            nome.update({'Nome': nome, '': data_de_nascimento, 'Data de nascimento': gênero, 'estado_civil': estado_civil, 'Profissao': profissao, 'Celular': celular_int})
            break
    messagebox.showinfo('Sucesso', 'Nome atualizado com sucesso!')
    carregar_pacientes()
                             
def remover_nomet():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione um nome para remover!')
        return
    
    nome_id = tree.item(selected_item)['values'][0]

    if messagebox.askyesno('Confirmação', 'Tem certeja que deseja remover este nome?'):
        global pacientes
        pacientes = [nome for nome in pacientes if nome['ID'] != nome_id]
        messagebox.showinfo('Sucesso', 'Nome removido com sucesso!')
        limpar_campos()
        carregar_pacientes()
     
def pesquisar_por_nome():
    termo_pesquisar = entry_nome.get().lower()

    if not termo_pesquisar:
        carregar_pacientes()
        return
    
    pacientes_encontrados = [nome for nome in pacientes
                        if termo_pesquisar in nome['Nome'].lower()]
    if not pacientes_encontrados:
        messagebox.showinfo('Pesquisa', 'Nenhum nome encontrado para este nome')
        carregar_pacientes()
    else:
        carregar_pacientes(pacientes_encontrados)

# Dados em memória
pacientes = []
next_nome_id = 1

# Configuração da janela principal
root = tk.Tk()
root.title('Sistema de Cadastro de pacientes')
root.geometry('800x500')

# Frame do formulário
frame_form = ttk.LabelFrame(root,
                            text='Pacientes')
frame_form.pack(padx=10, pady=5, fill='x')

# Campos do formulário
ttk.Label(frame_form, text='Nome:').grid(row=0,
                                          column=0, padx=5,pady=5,
                                        sticky='e')
entry_nome = ttk.Entry(frame_form,width=40)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Data de nascimento:').grid(row=1,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_data_de_nascimento = ttk.Entry(frame_form,width=40)
entry_data_de_nascimento.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Gênero:').grid(row=2,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_gênero = ttk.Entry(frame_form,width=40)
entry_gênero.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Estado civil:').grid(row=3,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_estado_civil = ttk.Entry(frame_form,width=40)
entry_estado_civil.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Profissão:').grid(row=4,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_profissao = ttk.Entry(frame_form,width=40)
entry_profissao.grid(row=4, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='celular:').grid(row=5,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_celular = ttk.Entry(frame_form,width=40)
entry_celular.grid(row=5, column=1, padx=5, pady=5)

# Frame de botões
frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=5)

btn_adicionar = ttk.Button(frame_botoes, text='Adicionar', command=adicionar_nome)
btn_adicionar.grid(row=0, column=0, padx=5)

btn_adicionar = ttk.Button(frame_botoes, text='Editar', command=editar_nome)
btn_adicionar.grid(row=0, column=1, padx=5)

btn_adicionar = ttk.Button(frame_botoes, text='Remover', command=remover_nome)
btn_adicionar.grid(row=0, column=2, padx=5)

btn_adicionar = ttk.Button(frame_botoes, text='Limpar', command=limpar_campos)
btn_adicionar.grid(row=0, column=3, padx=5)

btn_adicionar = ttk.Button(frame_botoes, text='Pesquisar Pacientes ', command=pesquisar_por_nome)
btn_adicionar.grid(row=0, column=4, padx=5)

btn_salvar_json = ttk.Button(frame_botoes, text='Salvar', command=salvar_para_json)
btn_salvar_json.grid(row=0, column=5, padx=5)

btn_carregar_de_json = ttk.Button(frame_botoes, text='Carregar Dados', command=carregar_de_json)
btn_carregar_de_json.grid(row=0, column=6, padx=5)


# Tabela de pacientes
frame_tabela = ttk.Frame(root)
frame_tabela.pack(padx=10, pady=5, fill='both', expand=True)

tree = ttk.Treeview(frame_tabela, columns=('ID', 'Nome', 'Data de Nascimento', 'Gênero', 'Estado Civil', 'Profissão', 'Celular'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Nome', text='Nome')
tree.heading('Data de Nascimento', text='Data de Nascimento')
tree.heading('Gênero', text='Gênero')
tree.heading('Estado Civil', text='Estado Civil')
tree.heading('Profissão', text='Profissão')
tree.heading('Celular', text='Celular')

tree.column('ID', width=50)
tree.column('Nome', width=150)
tree.column('Data de Nascimento', width=100)
tree.column('Gênero', width=100)
tree.column('Estado Civil', width=100) 
tree.column('Profissão', width=50)
tree.column('Celular', width=50)

scrollbar = ttk.Scrollbar(frame_tabela, orient='vertical', command=tree.yview) #scrollbar é a barra de rolagem.
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side='left',fill='both',expand= True)
scrollbar.pack(side='right', fill='y')

tree.bind('<<TreeviewSelect>>', selecionar_nome) #o bind fica esperando acontecer alguma coisa.


root. mainloop()