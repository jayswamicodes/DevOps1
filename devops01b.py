# df -h
# lscpu | grep 'CPU(s):' | head -1 | awk '{print}'
# lscpu | grep 'Core(s) per socket:' | head -1 | awk '{print}'
# free -h | grep 'Mem:' | awk '{print $2 $3 $4}'

import os
import commands
import sys

def volumes():
    os.system("df -h | awk \'{print}\'")

def cpu_info():
    # os.system("lscpu | grep \'CPU(s):\' | head -1 | awk \'{print}\'")
    status, output = commands.getstatusoutput("lscpu | grep \'CPU(s):\' | head -1 | awk \'{print}\'")
    print("CPU(s): ", output)
    # os.system("lscpu | grep \'Core(s) per socket:\' | head -1 | awk \'{print}\'")
    status, output = commands.getstatusoutput("lscpu | grep \'Core(s) per socket:\' | head -1 | awk \'{print}\'")
    print("Core(s) per socket: ", output)
    status, output = commands.getstatusoutput("cat /proc/cpuinfo")
    print('Printing CPU info .... ')
    print(output)
    # os.system('/proc/cpuinfo')

def ram():
    status, output = commands.getstatusoutput("free -h | grep \'Mem:\' | awk \'{print $2}\'")
    print("Total Memory: ", output)
    status, output = commands.getstatusoutput("free -h | grep \'Mem:\' | awk \'{print $3}\'")
    print("Used Memory: ", output)
    status, output = commands.getstatusoutput("free -h | grep \'Mem:\' | awk \'{print $4}\'")
    print("Free Memory: ", output)

def network(intf='lo'):
    cmd1 = 'ip addr show {}'.format(intf)
    cmd2 = ' | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\''
    ipv4 = os.popen(cmd1 + cmd2).read().strip()
    # ipv4 = os.popen('ip addr show {} | grep "\<inet\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\''.format(intf)).read().strip()
    cmd2 = ' | grep "\<ether\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\''
    mac = os.popen(cmd1 + cmd2).read().strip()
    # mac = os.popen('ip addr show {} | grep "\<ether\>" | awk \'{ print $2 }\' | awk -F "/" \'{ print $1 }\''.format(intf)).read().strip()
    print('eth0 ip address is  ', ipv4)
    print('eth0 mac address is', mac)

def arg_options():
    print('list of possible args: ...')
    print('1. volume : gives volumes on the system')
    print('2. cpu : gives number of CPUs/ cores per cpu with cpu info')
    print('3. ram: show ram info')
    print('4. network [interface_name]: to show ip / mac address of particular interface, default interface is loopback else enter interface name as additional arg')
    print('5. all : to display all of above info')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('No argument was  passed, pass an argument from below list')
        arg_options()
        sys,exit()

    arg = sys.argv[1]

    if arg == 'volume':
        volumes()

    elif arg == 'cpu':
        cpu_info()

    elif arg == 'ram':
        ram()

    elif arg == 'network':
        if len(sys.argv) < 3:
            network()
        else:
            network(sys.argv[2])

    elif arg == 'all':
        volumes()
        cpu_info()
        ram()
        if len(sys.argv) < 3:
            network()
        else:
            network(sys.argv[2])
    else:
        print('You entered an invalid arg : ', arg)
        arg_options()

