import random
import time

window_size = 4
total_frames = 10
sent_frames = 0
ack_received = 0

# Frames sending
while ack_received < total_frames:
    # Sending frames within the window
    for i in range(window_size):
        if sent_frames < total_frames:
            print(f"Sending Frame {sent_frames}")
            sent_frames += 1
            time.sleep(1)
    
    # Acknowledgment process
    for i in range(window_size):
        if ack_received < total_frames:
            ack = random.choice([True, False])
            if ack:  # If acknowledgment is received
                print(f"ACK received for Frame {ack_received}")
                ack_received += 1
            else:  # If acknowledgment is lost
                print(f"Frame {ack_received} lost, resending from this frame")
                sent_frames = ack_received  # Reset the sent_frames pointer
                break





