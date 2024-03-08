n = int(input('Digite um número: '))
t1 = 0
t2 = 1
c = 3
resposta = bool
while c <= n:
    t3 = t1 + t2
    if t1 == n or t2 == n or t3 == n:
        resposta = True
        break
    else:
        resposta = False
    t1 = t2
    t2 = t3
    c = c + 1
if resposta == True:
    print(f'{n} pertence a sequência!')
else:
    print(f'{n} não pertence a sequência!')
