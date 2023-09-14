import random

def play():
    usuario = input("Qual a sua escolha? 'r' para pedra, 'p' para papel, 't' para tesoura\n")
    computador = random.choice(['r', 'p', 't'])

    if usuario == computador:
        return 'Empate'
    
    # r > t, t > p, p > r
    if ganhar(usuario, computador):
        return 'Você Ganhou!'

    return 'Você perdeu!'

def ganhar(player, opponent):
    # return true if player wins
    # r > t, t > p, p > r
    if (player == 'r' and opponent == 't') or (player == 't' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    
print(play())