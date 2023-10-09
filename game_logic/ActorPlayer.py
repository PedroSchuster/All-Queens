from tkinter import *
import os
from tkinter import messagebox
from custom.PyNetGamesServerProxyCustom import PyNetgamesServerProxyCustom
from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener
from game_logic.Janela import Janela

class ActorPlayer(PyNetgamesServerListener):
	#	A definição da superclasse demanda a necessidade de sobrescrever métodos abstratos herdados 
	#	(no primeiro momento, com "pass"; depois, com a implemetação dos correspondentes casos de uso)
        def __init__(self, tabuleiro):
            self.server_url = "wss://py-netgames-server.fly.dev"
            self.match_id = ''
            self.tabuleiro = tabuleiro
            
            self.janela = Janela(self.tabuleiro, self.click_conexao, self.click_desconexao, self.click_posicao)
        #----------------------- Pynetgames ----------------------------------

        def click_conexao(self):
            self.add_listener()
            self.send_connection()
            
        def click_desconexao(self):
            self.send_disconnect()
        
        def click_posicao(self, pos):
            if self.janela.jogador_local.conectado: # mudar isso para partida em andamento
                self.send_move(pos)

        def set_match_id(self, match_id):
            self.match_id = match_id

        def add_listener(self):     # Pyng use case "add listener"
            self.server_proxy = PyNetgamesServerProxyCustom()
            self.server_proxy.add_listener(self)

        def remove_listener(self):  # Pyng custom use case "remove listener"
            self.server_proxy.remove_listener(self)
        
        def send_connection(self):  # Pyng use case "send connect"
            self.server_proxy.send_connect(self.server_url)
            #self.server_proxy.send_connect()

        def send_match(self, amount_of_players):    # Pyng use case "send match"
            self.server_proxy.send_match(amount_of_players)

        def receive_connection_success(self):    # Pyng use case "receive connection"
            self.janela.mostrar_mensagem('Conectado ao servidor')  
            self.janela.estado_conectado() 
            self.send_match(2) 
            
        def receive_disconnect(self):    # Pyng use case "receive disconnect"
            self.janela.mostrar_mensagem('Desconectado do servidor')
            self.remove_listener()
            self.janela.estado_desconectado()
            
        def send_disconnect(self):
            self.server_proxy.send_disconnect()
        
        def receive_error(self, error):    # Pyng use case "receive error"
            self.janela.mostrar_mensagem('Notificação de erro do servidor. Feche o programa. ')


        def receive_match(self, match):	# Pyng use case "receive match"
            self.janela.mostrar_mensagem('Partida iniciada') 
            self.set_match_id(match.match_id)
            return

        def send_move(self, move):	# Pyng use case "send move"
            self.server_proxy.send_move(self.match_id, move)
        
        def receive_move(self, move):	# Pyng use case "receive move"
            self.janela.mostrar_mensagem(str(move))
  

        

		
		

	