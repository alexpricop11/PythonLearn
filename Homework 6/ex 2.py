names = input("Introdu o lista de nume: ")
list_of_names = names.split(',')

list_of_marks = []

for name in list_of_names:
    mark = float(input(f"Introduceți nota pentru {name.strip()}: "))
    list_of_marks.append(mark)
for i in range(len(list_of_names)):
    print(f"{list_of_names[i].strip()} are nota: {list_of_marks[i]}")
marks_sum = 0
for mark in list_of_marks:
    marks_sum += mark
print(f"Suma notelor: {marks_sum}")
print(f"Media notelor: {marks_sum / len(list_of_marks)}")