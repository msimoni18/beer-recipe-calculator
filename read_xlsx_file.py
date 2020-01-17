#! /usr/bin/python python3

import pandas as pd

df = pd.read_excel('Grain.xlsx')

#print(df.columns)
#print()
#print(df['Fermentable'].to_list())


def fermentable_list():
    df = pd.read_excel('Grain.xlsx')
    ferm_list = df['Fermentable'].to_list()
    return ferm_list

print(fermentable_list())