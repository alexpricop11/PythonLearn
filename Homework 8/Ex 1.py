numar_de_termeni = 20

a, b = 0, 1

print(f"Primele {numar_de_termeni} numere din secvența Fibonacci sunt:", end=" ")

for _ in range(numar_de_termeni):
    print(a, end=", ")
    a, b = b, a + b
