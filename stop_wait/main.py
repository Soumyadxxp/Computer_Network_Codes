import time
from sender import send_frame, send_ack
from receiver import receive_frame

TIMEOUT = 1.0


def main():
    """Main transmission control and verification."""
    messages = []
    for i in range(5):
        message = input(f"Enter message {i}: ")
        messages.append(message)

    sent_data = []
    received_data = []
    next_seq = 0
    expected_seq = 0
    waiting = None
    timeout_deadline = None
    index = 0

    print("\n" + "="*60)
    print("Starting Stop-and-Wait transmission...\n")

    while index < len(messages) or waiting is not None:
        if waiting is None and index < len(messages):
            waiting = (next_seq, messages[index])
            timeout_deadline = time.time() + TIMEOUT
            frame = send_frame(*waiting)
        else:
            frame = waiting

        if frame is not None:
            ack_seq, payload, expected_seq = receive_frame(frame, expected_seq)
            if payload is not None:
                received_data.append(payload)
            ack = send_ack(ack_seq)
            if ack == next_seq:
                print(f"Sender: received ACK({ack})")
                sent_data.append(messages[index])
                next_seq ^= 1
                waiting = None
                index += 1
                continue

        if waiting is not None and time.time() >= timeout_deadline:
            print(f"Sender: timeout for seq={waiting[0]}, retransmitting")
            frame = send_frame(*waiting)
            timeout_deadline = time.time() + TIMEOUT

        time.sleep(0.05)

    print("\n" + "="*60)
    print("TRANSMISSION VERIFICATION REPORT")
    print("="*60)
    print(f"Messages sent:     {len(sent_data)}")
    print(f"Messages received: {len(received_data)}")
    
    if sent_data == received_data:
        print("\n✓ SUCCESS: All data transmitted correctly!")
        print(f"Transmitted: {sent_data}")
    else:
        print("\n✗ FAILURE: Data mismatch detected!")
        print(f"Sent:     {sent_data}")
        print(f"Received: {received_data}")
        for i, (s, r) in enumerate(zip(sent_data, received_data)):
            if s != r:
                print(f"  Message {i}: '{s}' != '{r}'")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
