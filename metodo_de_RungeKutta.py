import numpy as np


#É DE QUARTA ORDEM
h = 0.25


def f(x, y):
    f = y * (x ** 2) - y
    return f


x0 = 0  # começo do intervalo
xf = 1  # final no intervalo

n = (int)(xf / h)
print(n)
x_array = np.empty(n+1)
x_array[0] = 0
y_array = np.copy(x_array)
y_array[0] = 1

for i in range(n):
    k1 = h*f(x_array[i], y_array[i])
    k2 = h*f(x_array[i]+(h/2), y_array[i] + k1/2)
    k3 = h * f(x_array[i] + (h/2), y_array[i] + (k2/2))
    k4 = h * f(x_array[i] + h, y_array[i] + k3)
    x_array[i + 1] = x_array[i] + h
    y_array[i + 1] = y_array[i] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)

print(y_array)
print(x_array)