
import socket
import requests

HOST = 'localhost'
PORT = 12345
BUFSIZ = 1024
ADDR = (HOST, PORT)

def get_dollar_quote():
    response = requests.get('https://www.dolarsi.com/api/api.php?type=dolar')
    if response.status_code == 200:
        quote = response.json()[0]['casa']['venta']
        return quote
    return None

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(ADDR)
    server_socket.listen(5)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    while True:
        print('Server waiting for connection...')
        client_socket, addr = server_socket.accept()
        print('Client connected from:', addr)

        while True:
            data = client_socket.recv(BUFSIZ)
            if not data or data.decode('utf-8') == 'END':
                break

            try:
                amount = float(data.decode('utf-8'))
                quote = get_dollar_quote()
                if quote:
                    dollars = amount / quote
                    client_socket.send(bytes(f'Amount in dollars: {dollars:.2f}', 'utf-8'))
                else:
                    client_socket.send(b'Error getting quote')
            except ValueError:
                client_socket.send(b'Invalid amount')

        client_socket.close()

    server_socket.close()
