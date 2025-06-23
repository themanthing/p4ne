import ipaddress
import re
import glob

files = glob.glob("*.log")

ips = []

def ipsearch(ss):
  m = re.match("^(.* )([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})$", ss)
  if m and m[2] and m[3]:
    return ipaddress.IPv4Interface(m[2]+"/"+m[3])
  else:
    return None

for one_file in files:
  with open(one_file) as f:
    for l in f:
      if "ip address" in l:
        one_ip = ipsearch(l)
        if (one_ip):
          ips.append(one_ip.ip)

for elem in sorted(ips):
  print(elem)
