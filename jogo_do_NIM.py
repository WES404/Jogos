def main():
    print("\t...Bem vindo...")
    c = v = 0
    [c,v] = campeonato(c,v)
    print("\nPlacar: Você ", v ," X ", c ," Computador")

def computador_escolhe_jogada(n, m):       
    if m >= n:
        m = n
        print("\nO computador tirou", m, "peças.")
        return m
    else:
        if (n - m) % (m+1) == 0:
            print("\nO computador tirou", m, "peças.")
            return m
        else:
            x = n % 10
            x1 = n // 10
            if x > m and x1 !=0: 
                x = m
            else:
                x = 0
                while n  % (m+1) != 0:
                    n -= 1
                    x += 1 
                if x > m:
                    x = m
                else:
                    m = x
    print("\nO computador tirou", m, "peças.")
    return m            

def usuario_escolhe_jogada(n, m):
    x = int(input("\nQuantas peças você vai tirar? "))
    while x > m or x > n or x <= 0:
        print("\nOops! Jogada inválida! Tente de novo!")
        x = int(input("\nQuantas peças você vai tirar? "))
        
    else:
        m = x
        print("\nVocê tirou", x, "peças.")
        return m

def campeonato(c,v):
    r = int(input("Bem-vindo ao jogo do NIM! Escolha:\n\
          \n1 - para jogar uma partida isolada\
          \n2 - para jogar um campeonato: "))
    z = y = 0
    if r == 1:
        print("\n\t**** Rodada ", r, " ****\n")
        y = partida()
        if y == True:
            c += 1
        else:
            v += 1

    if r == 2:
        r = 1
        while r <= 3:
            print("\n\t**** Rodada", r, " ****\n")
            r += 1
            y = partida()
            if y == True:
                c += 1
            else:
                v += 1
    return c,v
            
def partida():
    n = int(input("Digte o número de peças: "))
    m = int(input("\nDigte o máximo de peças retiradas: "))

    y = z = 0
    
    if n % (m+1) != 0 or n <= m:
        print("\nComputador começa")
        k = computador_escolhe_jogada(n, m)
        n -= k
        print("\nAgora restam", n, "peças no tabuleiro")
        x = 2
        if n == 0:
            y = 1
            print("\nFim do jogo! O computador ganhou!")

    else:
        print("\nVoce começa")
        k = usuario_escolhe_jogada(n, m)
        n -= k
        print("\nAgora restam", n, "peças no tabuleiro")
        x = 1
        if n == 0:
            z = 1
            print("\nFim do jogo! Você ganhou!")
        
    while n > 0:
        if x == 1:
            k = computador_escolhe_jogada(n, m)
            n -= k
            print("\nAgora restam", n, "peças no tabuleiro")
            if n == 0:
                y = 1
                print("\nFim do jogo! O computador ganhou!")
                break
            k = usuario_escolhe_jogada(n, m)
            n -= k
            print("\nAgora restam", n, "peças no tabuleiro")
            if n == 0:
                z = 1
                print("\nFim do jogo! Você ganhou!")
                break
            
        if x == 2:
            k = usuario_escolhe_jogada(n, m)
            n -= k
            print("\nAgora restam", n, "peças no tabuleiro")
            if n == 0:
                z = 1
                print("\nFim do jogo! Você ganhou!")
                break
            k = computador_escolhe_jogada(n, m)
            n -= k
            print("\nAgora restam", n, "peças no tabuleiro")
            if n == 0:
                y = 1
                print("\nFim do jogo! O computador ganhou!")
                break  
    if y == 1:
        return True
    else:
        return False

main()

