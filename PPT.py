import random 

opcoes = ['Pedra', 'Papel', 'Tesoura']
Computador = random.choice(opcoes)


jogador = input('Jogue Pedra, Papel ou Tesoura: ')
print(f'Voce jogou: {jogador}')
print(f'Computador jogou: {Computador}')

if jogador == Computador:
    print('Empate!')

elif (jogador == 'Pedra' and Computador == 'Tesoura') or (jogador == 'Papel' and Computador == 'Pedra') or (jogador == 'Tesoura' and Computador == 'Papel'):
    print('Voce venceu!')

else:
    print('Computador venceu!')

print('Fim do jogo!')
