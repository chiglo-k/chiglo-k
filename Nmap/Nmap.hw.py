from nmap import nmap

nm = nmap.PortScanner()
nm.scan('192.168.1.131', '1-500', '-sT, -sU, -sP, -sV')
