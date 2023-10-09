import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import messagebox
from game_logic.Tabuleiro import Tabuleiro


class Janela(tk.Tk):
    def __init__(self, tabuleiro, click_conexao, click_desconexao, click_posicao):
        super().__init__()
        
        self.click_posicao = click_posicao

        self.posicao_vazio = tk.PhotoImage(file="empty.png")

        self.frame_botoes = ttk.Frame(self, height=20, width=400, padding=2)
        self.frame_tabuleiro = ttk.Frame(self, height=400, width=400, padding=2)

        self.title("All Queens")
        self.geometry('800x800')
        self.texto_superior = ttk.Label(
            self, text='Clique em conectar para iniciar o jogo')
        self.texto_superior.pack()

        # Botões:
        self.botao_conectar = ttk.Button(self.frame_botoes, text='Conectar', state='normal', command=click_conexao)
        self.botao_desconectar = ttk.Button(self.frame_botoes, text='Desconectar', state='disable', command=click_desconexao)
        
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


    def estado_conectado(self):
        self.texto_superior['text'] = 'Conectado'
        self.botao_conectar['state'] = 'disabled'
        self.botao_desconectar['state'] = 'normal'
       
    def estado_desconectado(self):
        self.texto_superior['text'] = 'Clique em conectar para iniciar o jogo'
        self.botao_conectar['state'] = 'normal'
        self.botao_desconectar['state'] = 'disable'

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
            
    def mostrar_mensagem(self, mensagem):
        messagebox.showinfo(message=mensagem)
    
        