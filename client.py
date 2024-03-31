import socket
import sys

def create_syn_header(sequence_number=0, ack_number=0, flags=0b010):
    """
    Constructs a SYN packet header with the specified parameters.
    Flags are set to indicate SYN packet; for simplicity, we're just using a byte here.
    """
    # Header structure: [Sequence Number (4 bytes), Ack Number (4 bytes), Flags (1 byte)]
    # Note: Adjust this method to match your project's header format and encoding
    return struct.pack('!IIB', sequence_number, ack_number, flags)

def send_syn_packet(server_ip, server_port):
    """
    Sends a SYN packet to initiate the three-way handshake.
    """
    try:
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Construct the SYN packet
        syn_header = create_syn_header(sequence_number=1000)  # Example sequence number
        sock.sendto(syn_header, (server_ip, server_port))

        # Wait for SYN-ACK response (simplified, without timeout handling)
        response, addr = sock.recvfrom(1024)
        print("Received response from the server.")

        # Here, you would parse the response and check if it's a SYN-ACK,
        # then proceed to send an ACK. This part is simplified.
        # ...

        print("SYN packet sent and SYN-ACK received.")
    except Exception as e:
        print(f"Failed to send SYN packet: {e}")
        sys.exit(1)
    finally:
        sock.close()

if __name__ == "__main__":
    # Example usage
    SERVER_IP = '127.0.0.1'  # Replace with actual server IP
    SERVER_PORT = 5000       # Replace with actual server port
    send_syn_packet(SERVER_IP, SERVER_PORT)

    
    main(server_ip, server_port, filename)
