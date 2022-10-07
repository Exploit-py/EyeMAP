#!/bin/python3

import nmap
import socket
import subprocess
from queue import Queue
from threading import Thread, Lock


class PortScanner_Thread:
    def __init__(self, host: str, portRange=1024, verbose=False, threads=50, serverVersion=True):
        self.host = host
        self.portRange = portRange
        self.verbose = verbose
        self.threads = threads
        self.serverVersion = serverVersion
        self.logs = {}
        self.tqueue = Queue()
        self.sync = Lock()

    def filter_nmap_output(self, output:str):
        begin = output.find("PORT")
        end = output.find("Service detection")
        print(output[begin-1:end-2])

    def server_version(self):
        _ports = ",".join([(str(x)) for x,y in self.logs.items()])
        print("\nChecking version, wait...\n")
        _scan = nmap.PortScanner()
        r = _scan.scan(self.host, ports=_ports, arguments="-sV -Pn")
        try:
            r2 = r["scan"][self.host]["tcp"]
            print(f"{'-'*22}\n")
            for x,y in r2.items():
                print(f"PORT: {x:<3}\n   Protocol: {y['name']}\n   Product: {y['product']}\n   Version: {y['version']}\n")
            print(f"{'-'*22}")

        except:
            process = subprocess.Popen(f"nmap {self.host} -sV -p{_ports} -Pn", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            print(f"{'-'*22}\n")
            self.filter_nmap_output(output.decode())
            print(f"{'-'*22}\n")
            
            

    def show_output(self):
        print(f"{'-'*22}")
        for x,y in self.logs.items():
            print(f"{x}: {y}")
        print(f"{'-'*22}")

    def scanPorts(self, portQueue): # default 
        if not self.verbose: # Verbose OFF
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.3)
                s.connect((self.host, portQueue))

            except:
                pass
            else:
                with self.sync: # evitar erro entre as chamadas das threads
                    try:
                        name = socket.getservbyport(portQueue)
                        self.logs[portQueue] = name
                    except OSError:
                        self.logs[portQueue] = "Open"
            finally:
                s.close()

        else: # Verbose ON
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.3)
                s.connect((self.host, portQueue))

            except:
                pass
            else:
                with self.sync: # evitar erro entre as chamadas das threads
                    try:
                        name = socket.getservbyport(portQueue)
                        self.logs[portQueue] = name
                        print(f"{portQueue} Open!")
                    except OSError:
                        self.logs[portQueue] = "Open"
                        print(f"{portQueue} Open!")

            finally:
                s.close()

    def threadConfig(self):
        while True:
            portNumberQueue = self.tqueue.get() #número através da fila (thread)
            self.scanPorts(portNumberQueue) #testar porta
            self.tqueue.task_done() # finalizar tarefa

    def scanner(self):
        if self.threads is not None:
            for x in range(self.threads):
                Thread(target=self.threadConfig, daemon=True).start() #gerar os numeros na fila (queue)

            if self.portRange is not None:
                for x in [x for x in range(self.portRange+1)]:
                    self.tqueue.put(x) #adicionar cada porta na fila
            else:
                for x in [x for x in range(1024+1)]:
                    self.tqueue.put(x) #adicionar cada porta na fila

        else:
            for x in range(51):
                Thread(target=self.threadConfig, daemon=True).start() #gerar os numeros na fila (queue)
        
            if self.portRange is not None:
                for x in [x for x in range(self.portRange+1)]:
                    self.tqueue.put(x) #adicionar cada porta na fila
            else:
                for x in [x for x in range(1024+1)]:
                    self.tqueue.put(x) #adicionar cada porta na fila

        self.tqueue.join() # espera que todos os threads do daemon terminem
