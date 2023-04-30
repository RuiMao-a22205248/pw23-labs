def positivo(n):
    return n > 0

def par(n):
    return n % 2 == 0

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
