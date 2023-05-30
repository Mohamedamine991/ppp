from sqlalchemy.orm import sessionmaker
from createTables import Device, Interface, InterfaceMetric, DeviceMetric, Base, TrafficClass ,engine

Session = sessionmaker(bind=engine)
session = Session()

# Querying data from the Device table
devices = session.query(Device).all()
# Printing the retrieved data
for device in devices:
    print(f"Device ID: {device.device_id}, Device Name: {device.name}")


# Querying data from the Device table
classes = session.query(TrafficClass).all()
# Printing the retrieved data
for clas in classes:
    print(f"class ID: {clas.class_id}, TrafficClass Name: {clas.class_name}")

# Closing the session
session.close()
