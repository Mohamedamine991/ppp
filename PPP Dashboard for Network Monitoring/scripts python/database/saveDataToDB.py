from sqlalchemy.orm import sessionmaker


from createTables import Device,TrafficClass, Interface, InterfaceMetric, DeviceMetric , Base , engine


Session = sessionmaker(bind=engine)
session = Session()


# Adding data to the Device table
device1 = Device(name='Device 1')
session.add(device1)


# Create instances of TrafficClass and add them to the session
traffic_classes = [
    TrafficClass(class_name='Browsing', description='Network traffic related to web browsing activities'),
    TrafficClass(class_name='File Transfer', description='Network traffic involving the transfer of files'),
    TrafficClass(class_name='Mail', description='Network traffic related to email communication'),
    TrafficClass(class_name='Remote Jobs', description='Network traffic associated with remote job execution or remote command execution'),
    TrafficClass(class_name='Time', description='Network traffic involved in time synchronization protocols'),
    TrafficClass(class_name='DNS', description='Network traffic related to the Domain Name System'),
    TrafficClass(class_name='NetBIOS', description='Network traffic associated with the NetBIOS protocol'),
    TrafficClass(class_name='Error Reports', description='Network traffic involved in the transmission of error reports or diagnostic information'),
    TrafficClass(class_name='Auth', description='Network traffic related to authentication and authorization processes'),
    TrafficClass(class_name='Search', description='Network traffic associated with search engines or search functionalities'),
    TrafficClass(class_name='Kerberos', description='Network traffic related to the Kerberos authentication protocol'),
    TrafficClass(class_name='Unix', description='Network traffic associated with Unix-based systems'),
    TrafficClass(class_name='Telnet', description='Network traffic related to the Telnet protocol'),
    TrafficClass(class_name='Text Services', description='Network traffic associated with text-based services'),
    TrafficClass(class_name='Others', description='General category for network traffic that does not fit into any specific class'),
    TrafficClass(class_name='Private', description='Network traffic related to private or internal network communications'),
    TrafficClass(class_name='Virtual Network', description='Network traffic associated with virtual network technologies'),
    TrafficClass(class_name='Oracle', description='Network traffic related to Oracle database systems'),
    TrafficClass(class_name='Media', description='Network traffic associated with media streaming')
]

session.add_all(traffic_classes)


# Commit the changes to persist the data in the database
session.commit()

session.close()




