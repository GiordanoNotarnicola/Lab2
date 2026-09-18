import numpy as np
import matplotlib.pyplot as plt

dati=np.loadtxt("/home/studentelab2/dati_arduino/data1.txt")
Vdig=dati[:,1]

Valmed=np.average(Vdig)
bons=50

def gauss(x,mu,sigma):
    return (1/np.sqrt(2*np.pi*sigma**2))*np.exp(-0.5 * ((x-mu)/sigma)**2)

count,bins,boh=plt.hist(Vdig,bins=bons, range=(Valmed-(bons/2),Valmed+(bons/2)), edgecolor='black', density=True)

bin_centers=0.5 *(bins[1:]+bins[:-1])

popt,cov=curve_fit(gauss, bin_centers,count,p0=[Valmed,np.std(Vdig)])

mu,sigma=popt
print(cov)

print(f"Parametri", mu, sigma)

x_fit=np.linspace(bins[0], bins[-1],400)
plt.plot(x_fit,gauss(x_fit,*popt), color='red',lw=2, label="Fit Gaussiano")

plt.xlabel("Valori di Vdig")
plt.ylabel("Densita di probabilia")

plt.show()

# dati1=np.loadtxt("/home/studentelab2/dati_arduino/data.txt")
#
# t=dati1[:,0]
# for i in range(8191):
#     t[i]=t[i+1]-t[i]
#
# Valmed1=np.average(t)
# bonss=400
#
# countt,binss,bohh=plt.hist(t,bins=bonss, range=(Valmed1-(bonss/2),Valmed1+(bonss/2)), edgecolor='black', density=True)
# plt.yscale('log')
# plt.show()
# print(Valmed1)

