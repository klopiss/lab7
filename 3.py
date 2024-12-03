import random
students = ["Катя", "Маша", "Вика", "Олег", "Алексей"]
sl = {}
for student in students:
    test = [random. randint(0,100) for _ in range(3)]
    summa = 0
    for score in test:
        summa += score
    ball = summa / 3
    sl[student] = ball
sl2 = sorted(sl.items(), key=lambda x: x[1], reverse=True)
print ("\nУченики по убыванию среднего балла: ")
for student, ball in sl2:
    print(f"Ученик {student}: {ball:.2f}")
