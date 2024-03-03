import socket
import threading


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        received_message = data.decode('utf-8')
        # Extract client name and message
        client_name, message = received_message.split(":")
        # 5. Print the client_id so the server knows which cleint has been contacting it.
        print(f"Received message from {client_name}:{message}")

        response_message = f"Server received: {received_message} - Thanks for the message!"
        client_socket.send(response_message.encode('utf-8'))

    client_socket.close()


def start_server():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 1.Initialize client counter to be 1

    try:
        server_socket.bind((server_ip, server_port))
        server_socket.listen(5)
        print(f"Server listening on {server_ip}:{server_port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")

            # 2. Create a client_id variable and update it with the counter value
            # 3. Increment the counter value so it is different for the next client that joins

            # 4.  Pass the client_id to the handle_client function
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

    except KeyboardInterrupt:
        print("Server is shutting down...")
    finally:
        # Close the server socket in the finally block
        server_socket.close()


if __name__ == "__main__":
    start_server()
