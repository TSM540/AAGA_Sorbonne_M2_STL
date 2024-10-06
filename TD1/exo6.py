def find_mu_lambda(f, X0):
    tortoise = X0
    hare = f(X0)
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
    mu = 0
    tortoise = X0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1
    
    lambda_ = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lambda_ += 1
    
    return mu, lambda_

def f(x):
    return (x * x + 1) % 10  

X0 = 2  
mu, lambda_ = find_mu_lambda(f, X0)
print(f"µ = {mu}, λ = {lambda_}")
