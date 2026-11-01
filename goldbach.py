def este_prim(x):
    if x < 2:
        return False
    for d in range(2, x // 2 + 1):
        if x % d == 0:
            return False
    return True

def citire_numar():
    try:
        n = int(input("Introduceti un numar natural par (n > 2): "))
        if n <= 2 or n % 2 != 0:
            print("Valoare invalida! Numarul trebuie sa fie par si mai mare decat 2.")
            return None
        return n
    except ValueError:
        print("Valoare invalida! Introduceti un numar intreg.")
        return None

def afisare_goldbach(n):
    print(f"Descompunerile Goldbach pentru {n} sunt:")
    for p in range(2, n // 2 + 1):
        q = n - p
        if este_prim(p) and este_prim(q):
            print(f"{n} = {p} + {q}")

if __name__ == "__main__":
    n = citire_numar()
    if n is not None:
        afisare_goldbach(n)