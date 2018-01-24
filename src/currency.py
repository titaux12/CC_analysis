#! /Users/louismelchior/anaconda/bin/python

# The first line have to be changed. It depends of the computer.
# Currently, only work for Louis Melchior.

import pandas as pd


def isolateCurrency(dataFileName):
    output = []
    data = pd.read_csv(dataFileName)
    for currency in data["coin"].unique():
        output += [( currency , data.loc[ (data['coin'] == currency ) ] )]
    return output

def isolateCurrency(dataFileName, currency):
    data = pd.read_csv(dataFileName)
    return data.loc[ (data['coin'] == currency ) ]
