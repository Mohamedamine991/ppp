from pysnmp.hlapi import *
import time
from datetime import datetime
data = (
    ObjectType(ObjectIdentity('1.3.6.1.4.1.9.9.48.1.1.1.5.1')),  # RAM USED
    ObjectType(ObjectIdentity('1.3.6.1.4.1.9.9.48.1.1.1.6.1'))   # RAM FREE
)
def getter(targetIp, data, labels=['']*len(data)):
    resultMatrix = []
    g = getCmd(SnmpEngine(), CommunityData('com', mpModel=0),
               UdpTransportTarget((targetIp, 161)), ContextData(), *data)

    errorIndication, errorStatus, errorlndex, varBinds = next(g)

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('error status ')
    else:
        i = 0
        for varBind in varBinds:
            l = [str(x) for x in varBind]
            resultMatrix.append([labels[i], l[0], l[1]])
            i += 1
    return resultMatrix

def calculate_percentage(used, free):
    return round((used / free) * 100, 2)

def write_result_to_file(result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    percentage = calculate_percentage(int(result[0][2]), int(result[1][2]))
    with open('ramUsage.txt', 'a') as file:
        file.write(f'{timestamp} {percentage}\n')
