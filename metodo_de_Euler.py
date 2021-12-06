import numpy as np

h = 0.25


def f(x, y):
    f = y * (x ** 2) - y
    return f


x0 = 0  # começo do intervalo
xf = 1  # final no intervalo

n = (int)(xf / h)
print(n)
x_array = np.empty(n)
x_array[0] = 0
y_array = np.copy(x_array)
y_array[0] = 1

for i in range(n-1):
    x_array[i + 1] = x_array[i] + h
    y_array[i + 1] = y_array[i] + h * f(x_array[i], y_array[i])

print(y_array)
