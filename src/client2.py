import socket


def start_client():
    server_ip = "127.0.0.1"  # Loopback address for localhost
    server_port = 12345

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server {server_ip}:{server_port}")

    while True:
        # Get user input and send it to the server
        message = input("Enter message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))

        # Receive the echoed message from the server
        data = client_socket.recv(1024)
        print(f"Received message from server: {data.decode("utf-8")}")

    # Close the client socket when done
    client_socket.close()


if __name__ == "__main__":
    start_client()
