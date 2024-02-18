import tkinter
from tkinter import *
from tkinter import ttk

# Cores -----------------------------------------------------

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
frame_cima = Frame(janela, width=245, height=140, bg=cor1, relief="raised")
frame_cima.grid(row=0, column=0, sticky=NW, padx=13, pady=10)
frame_baixo = Frame(janela, width=245, height=235, bg=cor2, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NW, padx=13, pady=5)

# Dividindo Frame de cima  : ------------------------------------------------------------------------------------------------------------------
lbl_dois_pontos = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor5)
lbl_dois_pontos.place(x=110, y=30)
lbl_placar = Label(frame_cima, text='Placar', height=1, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=cor1, fg=cor2)
lbl_placar.place(x=95, y=2)
# Dividindo Frame de cima - X 
lbl_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=cor1, fg=cor7)
lbl_x.place(x=20, y=25)
lbl_x_jogador1 = Label(frame_cima, text='Jogador 01', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=cor1, fg=cor0)
lbl_x_jogador1.place(x=15, y=85)
lbl_x_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0)
lbl_x_pontos.place(x=75, y=35)
# Dividindo Frame de cima -  O 
lbl_o = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=cor1, fg=cor4)
lbl_o.place(x=175, y=25)
lbl_o_jogador2 = Label(frame_cima, text='Jogador 02', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=cor1, fg=cor0)
lbl_o_jogador2.place(x=170, y=85)
lbl_o_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=cor1, fg=cor0)
lbl_o_pontos.place(x=135, y=35)

# Dividindo Frame de cima - contador de empates
lbl_empate = Label(frame_cima, text='Empates: ', height=1, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor1, fg=cor0)
lbl_empate.place(x=15, y=105)
lbl_empate_quant = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=cor1, fg=cor0)
lbl_empate_quant.place(x=130, y=105)

#  Dividindo Frame de Baixo ----------------------------------------------------------------------------------------------------------------
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
btn_linha0_bt0 = Button(frame_baixo, text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
btn_linha0_bt0.place(x=7, y=5)
btn_linha0_bt1 = Button(frame_baixo, text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
btn_linha0_bt1.place(x=85, y=5)
btn_linha0_bt2 = Button(frame_baixo, text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
btn_linha0_bt2.place(x=164, y=5)
#  Linhas divisórias Horisontal linha 1
btn_linha1_bt0 = Button(frame_baixo, text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
btn_linha1_bt0.place(x=7, y=80)
btn_linha1_bt1 = Button(frame_baixo, text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
btn_linha1_bt1.place(x=85, y=80)
btn_linha1_bt2 = Button(frame_baixo, text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
btn_linha1_bt2.place(x=164, y=80)
#  Linhas divisórias Horisontal linha 2
btn_linha2_bt0 = Button(frame_baixo, text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
btn_linha2_bt0.place(x=7, y=155)
btn_linha2_bt1 = Button(frame_baixo, text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
btn_linha2_bt1.place(x=85, y=155)
btn_linha2_bt2 = Button(frame_baixo, text='', width=3, height=0, font=('Ivy 26 bold'), relief='flat', overrelief=RIDGE, bg=cor2, fg=cor8)
btn_linha2_bt2.place(x=164, y=155)

#  Botão Jogar --------------------------------------------------------------------------------------------------------------------------------
btn_jogar = Button(janela, text='Jogar', width=10, height=0, font=('Ivy 15 bold'), relief='raised', overrelief=RIDGE, bg=cor2, fg=cor8)
btn_jogar.place(x=70, y=420)





janela.mainloop()