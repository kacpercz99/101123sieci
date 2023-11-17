import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 5678)
client_socket.connect(server_address)

try:
    message = ''
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))
        data = client_socket.recv(1024)
        print(f"Odpowiedź serwera: {data.decode('utf-8')}")

except KeyboardInterrupt:
    print("\nZamykanie klienta...")
finally:
    client_socket.close()
