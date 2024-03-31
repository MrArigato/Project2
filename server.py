from confundo_socket import ConfundoSocket
import socket

class ConfundoServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))

    def listen(self):
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            # Wait for a connection
            data, addr = self.sock.recvfrom(1024)  # Adjust based on expected max packet size
            print(f"Connection from {addr}")

            # Create a new ConfundoSocket for handling the connection
            confundo_socket = ConfundoSocket()
            confundo_socket.sock = self.sock  # Use the existing socket
            confundo_socket.remote_address = addr  # Set the client's address
            
            # Process the initial packet received
            confundo_socket.process_initial_packet(data)

            # Receive data
            received_data = confundo_socket.receive()
            print(f"Received data: {received_data}")

            # Here you can process the received data and optionally send a response
            # For simplicity, this example will just echo the received data back to the client
            confundo_socket.send(received_data)

            # Close the ConfundoSocket for this connection
            confundo_socket.close()

    def process_initial_packet(self, data):
        # Here, you would parse the initial packet to handle SYN, set up connection parameters, etc.
        # This method needs to be implemented in ConfundoSocket to properly initialize the connection
        pass

if __name__ == "__main__":
    HOST = 'localhost'  # Or specify your server's IP address
    PORT = 5000  # Your chosen port for the server

    server = ConfundoServer(HOST, PORT)
    server.listen()
