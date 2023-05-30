from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship




############################################################################################################
# Create the tables

engine = create_engine("mysql+mysqlconnector://root:@127.0.0.1/ppp")

Base = declarative_base()


class Device(Base):
    __tablename__ = 'device'
    device_id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    device_type = Column(String(length=255))    # (e.g., router, switch, server, etc.)

    interfaces = relationship('Interface')

class Interface(Base):
    __tablename__ = 'interface'
    interface_id = Column(Integer, primary_key=True)
    interface_name = Column(String(length=255))    # The name or label assigned to the interface
    interface_type = Column(String(length=255))    # (e.g., Ethernet, Wi-Fi, WAN, etc.)
    status = Column(String(length=50))    
    ip_address = Column(String(length=50))    
    subnet_mask = Column(String(length=50))
    mac_address = Column(String(length=50))
    device_id = Column(Integer, ForeignKey('device.device_id'))
    metrics = relationship('InterfaceMetric')

class InterfaceMetric(Base):
    __tablename__ = 'interface_metric'

    metric_id = Column(Integer, primary_key=True)
    interface_id = Column(Integer, ForeignKey('interface.interface_id'))
    timestamp = Column(DateTime)    # The timestamp indicating when the metric data was recorded
    traffic_in = Column(Integer)    # The amount of incoming network traffic on the interface (e.g., in bytes, packets)
    traffic_out = Column(Integer)    # The amount of outgoing network traffic on the interface (e.g., in bytes, packets)
    errors = Column(Integer)    # The number of errors or issues encountered on the interface
    packet_loss = Column(Float)    # The percentage of packet loss on the interface
    latency = Column(Float)    # The measured latency or round-trip time on the interface
    bandwidth = Column(Float)    # The current bandwidth utilization on the interface


class DeviceMetric(Base):
    __tablename__ = 'device_metric'

    metric_id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey('device.device_id'))
    timestamp = Column(DateTime)
    cpu_utilization = Column(Float)
    cpu_temperature = Column(Float)
    ram_utilization = Column(Float)
    disk_usage = Column(Float) 
    power_usage = Column(Float)

class Packet(Base):
    __tablename__ = 'packet'
    packet_id = Column(Integer, primary_key=True)
    timestamp = Column(String(length=255))
    source_ip = Column(String(length=255))
    destination_ip = Column(String(length=255))
    source_port = Column(Integer)
    destination_port = Column(Integer)
    protocol = Column(String(length=255))
    payload = Column(String(length=255))

class TrafficClass(Base):
    __tablename__ = 'traffic_class'
    class_id = Column(Integer, primary_key=True)
    class_name = Column(String(length=255))
    description = Column(String(length=255))

class PacketTraffic(Base):
    __tablename__ = 'packet_traffic'
    packet_id = Column(Integer, ForeignKey('packet.packet_id'), primary_key=True)
    class_id = Column(Integer, ForeignKey('traffic_class.class_id'), primary_key=True)
    
    packet = relationship(Packet)
    traffic_class = relationship(TrafficClass)


Base.metadata.create_all(engine)
############################################################################################################