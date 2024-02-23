import tkinter
from tkinter import *
from tkinter import ttk

# Cores -----------------------------------------------------

cor  = ""
cor0 = "#FFFFFF"  #  Branco
cor1 = "#333333"  #  Preto Forte
cor2 = "#fcc058"  #  Laranja
cor3 = "#38576b"  #  Branco
cor4 = "#3297a8"  #  Azul
cor5 = "#fff873"  #  Amarelo
cor6 = "#f3f16b"  #  Laranja
cor7 = "#e85151"  #  Vermelho
cor8 = "#236112"  #  Verde Oliva escuro
cor9 = "#556b2f"  #  Verde Oliva
cor10 = "#fcfbf7"  
fundo = "#3b3b3b"  #  Preto

# Criando Janela Principal-------------------------------------

janela = Tk()
janela.title('Jogo da Velha')
janela.geometry('270x480')
janela.configure(bg=fundo)

# Criando divisões da janela-------------------------------------------------------------------------------------------------------------------
frame_cima = Frame(janela, width=245, height=160, bg=cor1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=13, pady=10)
frame_jogadores = Frame(janela, width=245, height=235, bg=cor2, relief="flat")
frame_jogadores.grid(row=1, column=0, sticky=NW, padx=13, pady=5)

# Dividindo Frame Dados do jogador  : ------------------------------------------------------------------------------------------------------------------

lbl_nome_X = Label(frame_jogadores, text='Nome Jogador X: ', height=1, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor7)
# lbl_partidas.place(x=150, y=5) # Podria usar pra definir o posicionamento dentro do Frame tipo oque ocorre dentro do frame_cima
lbl_nome_X.grid(row=0, column=0, sticky=NW, pady=2)
edt_jogador_X = Entry(frame_jogadores, text= 'Jogador 0', width=34, font=('Ivy 10 bold'),)
edt_jogador_X.grid(row=1, column=0)
edt_jogador_X.insert(0, 'Jogador X')
lbl_nome_O = Label(frame_jogadores, text='Nome Jogador O: ', height=1, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor2, fg=cor4)
# lbl_partidas.place(x=150, y=5) # Podria usar pra definir o posicionamento dentro do Frame tipo oque ocorre dentro do frame_cima
lbl_nome_O.grid(row=2, column=0, sticky=NW, pady=2)
edt_jogador_O = Entry(frame_jogadores, text= 'Jogador O', width=34, font=('Ivy 10 bold'))
edt_jogador_O.grid(row=3, column=0)
edt_jogador_O.insert(0, 'Jogador O')
# Dividindo Frame de cima  : ------------------------------------------------------------------------------------------------------------------
lbl_dois_pontos = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor5)
lbl_dois_pontos.place(x=125, y=45)
lbl_placar = Label(frame_cima, text='Placar', height=1, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor1, fg=cor2)
lbl_placar.place(x=15, y=2)
# Dividindo Frame de cima - contador de partidas
lbl_partidas = Label(frame_cima, text='Partidas: ', height=1, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
lbl_partidas.place(x=150, y=5)
lbl_partidas_quant = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor1, fg=cor0)
lbl_partidas_quant.place(x=220, y=2)
# Dividindo Frame de cima - X 
lbl_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=cor1, fg=cor7)
lbl_x.place(x=25, y=40)
lbl_x_jogador1 = Label(frame_cima, text='Jogador 01', height=1, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
lbl_x_jogador1.place(x=15, y=100)
lbl_x_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0)
lbl_x_pontos.place(x=90, y=50)
# Dividindo Frame de cima -  O 
lbl_o = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=cor1, fg=cor4)
lbl_o.place(x=190, y=40)
lbl_o_jogador2 = Label(frame_cima, text='Jogador 02', height=1, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
lbl_o_jogador2.place(x=165, y=100)
lbl_o_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0)
lbl_o_pontos.place(x=150, y=50)
# Dividindo Frame de cima - contador de empates
lbl_empate = Label(frame_cima, text='Empates: ', height=1, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor1, fg=cor0)
lbl_empate.place(x=15, y=125)
lbl_empate_quant = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor1, fg=cor0)
lbl_empate_quant.place(x=125, y=125)

# Criando funções e variáveis-------------------------------------
# Variáveis

X_ = 'X'
O_ = 'O'
jogador_1 = X_
jogador_2 = O_

matriz = [
          ['00','01','02'],
          ['10','11','12'],
          ['20','21','22']
]

jogando = X_
jogar   = ''
placar_X = 0
placar_O = 0
placar_E = 0
quant_partidas = 0
novo_jogo = 'Jogar'

#  funções-------------------------------------------------------------------------------------------------------------------------------------
def iniciar_jogo():
    global quant_partidas
    global contador        
    global ganhou
    contador = 0
    ganhou = False 
    matriz = [
          ['00','01','02'],
          ['10','11','12'],
          ['20','21','22']
    ]

    # marca a quantidade de partida
    quant_partidas += 1
    lbl_partidas_quant['text'] = str(quant_partidas)   

    # trocando valores do botão de jogar
    btn_jogar['text'] = 'Novo Jogo'
    lbl_x_jogador1['text'] = edt_jogador_X.get()
    lbl_o_jogador2['text'] = edt_jogador_O.get()
    

     #  para decidir o vencedor
    def venceu_partida(j, i):
        venceu = ''
        global placar_X
        global placar_O
        global placar_E
        
        # 1 - vencedor de X ou O na primeira linha 0
        if matriz[0][0] == X_ and matriz[0][1] == X_ and matriz[0][2] == X_:
            placar_X += 1
            venceu = j
        elif matriz[0][0] == O_ and matriz[0][1] == O_ and matriz[0][2] == O_:
            placar_O += 1
            venceu = j
        # 2 - vencedor de X ou O na segunda linha 1
        elif matriz[1][0] == X_ and  matriz[1][1] == X_ and  matriz[1][2] == X_:
            placar_X += 1
            venceu = j
        elif matriz[1][0] == O_ and matriz[1][1] == O_ and matriz[1][2] == O_:
            placar_O += 1
            venceu = j
        # 3 - vencedor de X ou O na terceira linha 2
        elif matriz[2][0] == X_ and matriz[2][1] == X_ and matriz[2][2] == X_:
            placar_X += 1
            venceu = j
        elif matriz[2][0] == O_ and matriz[2][1] == O_ and matriz[2][2] == O_:
            placar_O += 1
            venceu = j
        # 4 - vencedor de X ou O na primeira Coluna 0
        elif matriz[0][0] == X_ and matriz[1][0] == X_ and matriz[2][0] == X_:
            placar_X += 1
            venceu = j
        elif matriz[0][0] == O_ and matriz[1][0] == O_ and matriz[2][0] == O_:
            placar_O += 1
            venceu = j
        # 5 - vencedor de X ou O na segunda Coluna 1
        elif matriz[0][1] == X_ and matriz[1][1] == X_ and matriz[2][1] == X_:
            placar_X += 1
            venceu = j
        elif matriz[0][1] == O_ and matriz[1][1] == O_ and matriz[2][1] == O_:
            placar_O += 1
            venceu = j
        # 6 - vencedor de X ou O na terceira Coluna 2
        elif matriz[0][2] == X_ and matriz[1][2] == X_ and matriz[2][2] == X_:
            placar_X += 1
            venceu = j
        elif matriz[0][2] == O_ and matriz[1][2] == O_ and matriz[2][2] == O_:
            placar_O += 1
            venceu = j
        # 7 - vencedor de X ou O na primeira diagonal Esquerda para Direita
        elif matriz[0][0] == X_ and matriz[1][1] == X_ and matriz[2][2] == X_:
            placar_X += 1
            venceu = j
        elif matriz[0][0] == O_ and matriz[1][1] == O_ and matriz[2][2] == O_:
            placar_O += 1
            venceu = j
        # 8 - vencedor de X ou O na primeira diagonal Direita para Esquerda
        elif matriz[0][2] == X_ and matriz[1][1] == X_ and matriz[2][0] == X_:
            placar_X += 1
            venceu = j
        elif matriz[0][2] == O_ and matriz[1][1] == O_ and matriz[2][0] == O_:
            placar_O += 1
            venceu = j
        elif i == 9:
            placar_E += 1
            venceu = 'E'

        if j == venceu:
            if venceu == X_:
                lbl_x_pontos['text'] = str(placar_X)
                return  True
            elif venceu == O_:
                lbl_o_pontos['text'] = str(placar_O)
                return  True
        elif venceu == 'E':
                lbl_empate_quant['text'] = str(placar_E)
                return  True
        else:
            return False
        
    #  para controlar as jogadas
    def controles(i):
        global jogando
        global jogar
        global contador        
        global ganhou
        # if contador == 9 and ganhou == True:
        #     ganhou = False
        #     contador = 0
        #  Verificando posição jogada
        if i==str('00'):
            #  Verificando se posição esta vazia
            if btn_linha0_bt0['text'] == '':
                #  verificar quem esta jogando e definir a cor do simbolo
                if jogando == X_:
                    cor = cor7
                elif jogando == O_:
                    cor = cor8
            
                #  definir a cor do texto do botão
                #  marcar aquela posição na tabela
                #  com o valor do jogador atual
                btn_linha0_bt0['fg'] = cor
                btn_linha0_bt0['text'] = jogando
                matriz[0][0] = jogando
                contador += 1
                if contador >= 5 and ganhou == False:
                    ganhou = venceu_partida(jogando, contador)

                #  trocar jogador
                if jogando == X_:
                    jogando = O_
                    jogar = 'Jogador 1'
                elif jogando == O_:
                    jogando = X_
                    jogar = 'Jogador 2'
        
        elif i==str('01'):
            #  Verificando se posição esta vazia
            if btn_linha0_bt1['text'] == '':
                #  verificar quem esta jogando e definir a cor do simbolo
                if jogando == X_:
                    cor = cor7
                elif jogando == O_:
                    cor = cor8
            
                #  definir a cor do texto do botão
                #  marcar aquela posição na tabela
                #  com o valor do jogador atual
                btn_linha0_bt1['fg'] = cor
                btn_linha0_bt1['text'] = jogando
                matriz[0][1] = jogando
                contador += 1
                if contador >= 5 and ganhou == False:
                    ganhou = venceu_partida(jogando, contador)

                #  trocar jogador
                if jogando == X_:
                    jogando = O_
                    jogar = 'Jogador 1'
                elif jogando == O_:
                    jogando = X_
                    jogar = 'Jogador 2'

        elif i==str('02'):
            #  Verificando se posição esta vazia
            if btn_linha0_bt2['text'] == '':
                #  verificar quem esta jogando e definir a cor do simbolo
                if jogando == X_:
                    cor = cor7
                elif jogando == O_:
                    cor = cor8
            
                #  definir a cor do texto do botão
                #  marcar aquela posição na tabela
                #  com o valor do jogador atual
                btn_linha0_bt2['fg'] = cor
                btn_linha0_bt2['text'] = jogando
                matriz[0][2] = jogando
                contador += 1
                if contador >= 5 and ganhou == False:
                    ganhou = venceu_partida(jogando, contador)

                #  trocar jogador
                if jogando == X_:
                    jogando = O_
                    jogar = 'Jogador 1'
                elif jogando == O_:
                    jogando = X_
                    jogar = 'Jogador 2'

        elif i==str('10'):
            #  Verificando se posição esta vazia
            if btn_linha1_bt0['text'] == '':
                #  verificar quem esta jogando e definir a cor do simbolo
                if jogando == X_:
                    cor = cor7
                elif jogando == O_:
                    cor = cor8
            
                #  definir a cor do texto do botão
                #  marcar aquela posição na tabela
                #  com o valor do jogador atual
                btn_linha1_bt0['fg'] = cor
                btn_linha1_bt0['text'] = jogando
                matriz[1][0] = jogando
                contador += 1
                if contador >= 5 and ganhou == False:
                    ganhou = venceu_partida(jogando, contador)

                #  trocar jogador
                if jogando == X_:
                    jogando = O_
                    jogar = 'Jogador 1'
                elif jogando == O_:
                    jogando = X_
                    jogar = 'Jogador 2'

        elif i==str('11'):
            #  Verificando se posição esta vazia
            if btn_linha1_bt1['text'] == '':
                #  verificar quem esta jogando e definir a cor do simbolo
                if jogando == X_:
                    cor = cor7
                elif jogando == O_:
                    cor = cor8
            
                #  definir a cor do texto do botão
                #  marcar aquela posição na tabela
                #  com o valor do jogador atual
                btn_linha1_bt1['fg'] = cor
                btn_linha1_bt1['text'] = jogando
                matriz[1][1] = jogando
                contador += 1
                if contador >= 5 and ganhou == False:
                    ganhou = venceu_partida(jogando, contador)

                #  trocar jogador
                if jogando == X_:
                    jogando = O_
                    jogar = 'Jogador 1'
                elif jogando == O_:
                    jogando = X_
                    jogar = 'Jogador 2'

        elif i==str('12'):
            #  Verificando se posição esta vazia
            if btn_linha1_bt2['text'] == '':
                #  verificar quem esta jogando e definir a cor do simbolo
                if jogando == X_:
                    cor = cor7
                elif jogando == O_:
                    cor = cor8
            
                #  definir a cor do texto do botão
                #  marcar aquela posição na tabela
                #  com o valor do jogador atual
                btn_linha1_bt2['fg'] = cor
                btn_linha1_bt2['text'] = jogando
                matriz[1][2] = jogando
                contador += 1
                if contador >= 5 and ganhou == False:
                    ganhou = venceu_partida(jogando, contador)

                #  trocar jogador
                if jogando == X_:
                    jogando = O_
                    jogar = 'Jogador 1'
                elif jogando == O_:
                    jogando = X_
                    jogar = 'Jogador 2'

        elif i==str('20'):
            #  Verificando se posição esta vazia
            if btn_linha2_bt0['text'] == '':
                #  verificar quem esta jogando e definir a cor do simbolo
                if jogando == X_:
                    cor = cor7
                elif jogando == O_:
                    cor = cor8
            
                #  definir a cor do texto do botão
                #  marcar aquela posição na tabela
                #  com o valor do jogador atual
                btn_linha2_bt0['fg'] = cor
                btn_linha2_bt0['text'] = jogando
                matriz[2][0] = jogando
                contador += 1
                if contador >= 5 and ganhou == False:
                    ganhou = venceu_partida(jogando, contador)

                #  trocar jogador
                if jogando == X_:
                    jogando = O_
                    jogar = 'Jogador 1'
                elif jogando == O_:
                    jogando = X_
                    jogar = 'Jogador 2'

        elif i==str('21'):
            #  Verificando se posição esta vazia
            if btn_linha2_bt1['text'] == '':
                #  verificar quem esta jogando e definir a cor do simbolo
                if jogando == X_:
                    cor = cor7
                elif jogando == O_:
                    cor = cor8
            
                #  definir a cor do texto do botão
                #  marcar aquela posição na tabela
                #  com o valor do jogador atual
                btn_linha2_bt1['fg'] = cor
                btn_linha2_bt1['text'] = jogando
                matriz[2][1] = jogando
                contador += 1
                if contador >= 5 and ganhou == False:
                    ganhou = venceu_partida(jogando, contador)

                #  trocar jogador
                if jogando == X_:
                    jogando = O_
                    jogar = 'Jogador 1'
                elif jogando == O_:
                    jogando = X_
                    jogar = 'Jogador 2'

        elif i==str('22'):
            #  Verificando se posição esta vazia
            if btn_linha2_bt2['text'] == '':
                #  verificar quem esta jogando e definir a cor do simbolo
                if jogando == X_:
                    cor = cor7
                elif jogando == O_:
                    cor = cor8
            
                #  definir a cor do texto do botão
                #  marcar aquela posição na tabela
                #  com o valor do jogador atual
                btn_linha2_bt2['fg'] = cor
                btn_linha2_bt2['text'] = jogando
                matriz[2][2] = jogando
                contador += 1
                if contador >= 5 and ganhou == False:
                    ganhou = venceu_partida(jogando, contador)

                #  trocar jogador
                if jogando == X_:
                    jogando = O_
                    jogar = 'Jogador 1'
                elif jogando == O_:
                    jogando = X_
                    jogar = 'Jogador 2'
    
        print(matriz)

    # def cpuJoga():
    #     global jogadas
    #     global quemJoga
    #     global maxJogadas
    #     if quemJoga == 1 and jogadas < maxJogadas:
    #         l = random.randrange(0,3)
    #         l = random.randrange(0,3)
    #         while velha[l][c] != " ":
    #             l = random.randrange(0,3)
    #             l = random.randrange(0,3)
    #             velha[l][c] = "O"
    #             jogadas += 1
    #             quemJoga = 2

    #  para decidir o vencedor
    def vencedor():
        pass

    #  para termnar o jogo atual
    def terminar():
        pass

    #  Dividindo Frame de Baixo ----------------------------------------------------------------------------------------------------------------
    
    frame_baixo = Frame(janela, width=245, height=235, bg=cor2, relief="flat")
    frame_baixo.grid(row=1, column=0, sticky=NW, padx=13, pady=5)
    
    #  Linhas divisórias Vertical
    lbl_LinhaVertical1 = Label(frame_baixo, text='', height=30, pady=5, relief='flat', anchor='center', font=('Ivy 5 bold'), bg=cor0)
    lbl_LinhaVertical1.place(x=80, y=5)
    lbl_LinhaVertical2 = Label(frame_baixo, text='', height=30, pady=5, relief='flat', anchor='center', font=('Ivy 5 bold'), bg=cor0)
    lbl_LinhaVertical2.place(x=159, y=5)

    #  Linhas divisórias Horisontal
    lbl_LinhaHorisontal1 = Label(frame_baixo, text='', width=225, padx=1, pady=1, relief='flat', anchor='center', font=('Ivy 1 bold'), bg=cor0)
    lbl_LinhaHorisontal1.place(x=6, y=75)
    lbl_LinhaHorisontal2 = Label(frame_baixo, text='', width=225, padx=1, pady=1, relief='flat', anchor='center', font=('Ivy 1 bold'), bg=cor0)
    lbl_LinhaHorisontal2.place(x=6, y=148)

    #  Linhas divisórias Horisontal linha 0
    btn_linha0_bt0 = Button(frame_baixo, command=lambda:controles('00'), text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
    btn_linha0_bt0.place(x=7, y=5)
    btn_linha0_bt1 = Button(frame_baixo, command=lambda:controles('01'), text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
    btn_linha0_bt1.place(x=85, y=5)
    btn_linha0_bt2 = Button(frame_baixo, command=lambda:controles('02'), text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
    btn_linha0_bt2.place(x=164, y=5)
    #  Linhas divisórias Horisontal linha 1
    btn_linha1_bt0 = Button(frame_baixo, command=lambda:controles('10'), text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
    btn_linha1_bt0.place(x=7, y=80)
    btn_linha1_bt1 = Button(frame_baixo, command=lambda:controles('11'), text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
    btn_linha1_bt1.place(x=85, y=80)
    btn_linha1_bt2 = Button(frame_baixo, command=lambda:controles('12'), text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
    btn_linha1_bt2.place(x=164, y=80)
    #  Linhas divisórias Horisontal linha 2
    btn_linha2_bt0 = Button(frame_baixo, command=lambda:controles('20'), text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
    btn_linha2_bt0.place(x=7, y=155)
    btn_linha2_bt1 = Button(frame_baixo, command=lambda:controles('21'), text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
    btn_linha2_bt1.place(x=85, y=155)
    btn_linha2_bt2 = Button(frame_baixo, command=lambda:controles('22'),  text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
    btn_linha2_bt2.place(x=164, y=155)

#  Botão Jogar --------------------------------------------------------------------------------------------------------------------------------
btn_jogar = Button(janela, command=iniciar_jogo, text=novo_jogo, width=10, height=0, font=('Ivy 15 bold'), relief='raised', overrelief=RIDGE, bg=cor2, fg=cor8)
btn_jogar.place(x=75, y=430)





janela.mainloop()