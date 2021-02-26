import os

def wifiName():
    a = input('Enter name of wifi: ')
    return a

x = wifiName()
cmd = 'netsh wlan show profile name='+x+' key=clear'
os.system(cmd)
