# Esse programa tem objetivo de ser um gerador de numeros aleatorios. #

# implantar um gerador de numeros aleatorio
import random
anuncio =" Bem vindo ao jogo dos Dados Loucos"
anuncio2 = " Ele consiste em você adivinhar se o proximo valor a sair  sera maior ou menor que o valor anterior."
win = "     !!! Parabens você acertou o resultado. S2"
lose = "       XXX Bom não foi dessa vez, mais sorte na proxima"
print(anuncio)
print(anuncio2)
x = True
Pontos = 0
UltimoValor = 2
ValorAtual = 0
def roll() : # Roll de dados
    D11 = random.randrange(1,7,1)
    D12 = random.randrange(1,7)
    global ValorAtual 
    ValorAtual = D11 + D12
    print("Os Resultados foram", D11," &", D12, "dando um Totdal de:",ValorAtual)
    
while x : #Repetição para o jogo seguir
    
    print("O valor Atual È", UltimoValor, "você tem ", Pontos, " Pontos Acumulados.")
    print("Escolha o proximo dado sera maior ou menor?? (M/m)")
    r = input()
    if r == "M" or r == "m" :
        print("Escolha:", r, "Seu Numero: ", UltimoValor)
    else:
        while r != "M" or r != "m": # Validador 
            print("Opa meu amigo, escolha entre M ou m, vamos fcilitar as coisas.")
            r = input()
            if r == "M" or r == "m" :
                print("Boa escolha:", r)
                break
                
    roll()
    if  ValorAtual > UltimoValor :
        if r =="M":
            print(win)
            Pontos = Pontos +1
        else :
            print(lose)
            break
    if  ValorAtual < UltimoValor :
        if r =="m":
            print(win)
            Pontos = Pontos +1
        else :
            print(lose)
            break
    if  ValorAtual == UltimoValor :
        print("Empate??? então deu Pizza")

    UltimoValor = ValorAtual


print("Fim de Jogo")

