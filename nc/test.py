import socket


def start_server(host, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address}")

        # Start receiving and echoing messages
        while True:
            # Receive data from the client
            data = client_socket.recv(4096).decode()

            if not data:
                # No more data, connection closed by client
                break

            # Echo the received data back to the client
            client_socket.sendall(data.encode())

        # Close the client connection
        client_socket.close()
        print(f"Connection with client {client_address} closed")


# Provide the host and port to listen on
host = '127.0.0.1'  # Example host
port = 1234        # Example port

# Start the server
start_server(host, port)
