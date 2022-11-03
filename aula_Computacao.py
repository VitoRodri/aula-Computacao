import random
deck_player=[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]
deck_NPC=[1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

def baralhar(deck_player,deck_NPC):
    random.shuffle(deck_player)
    random.shuffle(deck_NPC)
baralhar(deck_player,deck_NPC)

def show_deck(deck_player,deck_NPC):
    print("deck do player:"+ str(deck_player))
    print("deck do computador:"+str(deck_NPC))
show_deck(deck_player,deck_NPC)

def fish(deck_player, deck_NPC):
    x=[deck_player[13], deck_player[12]]
    y=[deck_NPC[13],deck_NPC[12]]
    print("cartas do player"+str(x))
    print("cartas do computador"+str(y))
    return x,y
x,y=fish(deck_player,deck_NPC)


def discard(x):
    a=True
    while a==True:
        print("Do you want to discard a card?")
        n=input()
        if n=="yes":
            print("dicard all, the first or the second card?")
            i=input()
            if i=="all":
                random.shuffle(deck_player)
                show_deck(deck_player,deck_NPC)
                fish(deck_player,deck_NPC)
            elif i=="first":
                del(deck_player[12])
                random.shuffle(deck_player)
                show_deck(deck_player,deck_NPC)
                x[0]=deck_player[12]
                print("cartas do player"+str(x))
                print("cartas do computador"+str(y))
            elif i=="second":
                del(deck_player[13])
                random.shuffle(deck_player)
                show_deck(deck_player,deck_NPC)
                x[1]=deck_player[12]
                print("cartas do player"+str(x))
                print("cartas do computador"+str(y))
            else:
                print("Could not understand")
        else:
            a=False

discard(x)

            


def player(x):
    soma=0
    if x[0]=="J" :
        soma=soma+11
    elif x[0]=="Q" :
        soma=soma+12
    elif x[0]=="K" :
        soma=soma+13
    elif x[0]=="A" :
        soma=soma+14
    elif 0<x[0]<11:
        soma=soma+x[0]
    elif 0<x[1]<11:
        soma=soma+x[1]
    else :
        print("error")
    if x[1]=="J":
        soma=soma+11
    elif x[1]=="Q":
        soma=soma+12
    elif x[1]=="K":
        soma=soma+13
    elif x[1]=="A":
        soma=soma+14
    elif 0<x[1]<11:
        soma=soma+x[1]
    else:
        print("error")
    return soma
soma=player(x)

def npc(y):
    soma1=0
    if y[0]=="J" :
        soma1=soma1+11
    elif y[0]=="Q" :
        soma1=soma1+12
    elif y[0]=="K" :
        soma1=soma1+13
    elif y[0]=="A" :
        soma1=soma1+14
    elif 0<y[0]<11:
        soma1=soma1+y[0]
    else :
        print("error")
    if y[1]=="J":
        soma1=soma1+11
    elif y[1]=="Q":
        soma1=soma1+12
    elif y[1]=="K":
        soma1=soma1+13
    elif y[1]=="A":
        soma1=soma1+14
    elif 0<y[1]<11:
        soma1=soma1+y[1]
    else:
        print("error")
    return soma1
soma1=npc(y)

def comparar(soma,soma1):
    print("pontos do jogador "+str(soma))
    print("pontos do computador "+ str(soma1))
    if soma>soma1:
        print("player wins")
    elif soma1>soma:
        print("Computer wins")
    elif soma==soma1:
        print("empate")
    else:
        print("error")
comparar(soma,soma1)


