#!/usr/bin/env python3

import argparse
import socket
import sys
from time import sleep

class ConfundoSocket:
    def __init__(self, dst_host, dst_port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.dst_host = dst_host
        self.dst_port = dst_port
        self.connection_id = None
        self.sequence_number = 50000  # Example initial sequence number
        self.ack_number = 0
        self.cwnd = 412  # Initial congestion window size
        self.mss = 412  # Maximum segment size, adjust as per your project requirements

    def send_syn(self):
        # Construct SYN packet here based on project requirements
        syn_packet = ...
        self.sock.sendto(syn_packet, (self.dst_host, self.dst_port))
    
    def receive_syn_ack(self):
        # Wait for SYN-ACK; adjust timeout as necessary
        self.sock.settimeout(10)
        try:
            data, addr = self.sock.recvfrom(1024)  # Adjust buffer size as needed
            # Extract connection ID, sequence number, etc., from received packet
            # For example:
            self.connection_id = ...
            self.sequence_number = ...
        except socket.timeout:
            print("Connection timeout.", file=sys.stderr)
            sys.exit(1)
    
    def send_ack(self):
        # Construct ACK packet here
        ack_packet = ...
        self.sock.sendto(ack_packet, (self.dst_host, self.dst_port))

    def send_data(self, data):
        # Implement sliding window protocol here based on CWND
        # For simplicity, this example sends data in one go
        self.sock.sendto(data, (self.dst_host, self.dst_port))
        self.sequence_number += len(data)

    def close(self):
        # Send FIN and handle closure
        fin_packet = ...
        self.sock.sendto(fin_packet, (self.dst_host, self.dst_port))
        # Optionally wait for ACK of FIN and send last ACK

def main(host, port, file_path):
    confundo_socket = ConfundoSocket(host, port)
    confundo_socket.send_syn()
    confundo_socket.receive_syn_ack()
    confundo_socket.send_ack()
    
    try:
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(confundo_socket.mss)
                if not chunk:
                    break
                confundo_socket.send_data(chunk)
                # Implement ACK reception and congestion control adjustments here
    except Exception as e:
        print(f"Failed to send file: {e}", file=sys.stderr)
    
    confundo_socket.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Confundo Protocol Client')
    parser.add_argument('host', help='Hostname or IP address of the server')
    parser.add_argument('port', type=int, help='Port number of the server')
    parser.add_argument('file', help='Path to the file to be transferred')
    args = parser.parse_args()
    
    main(args.host, args.port, args.file)


    
    main(server_ip, server_port, filename)
