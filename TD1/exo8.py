a = 25214903917
c = 11
m = 2**48

def rand48(seed, num_values=10):
    values = []
    Xn = seed
    for _ in range(num_values):
        Xn = (a * Xn + c) % m
        values.append(Xn)
    return values
def to_signed_32bit(value):
    # On enlève les 16 bits de poids faible
    x = (value >> 16) & 0xFFFFFFFF
    # Conversion en integer signé de la remarque
    if x >= 2**31:
        x -= 2**32
    return x
def java_rand48(seed, num_values=6):
    values_32bit = []
    Xn = seed
    for _ in range(num_values):
        Xn = (a * Xn + c) % m
        signed_32bit = to_signed_32bit(Xn)
        values_32bit.append(signed_32bit)
    return values_32bit
# ! Question 8.1
seed = 0
rand48_values = rand48(seed, 10)
print("RAND48 values from seed 0:", rand48_values)
# ! Question 8.2
seed_java = 156079716630527
java_values = java_rand48(seed_java, 10)
print("Java-style RAND48 values:", java_values)