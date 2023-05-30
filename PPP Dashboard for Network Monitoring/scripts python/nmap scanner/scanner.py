# -*- coding: utf-8 -*-
"""
Created on Mon May 29 10:50:15 2023

@author: 21650
"""

import nmap 
import subprocess
import re
import json

def scan_network(subnet):
    # Run the nmap command and get the output
    nmap_command = ["nmap", "-p", "161", "--open", "-sU", "-sS", "--script=snmp-netstat", "-oN", "scan_results.txt", subnet]
    subprocess.run(nmap_command, capture_output=True)

    # Parse the SNMP scan results from the output file
    network_devices = parse_snmp_scan_results()

    # Return the results as a JSON string for easy printing
    return json.dumps(network_devices, indent=4)

def parse_snmp_scan_results():
    # Read the scan results from the output file
    with open("scan_results.txt", "r") as file:
        output = file.read()

    # Initialize the dictionary to hold the results
    network_devices = {}

    # Parse the output
    lines = output.split("\n")
    for line in lines:
        # Extract relevant information from each line
        if "Nmap scan report for" in line:
            ip_match = re.search(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", line)
            if ip_match:
                ip = ip_match.group()
                network_devices[ip] = {"mac": None, "vendor": None}
        elif "MAC Address:" in line:
            mac_match = re.search(r"(([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))", line)
            if mac_match:
                mac = mac_match.group()
                vendor = line.split("(")[1].split(")")[0]
                network_devices[ip]["mac"] = mac
                network_devices[ip]["vendor"] = vendor

    return network_devices

"""
subnets = ['192.168.1.0/24', '192.168.2.0/24', '192.168.3.0/24', '192.168.4.0/24','192.168.5.0/24','192.168.6.0/24','192.168.10.0/24']

for subnet in subnets:
    print(scan_network(subnet))
"""