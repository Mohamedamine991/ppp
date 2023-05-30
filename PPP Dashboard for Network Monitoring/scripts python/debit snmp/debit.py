from pysnmp.hlapi import *
import time
from datetime import datetime
def f(ipadd):
    data = ObjectType(ObjectIdentity('.1.3.6.1.2.1.2.2.1.16.1'))
    last_reading = None
    last_timestamp = None
    
    while True:
        timestamp = datetime.now()
        g = getCmd(SnmpEngine(), CommunityData('com', mpModel=0)
               , UdpTransportTarget((ipadd, 161))
               , ContextData() , data)
        errorIndication, errorStatus, errorlndex, varBinds = next(g)
    
        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('error status')
        else:
            if last_reading is not None:
                volume_diff = int(varBinds[0][1]) - last_reading
                time_diff = (timestamp - last_timestamp).total_seconds()
                rate = volume_diff / time_diff
                
                print(f'{rate:.2f} bytes per second')
                print(volume_diff)
                print(timestamp)

                with open("taux.txt", "w") as f:
                    f.write(f'{rate:.2f}\n')
                    
            last_reading = int(varBinds[0][1])
            last_timestamp = timestamp
        time.sleep(3)
    

ipadd='192.168.5.1'
f(ipadd)
