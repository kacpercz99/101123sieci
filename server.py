import socket
while True:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_address = ('localhost', 5678)
        server_socket.bind(server_address)
        server_socket.listen(1)
        print("Czekam na połączanie...")

        client_socket, client_address = server_socket.accept()
        print(f"Połączono z {client_address}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            decoded_data = data.decode('utf-8')
            print(f"Otrzymane dane: {decoded_data}")
            client_socket.send(data)

    except Exception as e:
        print(f"Wystąpił błąd: {e}")

    finally:
        print("Zamykanie połączenia...")
        server_socket.close()