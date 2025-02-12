import socket
import ssl
import threading

class IRCClient:
    def __init__(self, host, port, nickname, use_ssl=False):
        self.host = host
        self.port = port
        self.nickname = nickname
        self.use_ssl = use_ssl
        self.running = True
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if self.use_ssl:
            # Crear una instancia de SSLContext para autenticación del servidor (conexión cliente)
            ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            ssl_context.check_hostname = True  # Verifica que el nombre de host en el certificado coincide con el objetivo
            ssl_context.verify_mode = ssl.CERT_REQUIRED  # Requiere un certificado válido
            # ssl_context.check_hostname = False
            # ssl_context.verify_mode = ssl.CERT_NONE  #Deshabilita la verificación del certificado
            # Envolver el socket existente en un contexto SSL
            self.socket = ssl_context.wrap_socket(self.socket, server_hostname=self.host)
        
        self.send_raw(f'NICK {self.nickname}')
        self.send_raw(f'USER {self.nickname} 0 * :Python IRC Client')
        
    
    def send_raw(self, data):
        self.sock.send((data + '\r\n').encode('utf-8'))
    
    def change_nick(self, new_nick):
        self.send_raw(f'NICK {new_nick}')
        self.nickname = new_nick
    
    def join_channel(self, channel):
        self.send_raw(f'JOIN {channel}')
    
    def part_channel(self, channel):
        self.send_raw(f'PART {channel}')
    
    def send_message(self, target, message):
        self.send_raw(f'PRIVMSG {target} :{message}')
    
    def send_notice(self, target, message):
        self.send_raw(f'NOTICE {target} :{message}')
    
    def list(self):
        self.send_raw(f'LIST')
    
    def quit(self, message="Goodbye!"):
        self.send_raw(f'QUIT :{message}')
        self.running = False
        self.sock.close()
    
    def handle_server_response(self):
        while self.running:
            try:
                data = self.sock.recv(4096).decode('utf-8', errors='ignore')
                if not data:
                    break
                for line in data.split('\r\n'):
                    if line:
                        print(line)
                        self.process_message(line)
            except Exception as e:
                print(f'Error en la recepción: {e}')
                break
    
    def process_message(self, message):
        parts = message.split()
        if len(parts) < 2:
            return
        if parts[0] == 'PING':
            self.send_raw(f'PONG {parts[1]}')
    
    def start(self):
        thread = threading.Thread(target=self.handle_server_response)
        thread.start()

if __name__ == "__main__":
    import sys
    
    test_input = sys.argv[1:]
    host,port,nickname,command,arg = test_input[1],int(test_input[3]),test_input[5],'/'+test_input[7].split('/').pop(),test_input[9]
    
    client = IRCClient(host, port, nickname)
    client.start()
    
    if command == "/nick":
        client.change_nick(arg)
    elif command == "/join":
        client.join_channel(arg)
    elif command == "/part":
        client.part_channel(arg)
    elif command == "/privmsg":
        target, message = arg.split(" ", 1)
        client.send_message(target, message)
    elif command == "/notice":
        target, message = arg.split(" ", 1)
        client.send_notice(target, message)
    elif command == "/list":
        client.list()
    elif command == "/quit":
        client.quit(arg)
        
    client.quit()

    # while True:
    #     cmd = input().strip().split(" ", 1)
    #     if not cmd:
    #         continue
    #     command = cmd[0]
    #     argument = cmd[1] if len(cmd) > 1 else ""
        
    #     if command == "/nick":
    #         client.change_nick(argument)
    #     elif command == "/join":
    #         client.join_channel(argument)
    #     elif command == "/part":
    #         client.part_channel(argument)
    #     elif command == "/privmsg":
    #         target, message = argument.split(" ", 1)
    #         client.send_message(target, message)
    #     elif command == "/notice":
    #         target, message = argument.split(" ", 1)
    #         client.send_notice(target, message)
    #     elif command == "/quit":
    #         client.quit(argument)
    #         break