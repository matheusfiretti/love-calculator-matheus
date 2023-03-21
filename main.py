nome1 = input()
nome2 = input()

lower_nome1 = nome1.lower()
lower_nome2 = nome2.lower()
comb = nome1 + nome2
soma1 = 0
soma2 = 0

for i in 'true':
    c1 = comb.count(i)
    soma1 += c1

for i in 'love':
    c2 = comb.count(i)
    soma2 += c2

perc = str(soma1) + str(soma2)
print(perc)

if int(perc) < 10 or int(perc) > 90:
    print(f'Sua pontuação é {perc}')
elif 40 < int(perc) < 50:
    print(f'Sua pontuação é {perc}, tudo bem!')
else:
    print(f'Pontuação: {perc}')
