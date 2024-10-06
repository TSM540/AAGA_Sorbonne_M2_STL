def generateur_lineaire(a, c, m, x0):
    x = x0
    while True:
        x = (a * x + c) % m
        yield x
    
# Tests 
gen = generateur_lineaire(3, 7, 10, 1)
for _ in range(10):
    print(next(gen))
    
#Calcul de la période du générateur linéaire
def period_generator(a, c, m, x0):
    x = x0
    period = 0
    while True:
        x = (a * x + c) % m
        period += 1
        if x == x0:
            return period

# Tests
# Expected output: 4
print(period_generator(3, 7, 10, 1)) 