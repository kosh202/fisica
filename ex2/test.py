import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []

vo=10#m/s
g= 9.8
alpha = np.pi/4. # 45°

# np.sin(np.pi/2.) = sen(90°)

distanciaMax = ((vo*vo) * np.sin(np.pi/2))/ g

sen90 = np.around(np.sin(alpha)**2, 2)

Hmax = ((vo**2)* sen90)/(2*g)

voy = vo * np.sin(alpha)

vox = vo * np.cos(alpha)
 
tHmax = voy/g

Ttot = tHmax*2

fig, ax = plt.subplots()
ax.set_xlim(0, distanciaMax)
ax.set_ylim(0, Hmax)
line, = ax.plot(0, 0)

def altura(num):
    y = ((voy*num)-((g*(num**2))/2))
    #if (y >= Hmax):
	    
    return y_data.append(y)
    #elif (y <= Hmax):
       # y = voy*num+((g*(num**2))/2)
        #return y_data.append(num)

def distancia(num):
    x = vox*num
    return 	x_data.append(x)  



def animation_frame(i):
	distancia(i) 
	altura(i)

	line.set_xdata(x_data)
	line.set_ydata(y_data)
	return line, 

animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 10, 0.1), interval=10)
plt.show()