'''
Drop trajectory simulator
'''

import pygame, sys
from pygame.locals import *
import time
img_red = pygame.image.load('redbox.bmp')
img_green = pygame.image.load('greenbox.bmp')
area_x = 0.025434
area_y =  0.0171
density = 1.223
Cd_x = 1.1
Cd_y = 1.1
m = 0.454
g = 9.81
vx_i = 33
vy_i = 0
ht = 35
dt = 0.01

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

pygame.init()
wid = 640
ht = 480
DISPLAY=pygame.display.set_mode((wid,ht),0,32)
black=(0,0,0)

DISPLAY.fill(black)
pygame.display.flip()
while(ht > y_t):
    vx_t = vx_t + ax_t(density,area_x,Cd_x,m,vx_t)*dt
    vy_t = vy_t + ay_t(density,area_y,Cd_y,m,vy_t,g)*dt
    x_t = x_t + vx_t * dt
    y_t = y_t + vy_t * dt

    x_t_nd = vx_i * t
    y_t_nd = 0.5*g*t*t
    t = t + dt


    oldRect = img_red.get_rect(center=(x_t,y_t))
    DISPLAY.blit(img_red, oldRect)
    oldRect = img_green.get_rect(center=(x_t_nd,y_t_nd))
    DISPLAY.blit(img_green, oldRect)
    pygame.display.update()
