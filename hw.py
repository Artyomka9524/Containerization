# Скрипт будет формировать dataSeries в pandas с расписанием уроков на день и выводить его на экран. 

import numpy as np
import pandas as pd
# создаем словарь с расписанием уроков
lessons_list = {'1.': 'Математика', '2.': 'Литература', '3.': 'Русский язык', '4.': 'География'}
# формируем dataSeries на основе словаря 
schedule = pd.Series(data = lessons_list, index=['1.','2.','3.','4.'])
 
# вывод расписания
print(schedule.head(5))
# вывод трехмерной единичной матрицы
print(np.eye(3))