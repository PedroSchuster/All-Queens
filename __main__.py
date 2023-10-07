from ActorPlayer import ActorPlayer
from Tabuleiro import Tabuleiro


if __name__ == "__main__":
    tabuleiro = Tabuleiro()
    player = ActorPlayer(tabuleiro)
    player.janela.mainloop()
