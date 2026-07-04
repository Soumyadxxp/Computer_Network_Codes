from dataclasses import dataclass

WINDOW_SIZE = 4
TIMEOUT_SECONDS = 2.0
PACKET_LOSS_PROBABILITY = 0.2
ACK_LOSS_PROBABILITY = 0.1
CORRUPTION_PROBABILITY = 0.05
SIMULATION_STEP_SECONDS = 0.2


@dataclass
class Frame:
    seq: int
    data: str


@dataclass
class Ack:
    seq: int
