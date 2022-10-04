from cProfile import run
from os import pipe
from typing import Match, Text
from urllib import request
import bs4
import pandas as pd
import urllib.request
import numpy as np
import json
from json import scanner
from pandas.core.indexing import convert_from_missing_indexer_tuple, convert_missing_indexer
import requests
import re
from datetime import date, timedelta
import urllib
import urllib.parse
import urllib.request
import gettext
from gettext import gettext
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import statistics
import numpy as np
from scipy import stats
import scipy
from scipy.stats import poisson
import matplotlib.pyplot as plt
import math
import random
import sqlite3
from operator import itemgetter
import schedule
from sqlalchemy import column
from sympy import continued_fraction_reduce
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_auto_update import check_driver
import copy


url_dk = 'https://sportsbook.draftkings.com/leagues/football/nfl'
html_text = urllib.request.urlopen(
    "https://sportsbook.draftkings.com/leagues/football/nfl"
)
bs_obj = BeautifulSoup(html_text)
tables = bs_obj.findAll('table', attrs={'class': 'sportsbook-table'})
dfs = []
for table in tables:
    df = pd.DataFrame(pd.read_html(str(table))[0])
    print(df)
    df.columns.values.tolist()
    col_lst = list(df.columns)
    dat_e = col_lst[0]
    df = df.rename(
        columns={dat_e: 'Team'})
    df['date'] = df.apply(lambda x: dat_e, axis=1)
    dfs.append(df)

# print(dfs)

df_dk = pd.concat(dfs)
df_dk = df_dk.reset_index(drop=True)

print(df_dk)

str_soup = str(bs_obj)
ind0 = str_soup.index('class="event-cell-link"')
str_soup = str_soup[ind0:]
game_number = str_soup.count('class="event-cell-link" href="')
games = str_soup.split('class="event-cell-link" href="')


for elem in games:
    # ind1 = elem.index('"><')  # class="event-cell">
    print(elem[:100])
    print(len(elem))
    print(type(elem))
    print('\n')


i = 0
while True:
    if i < len(games):
        if len(games[i]) == 0:
            del games[i]
            continue
        game = str(games[i])
        print(game[:100])
        print(type(game))
        print('\n')
        ind1 = game.index('"><div')
        games[i] = game[:ind1]
        i += 1
        continue
    else:
        break

for elem in games:
    print(elem)


df_dk_urls = pd.DataFrame({'links': games})

print('\n')
print(df_dk_urls)
