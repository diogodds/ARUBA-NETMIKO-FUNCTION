#!/usr/bin/env python

from netmiko import ConnectHandler 
from datetime import datetime
import sys
import getpass
import re
 
 #######################################################################
 # Warnings module needed to be imported to solve a connection mode    #
 # deprecated warrning that I was geting when trying to connect to     #
 # the juniper switches                                                #
 #######################################################################

import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')

########################################################################

def ntmk_aruba(command):
	net_connect.send_command(command, expect_string=r"#")


########################################################################
host = '172.16.7.3'
username = 'manager'
password = getpass.getpass()

########################################################################

#list_of_devices = ['10.23.4.54',
#                   '10.23.4.55',
#                   '10.23.4.59',
#                  ]
#list_of_devices = open('ARUBA-DEVICES.txt','r')

#with open('ARUBA-DEVICES.txt') as file: # This opens the text file with the name ARUBA-DEVICES.txt in csv format (IP,hostname)
#    list_of_devices = file.read().splitlines() # The file is loaded into the "list_of_devices" variable and splited into lines

#######################################################################

#for line in list_of_devices:
#  host_to_create = line.split(',') #this will create a list by spliting the line into two elements, considering the coma as delimiter for the strip.
#  octects = host_to_create[0].split('.')
  
print('Establishing connection to ' + host)
 
start_time = datetime.now()

net_connect = ConnectHandler(device_type='hp_procurve', ip=host, username=username, password=password, global_delay_factor=3.5)
  
print('Connected to ' + host)
  
net_connect.send_command('\n')
ntmk_aruba('conf t')
ntmk_aruba('vlan 144')
ntmk_aruba('name PHOTO-STUDIO')
ntmk_aruba('save')
end_time = datetime.now()
print('\nTotal time: {}'.format(end_time - start_time))
print('Configuration successfully applied to the device ' + host +'\n\n' + '#' * 60)