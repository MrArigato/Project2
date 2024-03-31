import socket
import struct
import select
import time

# Define control flags
SYN = 0x02
ACK = 0x10
FIN = 0x01

class ConfundoSocket:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(0.5)  # Set a timeout for socket operations
        self.sequence_number = 0
        self.acknowledgment_number = 0
        self.connection_id = 0
        self.remote_address = None
        self.header_format = '!I I H B'  # Sequence Num, Ack Num, Connection ID, Flags
    
    def connect(self, address):
        self.remote_address = address
        self._send_header(SYN)  # Send SYN
        self._receive_header()  # Expecting SYN-ACK
        self._send_header(ACK)  # Send ACK to complete handshake

    def send(self, data):
        """Send data using stop-and-wait ARQ."""
        for i in range(0, len(data), 412):
            segment = data[i:i+412]
            while True:
                self._send_header(ACK, segment)  # Send data with ACK flag
                try:
                    self._receive_header()  # Waiting for ACK
                    break  # Move to next segment upon receiving ACK
                except socket.timeout:
                    continue  # Resend on timeout

    def receive(self):
        """Receive data. This is a blocking call."""
        data = b''
        while True:
            header, segment = self._receive_header()
            if header['flags'] & FIN:  # Check if the FIN flag is set
                self._send_header(ACK)  # Send ACK for FIN
                break
            data += segment
            self._send_header(ACK)  # Acknowledge received data
        return data

    def close(self):
        """Terminate the connection."""
        self._send_header(FIN)  # Send FIN
        self._receive_header()  # Expecting ACK for FIN

    def _send_header(self, flags, data=b''):
        """Send a packet with the specified header flags and data."""
        header = struct.pack(self.header_format, self.sequence_number, self.acknowledgment_number, self.connection_id, flags)
        self.sock.sendto(header + data, self.remote_address)

    def _receive_header(self):
        """Receive a packet and unpack its header."""
        packet, _ = self.sock.recvfrom(1024)
        header = struct.unpack(self.header_format, packet[:8])
        return {'sequence_number': header[0], 'acknowledgment_number': header[1], 'connection_id': header[2], 'flags': header[3]}, packet[8:]

# Example usage
if __name__ == '__main__':
    client = ConfundoSocket()
    client.connect(('localhost', 5000))
    client.send(b'Hello, Confundo!')
    print(client.receive())
    client.close()
