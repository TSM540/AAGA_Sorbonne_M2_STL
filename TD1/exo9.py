# ça ne marche pas, et pas envie de le faire marcher
# PR si vous avez la patience :) 

a = 25214903917
c = 11
m = 2**48

def to_signed_32bit(value):
    x = (value >> 16) & 0xFFFFFFFF
    if x >= 2**31:
        x -= 2**32
    return x

def java_rand48_single(seed):
    return (a * seed + c) % m

# Fonction pour retrouver V1
def find_seed(v1, v2):
    for Xn_16 in range(2**16):
        candidate_seed = (v1 << 16) | Xn_16
        next_value = java_rand48_single(candidate_seed)
        if to_signed_32bit(next_value) == v2:
            return candidate_seed
    return None

# Test
v1 = 1486738135  # Exemple de valeur pour v1
v2 = -423736364  # Exemple de valeur pour v2

seed_found = find_seed(v1, v2)
if seed_found is not None:
    print(f"V1 trouvé : {seed_found}")
else:
    print("Aucun seed correspondant trouvé.")
