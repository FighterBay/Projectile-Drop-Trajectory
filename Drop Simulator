from __future__ import division
from random import randint
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time


area_x = 0.025434
area_y =  0.0171
density = 1.223
Cd_x = 1.1
Cd_y = 1.1
m = 0.454
g = 9.81
vx_i = 33.333
vy_i = 0
ht = 35
dt = 0.001

vx_t = vx_i
vy_t = vy_i
t = 0

x_t = 0
y_t = 0
x_pl = []
y_pl = []
ctr = 0
def ax_t(density_f,area_x_f,Cd_x_f,m_f,vx_t_f):
    return -(density_f*area_x_f*(vx_t_f**2)*Cd_x_f/(2*m_f))

def ay_t(density_f,area_y_f,Cd_y_f,m_f,vy_t_f,g_f):
    a = 1/2*density_f*area_y_f*(vy_t_f**2)*Cd_y_f
    return (m_f*g_f - a)/m_f

while(ht > y_t):
    vx_t = vx_t + ax_t(density,area_x,Cd_x,m,vx_t)*dt
    vy_t = vy_t + ay_t(density,area_y,Cd_y,m,vy_t,g)*dt
    x_t = x_t + vx_t * dt
    y_t = y_t + vy_t * dt
    print "Vx @ ", t , vx_t
    print "Vy @ ", t , vy_t
    print "X @ ", t , x_t
    print "Y @ ", t , y_t
    x_pl.append(x_t)
    y_pl.append(-y_t)
    #ht = ht - y_t
    t = t + dt
    ctr = ctr + 1
print "Present UAV's Speed : " , vx_i , "m/s"
plt.plot(x_pl,y_pl)
plt.show()
