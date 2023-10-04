from scipy.optimize import linprog

# Coeficientes de la función objetivo a minimizar (-Z)
c = [-6, -3]

# Coeficientes de las restricciones en el lado izquierdo (lado derecho de las desigualdades)
A = [
    [2, 4],
    [-1, 4],
    [1, -1]
]

# Lados derechos de las restricciones
b = [8, 4, 2]

# Límites de las variables de decisión (x1 y x2)
x_bounds = [(0, None), (0, None)]

# Resolver el problema de optimización lineal
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

# Extraer la solución óptima
x1_opt = result.x[0]
x2_opt = result.x[1]
Z_opt = -result.fun  # El valor óptimo de Z es el negativo del valor de la función objetivo minimizada

# Imprimir la solución óptima
print("Solución óptima:")
print("x1 =", x1_opt)
print("x2 =", x2_opt)
print("Z =", Z_opt)

import numpy as np
import matplotlib.pyplot as plt

# Definir las restricciones como desigualdades
x = np.linspace(0, 10, 400)
y1 = (8 - 2 * x) / 4
y2 = (4 + x) / 4
y3 = x - 2

# Definir las restricciones como límites en el gráfico
plt.plot(x, y1, label=r'$2x_1 + 4x_2 \leq 8$')
plt.plot(x, y2, label=r'$-x_1 + 4x_2 \leq 4$')
plt.plot(x, y3, label=r'$x_1 - x_2 \leq 2$')

# Restringir el área de trazado
plt.xlim((0, 10))
plt.ylim((0, 10))

# Rellenar la región factible
plt.fill_between(x, 0, np.minimum.reduce([y1, y2, y3]), where=(y1 >= 0) & (y2 >= 0) & (y3 >= 0), alpha=0.2)

# Resaltar la solución óptima
plt.scatter(x1_opt, x2_opt, color='red', marker='o', label='Solución óptima')

# Etiquetas de ejes y leyenda
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.legend()

# Mostrar el gráfico
plt.show()
