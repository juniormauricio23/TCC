import os
import subprocess
from multiprocessing import Pool
import sys

processos = ('main.py', 'mouse_controller.py')
subprocess.Popen('/home/mauricio/Skeltrack-Desktop-Control/src/skeltrack-desktop-control')

def roda_processo(processo):
    os.system('python {}'.format(processo))

pool = Pool(processes=2)
pool.map(roda_processo, processos)
