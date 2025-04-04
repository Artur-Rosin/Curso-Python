import tkinter as tk

def fnAdicao():
    x = float(entryNumero1.get())
    y = float(entryNumero2.get())
    resultado = x + y
    lblResultado.config(text=f'A soma é {resultado}')

def fnSubtracao():
    x = float(entryNumero1.get())
    y = float(entryNumero2.get())
    resultado = x - y
    lblResultado.config(text=f'A subtracao é {resultado}')

def fnMultiplicacao():
    x = float(entryNumero1.get())
    y = float(entryNumero2.get())
    resultado = x * y
    lblResultado.config(text=f'A multiplicacao é {resultado}')

def fnDivisao():
    x = float(entryNumero1.get())
    y = float(entryNumero2.get())
    resultado = x / y
    lblResultado.config(text=f'A divisao é {resultado}')



janela = tk. Tk() #Desenha uma janela.
janela.title('WinCalc - a super calculadora')
janela.geometry('800x600') #Tamanho da janela.

lblTitulo = tk.Label(janela,
                     text='WinCalc',
                     font=('Pristina',22),
                     fg='White',
                     bg='Black',
                     width=800,
                     justify='left')
lblTitulo.pack(padx=5,pady=5)

lblNumero1 = tk.Label(janela,
                      text='Digite um número',
                      font=('Calibri', 20))
lblNumero1.pack(padx=5,pady=5)

entryNumero1 = tk.Entry(janela,
                       width=90,
                       font=('Calibri',))
entryNumero1.pack(padx=5,pady=5)

lblNumero2 = tk.Label(janela,
                      text='Digite outro número',
                      font=('Calibri', 30))
lblNumero2.pack(padx=5,pady=5)

entryNumero2 = tk.Entry(janela,
                       width=90,
                       font=('Calibri',))
entryNumero2.pack(padx=5,pady=5)

btnAdicao = tk.Button(janela,
                     text='Adição',
                      font=('calibri',16),
                      width=15,
                      command=fnAdicao)
btnAdicao.pack(padx=5,pady=5)

btnAdicao = tk.Button(janela,
                     text='Subtração',
                      font=('calibri',16),
                      width=15,
                      command=fnSubtracao)
btnAdicao.pack(padx=5,pady=5)

btnAdicao = tk.Button(janela,
                     text='Multiplicação',
                      font=('calibri',16),
                      width=15,
                      command=fnMultiplicacao)
btnAdicao.pack(padx=5,pady=5)

btnAdicao = tk.Button(janela,
                     text='Divisão',
                      font=('calibri',16),
                      width=15,
                      command=fnDivisao)
btnAdicao.pack(padx=5,pady=5)

lblResultado = tk.Label(janela,
                        text='0.00',
                        font=('calibri',22))
lblResultado.pack(padx=5,pady=5)
                      

janela.mainloop() #Mantem o programa rodando.