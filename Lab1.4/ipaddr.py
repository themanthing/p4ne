# семинар 5
# self - это объект текущего класса
from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
      net = random.randint(0x0B000000, 0xDF000000)  # Диапазон — между 11.0.0.0 (0x0B000000) и 223.0.0.0 (0xDF000000)
      mask = random.randint(8,24)                   # Маска — между /8 и /24
      IPv4Network.__init__(self, (net, mask), strict=False)   # (1)

    def regular(self):
      return self.is_global

    def key_value(self):
      return int(self.netmask)*2**32 + int(self.network_address) # (3)

net_list = []

while len(net_list) < 20:
  net1 = IPv4RandomNetwork()
  if net1.regular():
    net_list.append(net1)

# net_list

# def value_ip(net):
#   return int(net.netmask)*2**32 + int(net.network_address)

def value_ip(net):
  return net.key_value()

sorted_list = sorted(net_list, key=value_ip)      # возвращает новый отсортированный список. передаем функцию сортировки в качестве параметра! функци, которая м.б. предоставлена чтобы кастомизировать порядок сортировки!

for i in sorted_list:
  print(i)
