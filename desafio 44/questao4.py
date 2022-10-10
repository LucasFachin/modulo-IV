num = int(input('digite um  numero inteiro, sempre 1 mais do numero normal: '))
for n in range(1, num):
    if n % 2 == 1:
        print(n, end=' ')
print('acabou')