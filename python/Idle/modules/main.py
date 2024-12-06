#1. import page you want simply
'''
import myModule
myModule.greet
 '''
 
#2. import myModule as keyword :

import myModule as m

m.greet
print("-----------------------------------------------")

#3. system module : gives names of system i.e windows

import platform

x=platform.system()
print(x)
print("-----------------------------------------------")

#4.

x = dir(platform)
print("gives ",x)
