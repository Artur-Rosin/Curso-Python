import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json

def carregar_de_json():
    global s, next_paciente_id

    arquivo = filedialog.askopenfilename(filetypes=[('Arquivos JSON', '*.json')],
                                         title='Selecionar arquivo JSON para carregar')
    
    if not arquivo: # Seo usuário cancelar
        return
    try:
        with open(arquivo, 'r', encoding= 'utf-8') as f:
            paciente_carregar = json.load(f)

        # Atualiza a lista de paciente e o próximo ID
        paciente = paciente_carregar
        if paciente:
            next_paciente_id=max(paciente['ID']
                            for paciente in paciente)+1
        else:
            next_paciente_id = 1

        carregar_paciente()

        messagebox.showinfo('Sucesso', f'Dados carregados com sucesso de: \n{arquivo}')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao carregar: \n{str(e)}')


def salvar_para_json():
    if not paciente:
        messagebox.showwarning('Aviso', 'Não há paciente!')
        return
    
        #Abre a janela para selecionar onde salvar o arquivo.
    arquivo = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[('Arquivo JSON', '*.json')], 
                                           title='Salvar lista de paciente como JSON')
    if not arquivo: #Se o usuário cancelar
        return
    
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(paciente, f, ensure_ascii=False, indent=4)
            messagebox.showinfo('Sucesso', f'Dados salvos com suscesso em:')
    
    except Exception as e:
        messagebox.showerror('Erro', f"Ocorreu um erro ao salvar:\n{str(e)}")

def carregar_paciente(paciente_list=None):
    for item in tree.get_children():
        tree.delete(item)

    paciente_to_load = paciente_list if paciente_list is not None else paciente

    for paciente in paciente_to_load:
        tree.insert('', 'end', values=(paciente['ID'],
                                       paciente['Nome'], paciente['Data de nascimento'], paciente['Gênero'], paciente['Estado civil'], paciente['Profissão'], paciente['Celular'],))

def adicionar_paciente():
    global next_paciente_id
    nome = entry_nome.get()
    data_de_nascimento = entry_data_de_nascimento.get()
    gênero = entry_genero.get()
    estado_civil = entry_estado_civil.get()
    profissao = entry_profissao.get()
    celular = entry_celular.get()

    if not paciente or not paciente:
        messagebox.showerror('Erro', 'Nome do paciente é obrigatórios!')
        return
    try:
        profissao_int = int(profissao) if profissao else 0 
    except ValueError:
        messagebox.showerror('Erro', 
                             'Profissao não deve conter número!')
        return
    
    novo_paciente = { 'ID': next_paciente_id, 'Nome': nome, 'Data de nascimento': data_de_nascimento, 'Gênero': gênero, 'Estado civil': estado_civil, 'Profissao': profissao, 'Celular': celular_int}

    paciente.append(novo_paciente)
    next_paciente_id += 1 

    messagebox.showinfo('Sucesso', 'Paciente cadastro com sucesso!')
    limpar_campos
    carregar_paciente()

def selecionar_paciente(event):
    selected_item = tree.selection()
    if not selected_item:
        return
    
    values = tree.item(selected_item)['values']
    limpar_campos()

    entry_nome.insert(0,values[1])
    entry_data_de_nascimento.insert(0,values[2])
    entry_genero_de_nascimento.insert(0,values[3])
    entry_estado_civil.insert(0,values[4])
    entry_profissao.insert(0,values[5])
    entry_celular.insert(0, str(values[6]))

def limpar_campos():
    entry_nome.delete(0, 'end')
    entry_data_de_nascimento.delete(0, 'end')
    entry_genero_de_nascimento.delete(0, 'end')
    entry_estado_civil.delete(0, 'end')
    entry_profissao.delete(0, 'end')
    entry_celular.delete(0, 'end')

def editar_paciente():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione um paciente para editar!')
        return
    paciente_id = tree.item(selected_item)['values'][0]
    paciente = entry_paciente.get()
    data_de_nascimento = entry_data_de_nascimento.get()
    gênero = entry_gênero_de_nascimento.get()
    estado_civil = entry_estado_civil.get()
    profissao = entry_profissao.get()
    celular = entry_celular.get()

    if not paciente or not paciente:
        messagebox.showerror('Erro', 'Nome do paciente é obrigatórios!')
        return
    
    try:
        profissao_int = int(profissao) if profissao else 0
    except ValueError:
        messagebox.showerror('Erro', 'Profissao não deve conter número!')
        return
    for paciente in paciente:
        if paciente['ID'] == paciente_id:
            paciente.update({'Paciente': paciente, '': data_de_nascimento, 'Data de nascimento': gênero, 'estado_civil': estado_civil, 'Profissao': profissao, 'Celular': celular_int})
            break
    messagebox.showinfo('Sucesso', 'Paciente atualizado com sucesso!')
    carregar_paciente()
                             
def remover_paciente():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione um paciente para remover!')
        return
    
    paciente_id = tree.item(selected_item)['values'][0]

    if messagebox.askyesno('Confirmação', 'Tem certeja que deseja remover este paciente?'):
        global paciente
        paciente = [paciente for paciente in paciente if paciente['ID'] != paciente_id]
        messagebox.showinfo('Sucesso', 'Paciente removido com sucesso!')
        limpar_campos()
        carregar_paciente()
     
def pesquisar_por_paciente():
    termo_pesquisar = entry_paciente.get().lower()

    if not termo_pesquisar:
        carregar_paciente()
        return
    
    paciente_encontrados = [paciente for paciente in paciente
                        if termo_pesquisar in paciente['Paciente'].lower()]
    if not paciente_encontrados:
        messagebox.showinfo('Pesquisa', 'Nenhum paciente encontrado para este nome')
        carregar_paciente()
    else:
        carregar_paciente(paciente_encontrados)

# Dados em memória
paciente = []
next_paciente_id = 1

# Configuração da janela principal
root = tk.Tk()
root.title('Sistema de Cadastro de pacientes')
root.geometry('800x500')

# Frame do formulário
frame_form = ttk.LabelFrame(root,
                            text='pacientes')
frame_form.pack(padx=10, pady=5, fill='x')

# Campos do formulário
ttk.Label(frame_form, text='Paciente:').grid(row=0,
                                          column=0, padx=5,pady=5,
                                        sticky='e')
entry_nome = ttk.Entry(frame_form,width=40)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Data de nascimento:').grid(row=1,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_data_de_nascimento = ttk.Entry(frame_form,width=40)
entry_data_de_nascimento.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Estado civil:').grid(row=2,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_estado_civil = ttk.Entry(frame_form,width=40)
entry_estado_civil.grid(row=2, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='Profissão:').grid(row=3,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_profissao = ttk.Entry(frame_form,width=40)
entry_profissao.grid(row=3, column=1, padx=5, pady=5)

ttk.Label(frame_form, text='celular:').grid(row=4,
                                          column=0, padx=5, pady=5,
                                        sticky='e')
entry_celular = ttk.Entry(frame_form,width=40)
entry_celular.grid(row=4, column=1, padx=5, pady=5)

# Radio Buttons para Gênero  
tk.Label(frame_form, text='Genero de nascimento:').grid(row=1,
                                          column=3, padx=5, pady=5,
                                          sticky='e')

opcoes =[  
        ("Feminino", "Feminino"),  
        ("Masculino", "Masculino")] 

genero_selecionado = tk.StringVar(value="None")  # Valor padrão  

for i, (texto, valor) in enumerate(opcoes):  # Adicione 'enumerate' aqui!
    tk.Radiobutton(
        frame_form, 
        text=texto, 
        variable=genero_selecionado, 
        value=valor
    ).grid(
        row=2 + i,  # Agora 'i' está definido pelo enumerate
        column=3, 
        padx=5, 
        pady=5, 
        sticky='e'
    )

# Frame de botões
frame_botoes = ttk.Frame(root)
frame_botoes.pack(pady=5)

btn_adicionar = ttk.Button(frame_botoes, text='Adicionar', command=adicionar_paciente)
btn_adicionar.grid(row=0, column=0, padx=5)

btn_adicionar = ttk.Button(frame_botoes, text='Editar', command=editar_paciente)
btn_adicionar.grid(row=0, column=1, padx=5)

btn_adicionar = ttk.Button(frame_botoes, text='Remover', command=remover_paciente)
btn_adicionar.grid(row=0, column=2, padx=5)

btn_adicionar = ttk.Button(frame_botoes, text='Limpar', command=limpar_campos)
btn_adicionar.grid(row=0, column=3, padx=5)

btn_adicionar = ttk.Button(frame_botoes, text='Pesquisar Pacientes ', command=pesquisar_por_paciente)
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

tree.bind('<<TreeviewSelect>>', selecionar_paciente) #o bind fica esperando acontecer alguma coisa.


root. mainloop()