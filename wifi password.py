import os
import subprocess


def wifiName():
    a = input('Enter name of wifi: ')
    return a


x = wifiName()
#cmd = 'netsh wlan show profile name='+x+' key=clear'
a=subprocess.run(['netsh','wlan','show','profile','name=',x,'key=','clear'],shell=True,text=True,capture_output=True)
with open("password.txt","w") as f:
    f.write(a.stdout)
    f.close()