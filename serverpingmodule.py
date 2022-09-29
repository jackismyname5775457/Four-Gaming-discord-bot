from ast import Mod
from socket import socket, create_connection, AF_INET, SOCK_DGRAM
from struct import unpack
from time import time
from dataclasses import dataclass
from typing import Tuple

# * Dataclass
@dataclass
class Status:
    name: str
    map: str
    players: int
    wave: int
    version: float
    vertype: str
    ping: float

# * Main class
class Server:
    def __init__(
        self,
        server_host: str,
        server_port: int=6567,
        input_port: int=6859
    ) -> None:
        self.server: Tuple[str, int] = (server_host, server_port)
        self.input_server: Tuple[str, int] = (server_host, input_port)

    def get_status(self, timeout: float=10.0) -> Status:
        # * Server initialization
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(self.server)
        s.settimeout(timeout)

        # * Creation and so it is clear what for what
        info = {}

        # * Data acquisition and measurement
        s_time = time()
        s.send(b"\xfe\x01")
        data = s.recv(1024)
        e_time = time()

        # * Parsing
        info["name"] = data[1:data[0]+1].decode("utf-8")
        data = data[data[0]+1:]
        info["map"] = data[1:data[0]+1].decode("utf-8")
        data = data[data[0]+1:]
        info["players"] = unpack(">i", data[:4])[0]
        data = data[4:]
        info["wave"] = unpack(">i", data[:4])[0]
        data = data[4:]
        info["version"] = unpack(">i", data[:4])[0]
        data = data[4:]
        info["vertype"] = data[1:data[0]+1].decode("utf-8")
        info["ping"] = round((e_time - s_time) * 1000)

        return Status(**info)
    
    def send_command(self, command: str) -> None:
        s = create_connection(self.input_server)
        s.sendall(
            bytes(
                command.encode(errors="ignore")
            )
        )
        s.close()
    
    def ping(self, timeout: float=10.0) -> int:
        # * Server initialization
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(self.server)
        s.settimeout(timeout)

        # * Data acquisition and measurement
        s_time = time()
        s.send(b"\xfe\x01")
        s.recv(1024)
        e_time = time()

        return round((e_time - s_time) * 1000)
