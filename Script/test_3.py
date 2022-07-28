import os
import subprocess


dir = str(input('Введи путь: '))
forward = f'cd {dir}'
subprocess.run(['bash', '-c', forward])
command = 'ls | wc -l'
output = subprocess.run(['bash', '-c', command])
