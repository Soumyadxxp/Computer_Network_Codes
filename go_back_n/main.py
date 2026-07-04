import time
from typing import List
from models import (
    Frame, Ack, WINDOW_SIZE, TIMEOUT_SECONDS,
    PACKET_LOSS_PROBABILITY, ACK_LOSS_PROBABILITY,
    CORRUPTION_PROBABILITY, SIMULATION_STEP_SECONDS,
)
from channel import Channel
from receiver import Receiver
from sender import Sender


def run_go_back_n(messages: List[str]) -> None:
    sender = Sender(messages, WINDOW_SIZE, TIMEOUT_SECONDS)
    receiver = Receiver()
    channel = Channel()

    pending_frames: List[Frame] = []
    pending_acks: List[Ack] = []
    iteration = 0

    print("\n=== Go-Back-N ARQ Simulation ===\n")
    print(f"Messages to send: {len(messages)}")
    print(f"Window size: {WINDOW_SIZE}")
    print(f"Timeout: {TIMEOUT_SECONDS}s")
    print(
        f"Packet loss: {PACKET_LOSS_PROBABILITY * 100:.0f}%, ACK loss: {ACK_LOSS_PROBABILITY * 100:.0f}%"
    )
    print(f"Corruption: {CORRUPTION_PROBABILITY * 100:.0f}%\n")

    while not sender.all_acked():
        iteration += 1
        print(f"\n--- Iteration {iteration} ---")

        while sender.can_send_next():
            pending_frames.append(sender.next_frame())

        pending_frames.extend(sender.get_retransmissions())

        for frame in pending_frames:
            delivered_frame = channel.send_frame(frame)
            if delivered_frame is not None:
                ack = receiver.receive(delivered_frame)
                if ack is not None:
                    pending_acks.append(ack)
        pending_frames.clear()

        for ack in pending_acks:
            delivered_ack = channel.send_ack(ack)
            if delivered_ack is not None:
                sender.process_ack(delivered_ack)
        pending_acks.clear()

        if sender.all_acked():
            break

        time.sleep(SIMULATION_STEP_SECONDS)

    print("\n=== Transmission Complete ===")
    print(f"Delivered messages: {len(receiver.delivered)}")
    for index, message in enumerate(receiver.delivered):
        print(f"  {index}: {message}")
    print("\nGo-Back-N simulation finished successfully.")


def main() -> None:
    packet_count = input(
        "Enter number of packets to send (or press Enter for default 8): "
    ).strip()
    if packet_count:
        try:
            count = int(packet_count)
        except ValueError:
            count = 8
    else:
        count = 8

    messages = [f"Packet {i}" for i in range(count)]
    run_go_back_n(messages)


if __name__ == "__main__":
    main()
