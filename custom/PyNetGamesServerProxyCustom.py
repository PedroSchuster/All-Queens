from typing import List, Callable
from py_netgames_client.tkinter_client.PyNetgamesServerProxy import PyNetgamesServerProxy

from py_netgames_model.messaging.message import MatchStartedMessage, MoveMessage

from py_netgames_client.tkinter_client.PyNetgamesServerListener import PyNetgamesServerListener


class PyNetgamesServerProxyCustom(PyNetgamesServerProxy):
    _listeners: List[PyNetgamesServerListener]
    
    #implement the constructor
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._listeners = []
        
    #implement the methods
    def add_listener(self, listener: PyNetgamesServerListener):
        self._listeners.append(listener)
        
    def remove_listener(self, listener: PyNetgamesServerListener):
        self._listeners.remove(listener)
        
    def _receive_match_start(self, match: MatchStartedMessage):
        [self._log_error(lambda: listener.receive_match(match)) for listener in self._listeners]
        
    def _receive_move(self, move: MoveMessage):
        [self._log_error(lambda: listener.receive_move(move)) for listener in self._listeners]
        
    def _disconnection(self):
        [self._log_error(lambda: listener.receive_disconnect()) for listener in self._listeners]

    def _connection_success(self):
        [self._log_error(lambda: listener.receive_connection_success()) for listener in self._listeners]

    def _error(self, error: Exception):
        [self._log_error(lambda: listener.receive_error(error)) for listener in self._listeners]

    def _match_requested_success(self):
        [self._log_error(lambda: listener.receive_match_requested_success()) for listener in self._listeners]

    def _move_sent_success(self):
        [self._log_error(lambda: listener.receive_move_sent_success()) for listener in self._listeners]

    def _log_error(self, method: Callable):
        try:
            method()
        except Exception as e:
            try:
                raise e from None
            except Exception as e:
                self._logger.exception(e)
