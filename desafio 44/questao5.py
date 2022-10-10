nt1 = int(input('digite a primeira nota do aluno: '))
nt2 = int(input('digite a segunda nota do aluno: '))
nt3 = int(input('digite a terceira nota do aluno: '))

media = (nt1 + nt2 + nt3) /3

if media >= 6:
    print('aprovado')
else:
    print('reprovado')