import pylab
import numpy as np
from scipy.optimize import curve_fit


Directory='/home/studentelab2/Lab2_files/datifit/' # <<<<<< now looking at a file in the datifit directory
NomeFile = 'es3dati.txt'   # <<<<<< now looking at a file called data00.txt
Filename=(Directory+NomeFile)
# data load
x,Dx,y,Dy=pylab.loadtxt(Filename,unpack=True)  # <<<<< the file is assumed to have 4 columns

# scatter plot with error bars
pylab.errorbar(x,y,Dy,Dx,linestyle = '', color = 'black', marker = '.')

# bellurie
pylab.rc('font',size=16)
pylab.xlabel('$V_{dig}$  [digit]',fontsize=18)
pylab.ylabel('$V_v$  [V]',fontsize=18)
pylab.minorticks_on()

# AT THE FIRST STEP (data plot only) YOU MUST COMMENT FROM HERE TO THE LAST LINE (pylab.show())


# make the array with initial values (to be carefully adjusted!)
init=(2.1,0)

# set the error (to be modified if effective errors have to be accounted for)
sigma=Dy
w=1/sigma**2

# define the model function (a straight line in this example)
# note how parameters are entered
# note the syntax
def ff(x, a, b):
    return a*x+b

# AT THE SECOND STEP (plot of the model with initial parameters):
# YOU MUST COMMENT FROM HERE TO THE THIRD TO LAST LINE
# (AND PUT IN THAT LINE *init IN THE PLACE OF *pars)
# call the routine
pars,covm=curve_fit(ff,x,y,init,sigma,absolute_sigma=True) # <<<< NOTE THE absolute_sigma option
for i in range(4):
    sigma=np.sqrt(sigma**2+(pars[0]*Dx)**2)
    w=1/sigma**2
    pars,covm=curve_fit(ff,x,y,init,sigma,absolute_sigma=True)
# calculate the kappasquare for the best-fit funtion
# note the syntax for the pars array
kappa2 = (w*(y-ff(x,*pars))**2).sum()

# determine the ndof
ndof=len(x)-len(init)

# print results on the console
print(pars)
print(covm)
print (kappa2, ndof)


# AT THE SECOND STEP, COMMENT UP TO HERE
# prepare a dummy xx array (with 500 linearly spaced points)
xx=np.linspace(0,4000,500)



# plot the fitting curve with either the initial or the optimised parameters
# AT THE SECOND STEP, YOU MUST REPLACE *pars WITH *init
#pylab.errorbar(x, y, yerr=Dy, fmt='.', label='Dati')
pylab.plot(xx,ff(xx,*pars), color='red')


pylab.tight_layout() # reuired to properly adjust the plot window size

# show the plot
pylab.show()
