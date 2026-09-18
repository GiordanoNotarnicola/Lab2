import pylab
import numpy as np
from scipy.optimize import curve_fit

Directory='/home/studentelab2/Lab2_files/gio e luca/esp14/' # <<<<<< now looking at a file in the datifit directory
NomeFile = 'esp14data.txt'   # <<<<<< now looking at a file called data00.txt
Filename=(Directory+NomeFile)
# data load
x,Dx,k,Dk, z, Dz=pylab.loadtxt(Filename,unpack=True)  # <<<<< the file is assumed to have 4 columns
# scatter plot with error bars

y=z/k
Dz/=np.sqrt(12)
Dk/=np.sqrt(12)
Dy=np.sqrt((Dk/k)**2+(Dz/z)**2)*y
sigma=Dy


w=1/sigma**2

pylab.errorbar(x,y,Dy,Dx,linestyle = '', color = 'black', marker = '.')

Dy=np.full_like(y,3)
# bellurie
pylab.rc('font',size=16)
pylab.xlabel('Frequenza  [Hz]',fontsize=18)
pylab.ylabel('Guadagno',fontsize=18)
pylab.minorticks_on()

# AT THE FIRST STEP (data plot only) YOU MUST COMMENT FROM HERE TO THE LAST LINE (pylab.show())


# make the array with initial values (to be carefully adjusted!)
#nit=(1.4e3, 1.3e2, 3.4e-3 , 1.7, 1.65e3)
#init=(1e3, 1.5e2, 3.2e-3 , 17., 1.7e3)
#init=(0.7e3, 1e2, 3e-3 , 1.7, 1.8e3)

#init=(0.7e3, 1e2, 3e-3 , 1.7, 1.8e3)
init=(0.47e-7, 720, 16)

R=329


# set the error (to be modified if effective errors have to be accounted for)

# define the model function (a straight line in this example)
# note how parameters are entered
# note the syntax
def ff(x, C, omega, r):
    return (2*np.pi*x*R*C)/np.sqrt((1-(x/omega)**2)**2+(2*np.pi*x*(R+r)*C)**2)

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
print (kappa2/ndof)

print(pars)
print(np.diag(np.sqrt(covm)))

# AT THE SECOND STEP, COMMENT UP TO HERE
# prepare a dummy xx array (with 500 linearly spaced points)
xx=np.linspace(min(x),max(x),500)



# plot the fitting curve with either the initial or the optimised parameters
# AT THE SECOND STEP, YOU MUST REPLACE *pars WITH *init
pylab.plot(xx,ff(xx,*pars), color='red')


pylab.tight_layout() # reuired to properly adjust the plot window size

# show the plot
pylab.show()
