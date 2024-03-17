import threading
import socket

alias = input('Choose alias ->')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12000))

def recive():
    while True:
        try:
            message= client.recv(1024).decode('utf-8')
            if message == "alias?":
                client.send(alias.encode("utf-8"))
            else:
                print(message)
        except:
            print('ERROR')
            client.close()
            break

def send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode("utf-8"))


recive_t = threading.Thread(target = recive)
recive_t.start()

send_t = threading.Thread( target = send)
send_t.start()