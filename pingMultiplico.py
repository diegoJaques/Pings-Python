import os
import time

with open("hosts.txt") as file:
    dump = file.read()
    dump = dump.splitlines() # colocando em linhas separadas

    for ip in dump:
        print("verificando o IP: ")
        print("-"*60)
        os.system('ping -n 2 {}'.format(ip))
        print("-" * 60)
        time.sleep(5)