from dataclasses import dataclass

@dataclass(frozen=True)
class Punkt:
    x: int
    y: int

p = Punkt(1, 2)
# p.x = 3  # detta skulle ge ett fel om du försöker det
