import numpy as np
while True:
    try:
        M = int(input("Введите количество строк: "))
        N = int(input("Введите количество столбцов: "))
        if M <= 0 or N <= 0:
            print ("Размеры матрицы должны быть положительными числами.")
            continue
        break
    except ValueError:
        print("Ошибка: надо ввести целое число")
matrix = np.random.randint(1, 100, (M, N))
print("Сгенерированная матрица: ")
print(matrix)
res = []
for i in range(M):
    if i % 2 == 0:
        res.extend(matrix[i, :])
    else:
        res.extend(matrix[i, ::-1])
res = [int(x) for x in res]
print ("\nЭлементы в заданном порядке: ")
print(res)