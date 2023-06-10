import socket
import time


def interact_with_connection(host, port):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to {host}:{port}")

        # Start the interaction loop
        # while True:
        if True:
            # Send data to the server
            message = input("Enter a message (or 'exit' to quit): ")
            if message.lower() == "exit":
                # break
                return
            client_socket.sendall(message.encode())

            # Delay for 1 seconds
            time.sleep(1)

            # Receive response from the server
            response = client_socket.recv(4096).decode()
            print("Server response:", response)

    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed.")


# Provide the host and port to connect to
host = '127.0.0.1'  # Example host
port = 1234        # Example port

# Start the interaction
interact_with_connection(host, port)
