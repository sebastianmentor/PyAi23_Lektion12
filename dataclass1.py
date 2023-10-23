from dataclasses import dataclass

@dataclass
class Punkt:
    x: int
    y: int

p = Punkt(1, 2)
print(p)  # Punkt(x=1, y=2)

p.x = 3
print(p)


@dataclass
class Rektangel:
    bredd: float
    höjd: float
    färg: str = "vit"

r = Rektangel(10, 20)
print(r)  # Rektangel(bredd=10, höjd=20, färg='vit')


