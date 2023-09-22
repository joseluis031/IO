# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "5+0*x"
f2 = "8-2*x"
f3 = "-4/5*x+6.2"
z= sym.symbols('z')
x = symbols('x')
plot(f1, f2, f3, (x, -5, 5), title='Gráfica de funciones', xlabel='x', ylabel='y', legend=True)
