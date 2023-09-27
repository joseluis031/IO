from scipy.optimize import linprog

# Coeficientes de la función objetivo (maximizar D + 2E).
c = [-1, -2]

# Coeficientes de las restricciones (E + D ≤ 10, D = 2E, E ≤ 1, D ≤ 4)
A = [[1, 1], [-2, 1], [1, 0], [0, 1]]
b = [10, 0, 1, 4]

# Límites de las variables (E, D)
x_bounds = [(0, None), (0, None)]

# Resolver el problema de optimización lineal
res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

# Imprimir los resultados
E = res.x[0]  # Tiempo dedicado al estudio
D = res.x[1]  # Tiempo dedicado a la diversión

print(f"Tiempo de estudio (E): {E} horas")
print(f"Tiempo de diversión (D): {D} horas")
print(f"Nivel de interés máximo: {D + 2 * E}")



import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definir las variables simbólicas
E, D = sp.symbols('E D')

# Función objetivo a maximizar: D + 2E
interest = D + 2 * E

# Restricciones
constraint1 = E + D - 10  # E + D ≤ 10
constraint2 = D - 2 * E    # D = 2E
constraint3 = E - 1       # E ≤ 1
constraint4 = D - 4       # D ≤ 4

# Resolver las restricciones para obtener las curvas
constraint1_curve = sp.solve(constraint1, D)
constraint3_curve = sp.solve(constraint3, E)
constraint4_curve = sp.solve(constraint4, D)

# Crear un rango de valores para E y calcular D para cada valor
E_values = np.linspace(0, 3, 400)
D_values_constraint1 = np.array([constraint1_curve[0].subs(E, e) for e in E_values])
D_values_constraint3 = np.array([constraint3_curve[0].subs(E, e) for e in E_values])
D_values_constraint4 = np.array([constraint4_curve[0].subs(E, e) for e in E_values])

# Graficar las restricciones
plt.figure(figsize=(10, 6))
plt.plot(E_values, D_values_constraint1, label='E + D ≤ 10')
plt.plot(E_values, D_values_constraint3, label='E ≤ 1')
plt.plot(E_values, D_values_constraint4, label='D ≤ 4')

# Graficar la función objetivo
E_values_optimal = np.array([1])  # Valor óptimo de E
D_values_optimal = np.array([2])  # Valor óptimo de D
plt.scatter(E_values_optimal, D_values_optimal, color='red', marker='o', label='Máximo interés')

plt.xlabel('Tiempo de estudio (E)')
plt.ylabel('Tiempo de diversión (D)')
plt.legend()
plt.grid(True)
plt.title('Graficación de restricciones y función objetivo')
plt.xlim(0, 3)
plt.ylim(0, 6)
plt.show()

