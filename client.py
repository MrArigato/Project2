import sys
from confundo_socket import ConfundoSocket

def main(server_ip, server_port, filename):
    # Initialize your custom socket
    confundo_socket = ConfundoSocket()
    
    try:
        # Connect to the server
        confundo_socket.connect((server_ip, server_port))
        print(f"Connected to {server_ip}:{server_port}")
        
        # Open and read the file
        with open(filename, 'rb') as file:
            data = file.read()
            # Send data
            confundo_socket.send(data)
            print(f"Sent data from {filename}")

        # Optionally, wait for a response if your protocol supports/requires this
        # response = confundo_socket.receive()
        # print(f"Received response: {response}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        confundo_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: client.py <HOSTNAME-OR-IP> <PORT> <FILENAME>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]
    
    main(server_ip, server_port, filename)
