student_1 = []
numele_1 = input("Inroduceti numele primului student: ")
student_1.append(numele_1)
nota1 = float(input("Introduceti nota primului student: "))
student_1.append(nota1)
student_2 = []
numele_2 = input("Inroduceti numele al doilea student: ")
nota2 = float(input("Introduceti nota al doilea student student: "))
student_2.append(nota2)
if nota1 > nota2:
    print(f"Studentul {numele_1} are nota mai mare ca studentul {numele_2}")
elif nota1 < nota2:
    print(f"Studentul {numele_2} are nota mai mare ca studentul {numele_1}")
else:
    print("Studentii au nota egala")