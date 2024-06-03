import socket

HOST = 'localhost'
PORT = 12345
BUFSIZ = 256

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input('Enter the host: ') or HOST
    port = input('Enter the port: ') or PORT

    sock_addr = (host, int(port))
    client_socket.connect(sock_addr)

    try:
        while True:
            amount = input('Enter the amount in pesos: ')
            if amount.lower() == 'end':
                client_socket.send(b'END')
                break
            
            client_socket.send(amount.encode('utf-8'))

            data = client_socket.recv(BUFSIZ)
            print(data.decode('utf-8'))
    except KeyboardInterrupt:
        print('Exited by user')
    
    client_socket.close()

