import tkinter 
#Chamado import tkinter para o python puxar da biblioteca tkinter.
root = tkinter.Tk() #Aqui atribuimos um valor ao root, com () para transformar em objeto.
root.title('Hello World gráfico') #Usamos title para dar um nome  a nossa janela.
root.geometry('800x600')#Usamos geometry para definir o tamanho da nossa janela.

labelFrase = tkinter.Label(root,
                           text= 'Olá Developer',
                           font=('Magneto',32),
                           fg='pink',
                           bg='lightblue')
labelFrase.pack(padx=5,pady=5)

labelNome = tkinter.Label(root,
                  text='Digite seu nome',
                  font=('Ariel',32),
                  fg='pink')
labelNome.pack(padx=5,pady=5)

entryNome = tkinter.Entry(root,width=100,
                          font=('Verdana',32))#Se vc quiser ocultar o que a pessoa digitar, coloque (root,show='#')
entryNome.pack(padx=5
               ,pady=5)

buttonGravar = tkinter.Button(root,
                              text='Gravar',
                              command=None)
buttonGravar.pack(padx=5,pady=5)

root.mainloop()