def eliminare_zerouri(cifre):
    while len(cifre) > 1 and cifre[0] == 0:
        cifre.pop(0)
    return cifre

def citire_numere_fisier(nume_fisier):
    try:
        with open(nume_fisier, "r") as f:
            linii = [linie.strip() for linie in f.readlines() if linie.strip() != ""]
        if len(linii) < 2:
            print("Fisierul trebuie sa contina doua numere pe linii separate!")
            return None, None
        s1, s2 = linii[0], linii[1]
        if not (s1.isdigit() and s2.isdigit()):
            print("Date invalide! Fisierul trebuie sa contina doar numere naturale.")
            return None, None
        if len(s1) > 200 or len(s2) > 200:
            print("Date invalide! Numerele pot avea cel mult 200 de cifre.")
            return None, None
        n1 = eliminare_zerouri([int(c) for c in s1])
        n2 = eliminare_zerouri([int(c) for c in s2])
        return n1, n2
    except FileNotFoundError:
        print("Fisierul numere.txt nu exista!")
        return None, None

def adunare(a, b):
    i = len(a) - 1
    j = len(b) - 1
    transport = 0
    rezultat = []
    while i >= 0 or j >= 0 or transport > 0:
        c1 = a[i] if i >= 0 else 0
        c2 = b[j] if j >= 0 else 0
        suma = c1 + c2 + transport
        rezultat.insert(0, suma % 10)
        transport = suma // 10
        i -= 1
        j -= 1
    return eliminare_zerouri(rezultat)

def inmultire(a, b):
    rezultat = [0]
    for i in range(len(b) - 1, -1, -1):
        cifra_b = b[i]
        produs_partial = []
        transport = 0
        for j in range(len(a) - 1, -1, -1):
            p = a[j] * cifra_b + transport
            produs_partial.insert(0, p % 10)
            transport = p // 10
        if transport > 0:
            produs_partial.insert(0, transport)
        zerouri = len(b) - 1 - i
        produs_partial.extend([0] * zerouri)
        rezultat = adunare(rezultat, produs_partial)
    return eliminare_zerouri(rezultat)

def afisare_numar(cifre):
    return "".join(str(c) for c in cifre)

if __name__ == "__main__":
    n1, n2 = citire_numere_fisier("numere.txt")
    if n1 is not None and n2 is not None:
        suma = adunare(n1, n2)
        produs = inmultire(n1, n2)
        print("Primul numar:", afisare_numar(n1))
        print("Al doilea numar:", afisare_numar(n2))
        print("Suma:", afisare_numar(suma))
        print("Produsul:", afisare_numar(produs))