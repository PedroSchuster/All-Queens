import tkinter as tk
from tkinter import ttk
from Tabuleiro import Tabuleiro
from Jogador import Jogador


class Janela(tk.Tk):
    def __init__(self, tabuleiro, jogador_local, click_1, click_posicao):
        super().__init__()
        
        self.click_posicao = click_posicao
        
        self.jogador_local = jogador_local

        self.posicao_vazio = tk.PhotoImage(file="empty.png")

        self.frame_botoes = ttk.Frame(self, height=20, width=400, padding=2)
        self.frame_tabuleiro = ttk.Frame(self, height=400, width=400, padding=2)

        self.title("All Queens")
        self.geometry('800x800')
        self.texto_superior = ttk.Label(
            self, text='Clique em conectar para iniciar o jogo')
        self.texto_superior.pack()

        # Botões:
        self.botao_conectar = ttk.Button(self.frame_botoes, text='Conectar', state='normal', command=click_1)
        self.botao_desconectar = ttk.Button(self.frame_botoes, text='Desconectar', state='disable', command=click_1)
        
        self.botao_conectar.pack()
        self.botao_desconectar.pack()

        self.frame_botoes.pack()

        self.posicoes = []

        for y in range(tabuleiro.tamanho):
            coluna = []
            for x in range(tabuleiro.tamanho):
                pos = ttk.Label(self.frame_tabuleiro, image=self.posicao_vazio)
                pos.grid(row=x, column=y)
                coluna.append(pos)
            self.posicoes.append(coluna)

        self.frame_tabuleiro.pack()
        self.atualiza_tabuleiro(tabuleiro)


    def click_conexao(self):
        #Conectar ao servidor
        if not self.jogador_local.conectado:
          self.texto_superior['text'] = 'Conectado'
          self.botao_conectar['state'] = 'disabled'
          self.botao_desconectar['state'] = 'normal'
          self.jogador_local.conectado = True
          return True
       
        #Desconectar do servidor
        self.texto_superior['text'] = 'Clique em conectar para iniciar o jogo'
        self.botao_conectar['state'] = 'normal'
        self.botao_desconectar['state'] = 'disable'
        self.jogador_local.conectado = False 
        return False

    def atualiza_tabuleiro(self, tabuleiro : Tabuleiro):
        for y in range(tabuleiro.tamanho):
            coluna = []
            for x in range(tabuleiro.tamanho):
                pos = None
                if tabuleiro.tabuleiro[x][y].peca.cor == 'preto':
                    pos = ttk.Label(self.frame_tabuleiro, image=None, text="♛", font=("Arial", 24),background="gray")
                elif tabuleiro.tabuleiro[x][y].peca.cor == 'vermelho':
                    pos = ttk.Label(self.frame_tabuleiro, image=None, text="♛", font=("Arial", 24),background="red")
                else:
                    pos = ttk.Label(self.frame_tabuleiro, image=self.posicao_vazio)
                pos.grid(row=x, column=y)
                pos.bind("<Button-1>", lambda e, x=x, y=y: self.click_posicao({"x": x, "y": y}))
                coluna.append(pos)
            self.posicoes.append(coluna)
            

    
        
        