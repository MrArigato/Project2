class CongestionControl:
    def __init__(self):
        # Initialize congestion window to 1 MSS (Maximum Segment Size)
        self.cwnd = 1
        self.ssthresh = 64  # Start with a high slow start threshold
        self.mss = 512  # Assuming an MSS of 512 bytes for this example

    def ack_received(self):
        """Adjusts the congestion window size upon receiving an ACK."""
        if self.cwnd < self.ssthresh:
            # In slow start, congestion window grows exponentially.
            self.cwnd *= 2
        else:
            # In congestion avoidance, congestion window grows linearly.
            self.cwnd += 1

    def timeout_occurred(self):
        """Adjusts the congestion window size and ssthresh upon a timeout."""
        # Upon timeout, ssthresh is set to half of the current congestion window (minimum 1 MSS)
        self.ssthresh = max(self.cwnd / 2, 1)
        self.cwnd = 1  # Reset congestion window to 1 MSS

    def get_cwnd(self):
        """Returns the current size of the congestion window."""
        return self.cwnd

    def get_ssthresh(self):
        """Returns the current slow start threshold."""
        return self.ssthresh
