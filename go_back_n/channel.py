import random
from typing import Optional
from models import Frame, Ack, PACKET_LOSS_PROBABILITY, CORRUPTION_PROBABILITY, ACK_LOSS_PROBABILITY


class Channel:
    def send_frame(self, frame: Frame) -> Optional[Frame]:
        if random.random() < PACKET_LOSS_PROBABILITY:
            print(f"Channel: frame {frame.seq} lost")
            return None

        if random.random() < CORRUPTION_PROBABILITY:
            print(f"Channel: frame {frame.seq} corrupted")
            return Frame(frame.seq, "<CORRUPTED>")

        print(f"Channel: frame {frame.seq} delivered")
        return frame

    def send_ack(self, ack: Ack) -> Optional[Ack]:
        if random.random() < ACK_LOSS_PROBABILITY:
            print(f"Channel: ACK {ack.seq} lost")
            return None

        print(f"Channel: ACK {ack.seq} delivered")
        return ack
