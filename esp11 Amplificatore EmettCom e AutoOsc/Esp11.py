import pylab
import numpy as np
from scipy.optimize import curve_fit

Directory='/home/studentelab2/Lab2_files/gio e luca/' # <<<<<< now looking at a file in the datifit directory
NomeFile = 'esp11_dati.txt'   # <<<<<< now looking at a file called data00.txt
Filename=(Directory+NomeFile)
# data load
x,Dx,w,Dw,z,Dz=pylab.loadtxt(Filename,unpack=True)  # <<<<< the file is assumed to have 4 columns

Dz=Dz*2
y=z/w
Dy=(Dz/Dw)*(np.sqrt((Dz/z)**2+(Dw/w)**2))

# scatter plot with error bars
pylab.errorbar(x,y,Dy,Dx,linestyle = '', color = 'black', marker = '.')

# bellurie
pylab.rc('font',size=16)
pylab.xlabel('DeltaV  [V]',fontsize=18)
pylab.ylabel('I  [mA]',fontsize=18)
pylab.minorticks_on()

# AT THE FIRST STEP (data plot only) YOU MUST COMMENT FROM HERE TO THE LAST LINE (pylab.show())

Rc=0.994
Rb=0.563
rb=3.12e-3
b=249
C=0.22e-6

# make the array with initial values (to be carefully adjusted!)
init=(0.22e-6, 200)

# set the error (to be modified if effective errors have to be accounted for)
sigma=Dy
w=1/sigma**2

# define the model function (a straight line in this example)
# note how parameters are entered
# note the syntax
def ff(x, a, b):
    return np.abs(-(Rc/(Rb+rb))*b*((1-1j*(2*np.pi*x)*(Rb+rb)*(C/b))/(1+1j*(2*np.pi*x)*a)))

# AT THE SECOND STEP (plot of the model with initial parameters):
# YOU MUST COMMENT FROM HERE TO THE THIRD TO LAST LINE
# (AND PUT IN THAT LINE *init IN THE PLACE OF *pars)
# call the routine
pars,covm=curve_fit(ff,x,y,init,sigma,absolute_sigma=True) # <<<< NOTE THE absolute_sigma option

# calculate the kappasquare for the best-fit funtion
# note the syntax for the pars array
kappa2 = (w*(y-ff(x,*pars))**2).sum()

# determine the ndof
ndof=len(str(x))-len(str(init))

# print results on the console
print(pars)
print(covm)
print (kappa2, ndof)


# AT THE SECOND STEP, COMMENT UP TO HERE
# prepare a dummy xx array (with 500 linearly spaced points)
xx=np.linspace(min(x),max(x),500)
pylab.xscale('log')
pylab.yscale('log')



# plot the fitting curve with either the initial or the optimised parameters
# AT THE SECOND STEP, YOU MUST REPLACE *pars WITH *init
pylab.plot(xx,ff(xx,*pars), color='red')


pylab.tight_layout() # reuired to properly adjust the plot window size

# show the plot
pylab.show()
