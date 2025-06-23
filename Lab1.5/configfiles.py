import glob
files = glob.glob("*.log")

ips = set()

for one_file in files:
  with open(one_file) as f:
    for l in f:
      if "ip address" in l:
        from_ = l.find("ip address")+11
        l = l.replace(" sub","")
        ips.add(l[from_:-1])

for elem in sorted(ips):
  print(elem)

