#!/bin/python3


#########################################
#
#   Author: https://github.com/Exploit-py
#   date: 09/09/2022
#

import argparse
import pyfiglet
from EyeMap_threading import *


def banner():
    banner = pyfiglet.figlet_format("EyeMap")
    print(f"{banner}\nAuthor: Exploit-py\nDate: 09/09/2022\n")


parser = argparse.ArgumentParser(description='Scan host ports')

parser.add_argument('host', type=str,help='A required host to scan\n')
parser.add_argument('--port_range', "-pR", type=int, help='Range to scan. Default: 1-1024\n')
parser.add_argument('--threads', "-T", type=int, help='Default: 50\n')
parser.add_argument('--verbose', '-v', action='store_true', help='Verbose mode\n')
parser.add_argument('--serverVersion', '-sV', action='store_true', help='Enables version detection\n')

args = parser.parse_args()

host = args.host
port_range = args.port_range
verbose = args.verbose
threads = args.threads
serverVersion = args.serverVersion

print(f"""
--------CONFIG--------
HOST: {host}
Port Range: {"1024" if port_range is None else port_range}
Server Version: {serverVersion}
Threads: {"50" if threads is None else threads}
Verbose: {verbose}
----------------------
""")

banner()

obj = PortScanner_Thread(host, port_range, verbose, threads, serverVersion)

if serverVersion:
    obj.scanner()
    obj.server_version()
else:
    obj.scanner()
    obj.show_output()
