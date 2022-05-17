import intertools as it
import pywifi
import time
import subprocess

#subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)

def searchNetworks():
    devices = subprocess.check_output(['netsh','wlan','show','network'])
    devices = devices.decode('ascii')
    devices= devices.replace("\r","")
    print(devices)



def getPasswordsFile():
    dic=open('./passwords.txt','a')#
    t=its.product(words,repeat=3)#
    for i in t:
        #Try
    dic.close()
 
def WifiConnect(pwd):
    wifi=pywifi.PyWiFi()#
    ifaces=wifi.interfaces()[0]#
    iface.disconnect()#
    time.sleep(1)#
    status=ifces.status()#
    if status==const.IFACE_DISCONNECTED:
        profile=pywifi.Profile()#wifi
        profile.ssid='gebilaowang'#wifi
        profile.auth=const.AUTH_ALG_OPEN#
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#wifi,wifiwps
        profile.clipher=const.CIPHER_TYPE_CCMP#
        profile.key=pwd#
        ifaces.remove_all_network_profiles()#
        tep_profile=ifaces.add_network_profile(profile)
        ifaces.connect(tep_profile)
        time.sleep(3)#,wifi,
        if ifaces.status()==const.IFACE_CONNECTED:#
            return True
        else:
            return False
    else:
        print('wifi,')
 
import socket

def internet(host="8.8.8.8", port=53, timeout=3):
    #check connection to internet / Firewall, using trying to connect to public google dns socket tcp
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False



  
    
   
    
