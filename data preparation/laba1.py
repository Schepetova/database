import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

disney = pd.read_csv('bd.csv', sep=',', error_bad_lines=False) # чтение csv базы данных 
pd.set_option('display.max_columns', None)
print(disney)


disn_1_7 = disney.iloc[:, 1:7] # разделение таблицы на 2 таблицы 
print(disn_1_7)


def filter(x): # фильтр на тип
    return x == 'United States'


disn_1_7_movie = disn_1_7[disn_1_7["country"].apply(filter)]

print(disn_1_7_movie)


merge_date_year = disney['director'] + ' - ' + disney['cast']# объединение стобцов 
merge_date_year = pd.DataFrame({"director and cast": merge_date_year})
disney_merge = pd.concat([disney.iloc[:, :5], merge_date_year, disney.iloc[:, 7]], axis=1)
print(disney_merge)


separate_date_year = merge_date_year["director and cast"].str.split(" - ", expand=True)# разделение столбца, нужно переименовать столбец
separate_date_year = separate_date_year.rename(columns={0: 'director', 1: 'cast'})
disney_separate = pd.concat([disney.iloc[:, :5], separate_date_year, disney.iloc[:, 7]], axis=1)
print(disney_separate)


disney_dublicate = pd.DataFrame(disney)# добавление дубликата
disney_dublicate.loc[len(disney.index)] = disney_dublicate.iloc[disney.shape[0] - 1]
print(disney_dublicate)


disney_drop = disney_dublicate.drop_duplicates()# сброс дубликата
print(disney_drop)



disney_melt = disney.melt()# melt и pivot функции
disney_pivot = disney_melt.pivot(columns='variable', values='value')
col = disney_pivot.columns
for value in col.values:
    disney_ = 1
print(disney_melt)


disney_sort = disney.sort_values(by=['title'])# сортировка
print(disney_sort)


disney_change_cell = pd.DataFrame(disney)# изменение значения в ячейке
disney_change_cell.loc[1, "Movie"] = "Muppets Haunted Mansion"
print(disney_change_cell)



def change_type_to_num(x):# изменение значения в столбце
    if x == "Movie":
        return 1
    if x == "TV Show":
        return 2



disney_change_cell['type'] = disney_change_cell['type'].apply(change_type_to_num)
print(disney_change_cell)


disney_change_cell.to_excel("disney.xlsx")# сохранение таблички в эксель
