import os
import subprocess

dir = str(input('\nВведите путь: '))
command = f'file {dir}'
out = subprocess.run(['bash', '-c', command])
