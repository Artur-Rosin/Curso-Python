while True:
    nota1 = float(input('digite a nota do primeiro bimestre: '))
    if (nota1 <= 10) and (nota1 >= 0):
        break

while True:
    nota2 = float(input('digite a nota do segundo bimestre: '))
    if (nota2 <= 10) and (nota2 >= 0):
        break

while True:
    nota3 = float(input('digite a nota do terceiro bimestre: '))
    if (nota3 <= 10) and (nota3 >= 0):
        break

while True:
    nota4 = float(input('digite a nota do quarto bimestre: '))
    if (nota4 <= 10) and (nota4 >= 0):
        break
#O input sempre retorna uma string. Portanto usamos os comando int(numero) e Float (numero quebrado), na frente do input.

notaTotal = nota1 + nota2+ nota3+ nota4
mediaFinal = notaTotal / 4

print('Nota Total:',notaTotal)
print(f'sua média é {mediaFinal:,.2f}')

#Para não precisar colocar a variavel fora da aspas, usa {f'()'} 
#Se você quiser só mostrar a media direto, pode ser apenas uma variavel, com regra de matematica:
#mediaFinal =(nota1 + nota2 + nota3 + nota4) / 4

if (mediaFinal >= 5 ):
    print('Aluno A P R O V A D O !!!')

elif (mediaFinal >= 3):
    print('Aluno em Recuperação')

else:
    print('Aluno R E P R O V A D O !!!')
      
print('fim do ano letivo')