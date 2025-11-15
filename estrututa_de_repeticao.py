#repetição com FOR
print ('Sistemas de voltas')
for voltas in range (1,11):
    print(f'{voltas}ª volta')

print ('='*30)

#repetição com WHILE

while True:
    number = int(input('Informe um numero positivo: '))
    if number > 0:
        print(f'Seu numero e o "{number}"')
        break
    else:
        print('Isso nao e um numero')
    

