import random
tabuleiro = []

def criar_tabuleiro():
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')  
            tabuleiro.append(row)

def primeiro_jogador():
        return random.randint(0, 1)

def posicionar( row, col, player):
    if (tabuleiro[row][col] == "O" or tabuleiro[row][col] == "X"):
        return False
    else:
        tabuleiro[row][col] = player
        return True

def vitoria( player):
        win = None

        n = len(tabuleiro)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if tabuleiro[i][j] != player:
                    win = False
                    break
            if win:
                return win

        for i in range(n):
            win = True
            for j in range(n):
                if tabuleiro[j][i] != player:
                    win = False
                    break
            if win:
                return win

        win = True
        for i in range(n):
            if tabuleiro[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if tabuleiro[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in tabuleiro:
            for item in row:
                if item == '-':
                    return False
        return True

def tabuleiro_completo():
        for row in tabuleiro:
            for item in row:
                if item == '-':
                    return False
        return True

def trocar_jogador(player):
        return 'X' if player == 'O' else 'O'

def mostrar_tabuleiro():
        for row in tabuleiro:
            for item in row:
                print(item, end=" ")
            print()

def start():
        criar_tabuleiro()
        print("Modos de jogo:")
        print("1. Jogar com outro jogador")
        print("2. Jogar sozinho com o computador")
        print()
        escolha_valida = False
        while not escolha_valida:
            try:
                modo_de_jogo = int(input("Escolha o modo de jogo (1 ou 2): "))
                if modo_de_jogo >= 3 or modo_de_jogo <= 0:
                    raise Exception()
            except Exception:
                print("Introduza apenas como valor 1 ou 2!\n")
                    
            else:
                escolha_valida = True        

        if (modo_de_jogo == 1):
            jogadorX = input("Introduza o nome do Player 1 (X): ")
            jogadorO = input("Introduza o nome do Player 2 (O): ")
            player = 'X' if primeiro_jogador() == 1 else 'O'
            while True:
                if (player == 'X'):
                    print(f"Turno do(a) {jogadorX}")
                else:
                    print(f"Turno do(a) {jogadorO}")
                print()
                mostrar_tabuleiro()
                print()

               
                valido = False
                while not valido:

                    linha_valida = False
                    while not linha_valida:
                        try:
                            linha = int(input("Introduza o número da linha em que pretende colocar a peça: "))
                            print()
                            if linha >= 4 or linha <= 0:
                                raise Exception
                        except Exception:
                            print("Valor da linha não permitido!")
                            print()
                        except ValueError:
                            print("Por favor introduza um valor numérico!")
                            print()
                        else:
                            linha_valida = True 
                            
                    coluna_valida = False
                    while not coluna_valida:
                        try: 
                            coluna = int(input("Introduza o número da coluna em que pretende colocar a peça: "))
                            print()
                            if coluna >= 4 or coluna <= 0:
                                raise Exception
                        except Exception:
                            print("Valor da coluna não permitido!")
                            print()
                        except ValueError:
                            print("Por favor introduza um valor numérico!")
                            print()
                        else:
                            coluna_valida = True 

                    row, col = list(
                        map(int, [linha , coluna]))
                        
                    try:
                        x = posicionar(row - 1, col - 1, player)
                        print()
                        if x == False:
                            raise Exception()
                    except Exception:
                        print("Casa já ocupada!")
                        print("Escolha outra casa!\n")
                    else:
                        valido = True
                    
                        if vitoria(player):
                            if (player == 'X'):
                                print(f"{jogadorX} ganhou o jogo! :)")
                                print()
                                mostrar_tabuleiro()
                                print()
                                return
                            else:
                                print(f"{jogadorO} ganhou o jogo! :)")
                                print()
                                mostrar_tabuleiro()
                                print()
                                return

                       
                        if tabuleiro_completo():
                            print("Empate!")
                            print()
                            mostrar_tabuleiro()
                            print()
                            break

                        
                        player = trocar_jogador(player)

        elif(modo_de_jogo == 2):
            peca_valida = False
            while not peca_valida:
                try:
                    jogador = str(input("Que peças pretende (X ou O): ")).upper()
                    print(jogador)
                    if jogador != 'X' and jogador != 'O':
                        raise Exception()
                except Exception:
                    print("Introduza apenas X ou O!\n")
                        
                else:
                    peca_valida = True 
            
            player = 'X' if primeiro_jogador() == 1 else 'O'
            while True:
                if (player == jogador):
                    print(f"Turno do jogador")
                    print()
                    mostrar_tabuleiro()
                    print()
                    
                   
                    valido = False
                    while not valido:
                        linha_valida = False
                        while not linha_valida:
                            try:
                                linha = int(input("Introduza o número da linha em que pretende colocar a peça: "))
                                print()
                                if linha >= 4 or linha <= 0:
                                    raise Exception
                            except Exception:
                                print("Valor da linha não permitido!")
                                print()
                            except ValueError:
                                print("Por favor introduza um valor numérico!")
                                print()
                            else:
                                linha_valida = True 
                        coluna_valida = False
                        while not coluna_valida:
                            try: 
                                coluna = int(input("Introduza o número da coluna em que pretende colocar a peça: "))
                                print()
                                if coluna >= 4 or coluna <= 0:
                                    raise Exception
                            except Exception:
                                print("Valor da coluna não permitido!")
                                print()
                            except ValueError:
                                print("Por favor introduza um valor numérico!")
                                print()
                            else:
                                coluna_valida = True 
            
                        row, col = list(
                            map(int, [linha , coluna]))
                        try:
                            x = posicionar(row - 1, col - 1, player)
                            print()
                            if x == False:
                                raise Exception()
                        except Exception:
                            print("Casa já ocupada!")
                            print("Escolha outra casa!\n")
                        else:
                            valido = True
                            if vitoria(player):
                                if (player == jogador):
                                    print(f"Parabéns! Ganhou o jogo! :)")
                                    print()
                                    mostrar_tabuleiro()
                                    print()
                                    return
                                else:
                                    print(f"Perdeu o jogo! :(")
                                    print()
                                    mostrar_tabuleiro()
                                    print()
                                    return

                            if tabuleiro_completo():
                                print("Empate!")
                                print()
                                mostrar_tabuleiro()
                                print()
                                break
                            player = trocar_jogador(player)    
                else:
                    print(f"Turno do computador")
                    print()
                    mostrar_tabuleiro()
                    print()

                    valido = False
                    while not valido:
                        row, col = list(
                            map(int, [random.randint(1, 3), random.randint(1, 3)]))
                        print()
                        try:
                            x = posicionar(row - 1, col - 1, player)
                            print()
                            if x == False:
                                raise Exception()
                        except Exception:
                            print(2)
                        else:
                            valido = True

                            if vitoria(player):
                                if (player == jogador):
                                    print(f"Parabéns! Ganhou o jogo! :)")
                                    print()
                                    mostrar_tabuleiro()
                                    print()
                                    return
                                else:
                                    print(f"Perdeu o jogo! :(")
                                    print()
                                    mostrar_tabuleiro()
                                    print()
                                    return

                            if tabuleiro_completo():
                                print("Empate!")
                                print()
                                mostrar_tabuleiro()
                                print()
                                break
                            player = trocar_jogador(player)


start()