# Семинар 5
# self - это объект текущего класса (ссылка на net1)
from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
      net = random.randint(0x0B000000, 0xDF000000)  # Диапазон — между 11.0.0.0 (0x0B000000) и 223.0.0.0 (0xDF000000)
      mask = random.randint(8,24)                   # Маска — между /8 и /24
      IPv4Network.__init__(self, (net, mask), strict=False)   # вызываем метод init у класса IPv4Network и кладем в переменную self (net1)
      # self = IPv4Network((net, mask), strict=False)         # нужно писать как выше! хотя так мне было бы понятней!
      # self.regular = self.is_global               # regular - переменная, которая выдает внутренний или внешний ip;

    def regular(self):                              # а здесь regular() - это функция, которая делает то же самое!
      return self.is_global                         # мы ей передали переменную куда записать значение (self)

    def key_value(self):
      return int(self.netmask)*2**32 + int(self.network_address)

net_list = []

while len(net_list) < 20:
  net1 = IPv4RandomNetwork()
  if net1.regular():                                # а можно вызвать net1.regular (см.класс)
    net_list.append(net1)

# net_list

# def value_ip(net):
#   return int(net.netmask)*2**32 + int(net.network_address)

# def value_ip(net):
#   return net.key_value()

sorted_list = sorted(net_list, key=IPv4RandomNetwork.key_value)
# возвращает новый отсортированный список. передаем функцию сортировки в качестве параметра!
# функции, которая м.б. предоставлена чтобы кастомизировать порядок сортировки!
# мы просто вызвали функцию класса. Внимание: здесь без скобок!

for i in sorted_list:
  print(i)
