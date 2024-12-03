import numpy as np
while True:
    try:
        M = int(input("Введите размер матрицы(MxM): "))
        if M <= 0:
            print("Размер матрицы должен быть положительным числом:")
            continue
        break
    except ValueError:
        print("Ошибка: введите целое положительное число: ")
matrix = np.random.randint(0, 100, (M,M))
print ("\nСгенерированная матрица")
print(matrix)
sort = np.argsort(-matrix[0, :])
sortm = matrix[:, sort]
print ("\nМатрица после сортировки значений:")
print (sortm)