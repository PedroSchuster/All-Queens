from game_logic.ActorPlayer import ActorPlayer
from game_logic.Tabuleiro import Tabuleiro


if __name__ == "__main__":
    tabuleiro = Tabuleiro()
    player = ActorPlayer(tabuleiro)
    player.janela.mainloop()
