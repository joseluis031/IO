# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x"
f2 = "x-1"
f3 = "4-0*x"
z= sym.symbols('z')
x = symbols('x')
plot(f1, f2, f3, (x, 0,10), title='Gráfica de funciones', xlabel='x', ylabel='y', legend=True)
