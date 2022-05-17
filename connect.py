import intertools as it
import pywifi
import time
import subprocess
import socket

names=[]

PLC151Port1Address=192.168.151.2
PLC151Port2Address=10.40.90.151

PLC141Port1Address=192.168.141.2
PLC141Port2Address=10.40.90.141

PLC131Port1Address=192.168.131.2
PLC131Port2Address=10.40.90.131

PLC121Port1Address=192.168.121.2
PLC121Port2Address=10.40.90.121

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


def internet(host="8.8.8.8", port=53, timeout=3):
    #check connection to internet / Firewall, using trying to connect to public google dns socket tcp
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False

#dumb but work
def tryEveryAddInSub():
    for ping in range(1,254):
    address = "10.40.90." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0:
        print( "ping to", address, "OK")
        print(socket.gethostname())
        print(socket.gethostbyaddr(socket.gethostname())[address])
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")
        
def writeAllNetworksNames():
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    data = meta_data.decode('utf-8', errors ="backslashreplace")
    data = data.split('\n')
    for i in data:
     
    if "All User Profile" in i :
        i = i.split(":")
        i = i[1]
        i = i[1:-1]
        names.append(i)
    for name in names:
        print(name)



  
    
   
    
