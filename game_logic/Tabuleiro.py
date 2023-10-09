from game_logic.Posicao import Posicao
from game_logic.Peca import Peca
from game_logic.Jogador import Jogador

class Tabuleiro:
    def __init__(self):
        self.tamanho = 5
        self.jogador = Jogador('branco')
        self.tabuleiro = []
        
        self.inicializar_tabuleiro()

    def inicializar_tabuleiro(self):
        
        for i in range(self.tamanho):
            linha = []
            for j in range(self.tamanho):
                linha.append(Posicao(Peca("branco")))
            self.tabuleiro.append(linha)
        
        posicoes_rainhas = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (2, 0), (2, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        i = 0
        for p in posicoes_rainhas:
            if i % 2 == 0:
                self.tabuleiro[p[0]][p[1]] = Posicao(Peca("vermelho"))
            else:
                self.tabuleiro[p[0]][p[1]] = Posicao(Peca("preto"))
            i += 1