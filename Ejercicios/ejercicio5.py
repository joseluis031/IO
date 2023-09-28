'''

# Modelo 1b
# Importar el módulo SymPy 
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x"
f2 = "x-1"
f3 = "4"
x = symbols('x')
plot(f1, f2, f3, (x, 15, 0))

# Modelo 2
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #<=
f2 = "x-1" #>=
f3 = "4" # <=
x = symbols('x')
plot(f1, f2, f3, (x, 15, 0))


# Modelo 3
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #<=
f2 = "x+1" #<=
f3 = "x-1" #>=
f4 = "4" # <=
x = symbols('x')
plot(f1, f2, f3, f4, (x, 15, 0))

'''

# Modelo 1
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #<=
f2 = "1+x" #<=
#y=4
f3 = "4"  #<=
Z1 = "(16-x)/2"
Z2 = "(14-x)/2"  #esta es la solucion
Z3 = "(13-x)/2"
x = symbols('x')
plot(f1, f2, f3, Z1, Z2, Z3, (x, 15, 0))

# sol Z=14 x1=6 x2=4
