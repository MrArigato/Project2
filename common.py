# Common constants for Confundo Protocol
MAX_PACKET_SIZE = 1024
HEADER_FORMAT = '!I I H B'  # Sequence Number, Acknowledgment Number, Connection ID, Flags
SEQUENCE_NUMBER_INIT = 50000
ACK_NUMBER_INIT = 0
CONNECTION_ID_INIT = 0
MAX_SEQUENCE_NUMBER = 50000

# Control flags for packet header (simplified)
SYN = 0x02  # Synchronize sequence numbers
ACK = 0x10  # Acknowledgment
FIN = 0x01  # No more data from sender

# Maximum payload size calculation
HEADER_SIZE = 12  # Assuming a 12-byte header (4+4+2+2 where the last 2 bytes include flags and padding)
MAX_PAYLOAD_SIZE = MAX_PACKET_SIZE - HEADER_SIZE

def pack_header(sequence_number, acknowledgment_number, connection_id, flags):
    """
    Packs the header information into bytes, suitable for sending over the network.
    """
    import struct  # Import here if you prefer to keep imports clean
    return struct.pack(HEADER_FORMAT, sequence_number, acknowledgment_number, connection_id, flags)

def unpack_header(packet):
    """
    Unpacks the header from the received packet bytes.
    """
    import struct  # Import here if you prefer to keep imports clean
    return struct.unpack(HEADER_FORMAT, packet[:HEADER_SIZE])

def print_packet_info(action, header, data_length=0):
    """
    Utility function to print information about sent or received packets.
    """
    seq_num, ack_num, conn_id, flags = header
    flags_description = get_flags_description(flags)
    print(f"{action}: Seq={seq_num}, Ack={ack_num}, ID={conn_id}, Flags={flags_description}, Data Length={data_length}")

def get_flags_description(flags):
    """
    Returns a string description of the flags set in the header.
    """
    descriptions = []
    if flags & SYN:
        descriptions.append("SYN")
    if flags & ACK:
        descriptions.append("ACK")
    if flags & FIN:
        descriptions.append("FIN")
    return "|".join(descriptions) if descriptions else "None"
