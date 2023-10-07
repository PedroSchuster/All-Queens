from tkinter import *
import os
from tkinter import messagebox
from PyNetGamesServerProxyCustom import PyNetgamesServerProxyCustom
from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener
from Janela import Janela

class ActorPlayer(PyNetgamesServerListener):
	#	A definição da superclasse demanda a necessidade de sobrescrever métodos abstratos herdados 
	#	(no primeiro momento, com "pass"; depois, com a implemetação dos correspondentes casos de uso)
        def __init__(self, tabuleiro):
            self.server_url = "wss://py-netgames-server.fly.dev"
            self.match_id = ''
            self.tabuleiro = tabuleiro
            
            self.janela = Janela(self.tabuleiro, self.tabuleiro.jogador, self.click_conexao, self.click_posicao)
        #----------------------- Pynetgames ----------------------------------

        def click_conexao(self):
            if self.janela.click_conexao():
                self.add_listener()
                return self.send_connection()
            return self.send_disconnect()
            
        def click_posicao(self, pos):
            if self.janela.jogador_local.conectado: # mudar isso para partida em andamento
                self.send_move(pos)
        
        def set_match_id(self, match_id):
            self.match_id = match_id
    
        def get_match_id(self):
            return self.match_id

        def add_listener(self):     # Pyng use case "add listener"
            self.server_proxy = PyNetgamesServerProxyCustom()
            self.server_proxy.add_listener(self)

        def remove_listener(self):  # Pyng use case "remove listener"
            self.server_proxy.remove_listener(self)
        
        def send_connection(self):  # Pyng use case "send connect"
            self.server_proxy.send_connect(self.server_url)
            #self.server_proxy.send_connect()


        def send_match(self, amount_of_players):    # Pyng use case "send match"
            self.server_proxy.send_match(amount_of_players)


        def receive_connection_success(self):    # Pyng use case "receive connection"
            messagebox.showinfo(message='Conectado ao servidor') 
            self.janela.jogador_local.conectado = True
            self.send_match(2)    # Pyng use case "send match"


        def receive_disconnect(self):    # Pyng use case "receive disconnect"
            messagebox.showinfo(message='Desconectado do servidor')
            self.janela.texto_superior['text'] = 'Clique em conectar para iniciar o jogo'
            self.janela.botao_conectar['state'] = 'normal'
            self.janela.botao_desconectar['state'] = 'disable'
            self.janela.jogador_local.conectado = False 
            self.remove_listener()

        def send_disconnect(self):
            self.server_proxy.send_disconnect()
        
        def receive_error(self, error):    # Pyng use case "receive error"
            messagebox.showinfo(message='Notificação de erro do servidor. Feche o programa.') 

        def receive_match(self, match):	# Pyng use case "receive match"
            messagebox.showinfo(message='Partida iniciada') 
            self.set_match_id(match.match_id)
            return

        def send_move(self, move):	# Pyng use case "send move"
            self.server_proxy.send_move(self.match_id, move)
        
        def receive_move(self, move):	# Pyng use case "receive move"
            messagebox.showinfo(message=str(move))

            

        

		
		

	