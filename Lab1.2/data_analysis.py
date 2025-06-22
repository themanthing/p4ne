from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx') # Загрузить таблицу Excel из файла в переменную
sheet = wb['Data'] # Загрузить лист с именем "Data" в переменную sheet
# sheet['A'][1:] # Получить содержимое колонки A в виде списка

def getvalue(x):
  return x.value
list_x = list(map(getvalue, wbsheet['A'][1:])) # Преобразовать содержимое колонки A в список, содержащий только значения (без форматирования и т. п.)
list_y1 = list(map(getvalue, wbsheet['C'][1:]))
list_y2 = list(map(getvalue, wbsheet['D'][1:]))

pyplot.plot(list_x, list_y1) # Построить график по точкам, в первом списке значения по оси X, во втором — значения по оси Y
pyplot.plot(list_x, list_y2)
pyplot.show() # показать график

