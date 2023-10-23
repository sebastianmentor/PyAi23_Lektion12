from enum import Enum

class Färg(Enum):
    RÖD = 1
    GRÖN = 2
    BLÅ = 3
    GUL = 4

print(Färg.RÖD)    # Färg.RÖD
print(Färg.RÖD.name) # RÖD
print(Färg.RÖD.value) # 1


for färg in Färg:
    print(färg.name, färg.value)


min_färg = Färg.RÖD

if min_färg == Färg.RÖD:
    print("Det är rött!")


