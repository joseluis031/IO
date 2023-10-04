# --------------------------------------------------------
# Ejercicio 1
# --------------------------------------------------------

# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "5+0*x"
f2 = "8-2*x"
x = symbols('x')
plot(f1, f2, (x, 0, 5))

# --------------------------------------------------------
# Ejercicio 2
# --------------------------------------------------------

# Modelo 1
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #<=
f2 = "1+x" #<=
#y=4
f3 = "4" #<=
Z1 = "(16-x)/2"
Z2 = "(14-x)/2"
Z3 = "(13-x)/2"
x = symbols('x')
plot(f1, f2, f3, Z1, Z2, Z3, (x, -15, 15))
# Sol: Z=14 x1=6 x2=4

# Modelo 1b
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x"
f2 = "x-1"
# x=4
#f3 = "4"
x = symbols('x')
plot(f1, f2, (x, 15, 0))


# Modelo 2
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #<=
f2 = "x-1" #>=
f3 = "4" # <=
Z1 = "(16-x)/2"
Z2 = "(14-x)/2"
Z3 = "(13-x)/2"
x = symbols('x')
plot(f1, f2, f3, Z1, Z2, Z3, (x, -15, 15))
# Sol: Z=13 x1=5 x2=4


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

 
# Modelo 1v1
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #<=
f2 = "1+x" #<=
#y=4
f3 = "4" #<=
Z1 = "16-x"
Z2 = "14-x"
Z3 = "13-x"
x = symbols('x')
plot(f1, f2, f3, Z1, Z2, Z3, (x, -1, 15))
# Sol: Z= x1= x2=


# Modelo 1v2
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "1+x" #<=
#y=4
f2 = "4" #<=
Z1 = "(16-x)/2"
Z2 = "(14-x)/2"
Z3 = "(13-x)/2"
x = symbols('x')
plot(f1, f2, Z1, Z2, Z3, (x, -1, 15))
# Sol: No acotada

# Modelo 1v3
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #<=
f2 = "1+x" #<=
#y=4
f3 = "4" #<=
x = symbols('x')
plot(f1, f2, f3, (x, -1, 15))
# Sol: múltiple


# Modelo 1V4
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #<=
f2 = "1+x" #<=
#y=4
f3 = "4" #<=
x = symbols('x')
plot(f1, f2, f3, (x, -1, 15))
# Sol: 


# --------------------------------------------------------
# R
# --------------------------------------------------------
f1 <- function(x){5+0*x}
f2 <- function(x){8-2*x}
curve(f1, col = "blue", lwd=2, xlab="X", ylab="Y", xlim = c(0,5), ylim = c(0,7), main="Title") 
curve(f2, col = "red", lwd=2, add = TRUE) 
grid()



# --------------------------------------------------------
# Python - matplotlib
# --------------------------------------------------------
from matplotlib import pyplot
def f1(x):
    return 5+0*x
def f2(x):
    return 8-2*x
x = range(0, 5)
pyplot.plot(x, [f1(i) for i in x])
pyplot.plot(x, [f2(i) for i in x])
# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(0, 5)
pyplot.ylim(0, 7)
# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")
# Mostrarlo.
pyplot.show()