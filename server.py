import threading
import socket

host = '127.0.0.1'
port = 12000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []


# Fuctions to handle connection
def broadcast(message):
    for client in clients:
        client.send(message)


def hdl_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index
            client.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} left the session.'.encode('utf-8'))
            aliases.remove((alias))
            break


# Main function to get the client connection

def recive():
    while True:
        print('Server is working :)')
        client, address = server.accept()
        print(f'Connection addres: {str(address)}')
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f'Alias of this client: {alias}'.encode('utf-8'))
        broadcast(f'{alias} enterd the session'.encode('utf-8'))
        client.send('WELCOME! You are now connected'.encode('utf-8'))
        thread = threading.Thread(target=hdl_client, args=(client,))
        thread.start()

if __name__== "__main__":
    recive()

