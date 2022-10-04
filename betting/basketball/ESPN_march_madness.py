from os import pipe
from typing import Match, Text
from urllib import request
import bs4
import pandas as pd
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
from scipy.stats import poisson
import matplotlib.pyplot as plt
import math
import random
import sqlite3
from operator import itemgetter
import schedule

today = date.today()
tomorrow = today + timedelta(1)
twodays = today + timedelta(2)
threedays = today + timedelta(3)
fourdays = today + timedelta(4)
fivedays = today + timedelta(5)
today = today.strftime("%Y%m%d")
tomorrow = tomorrow.strftime("%Y%m%d")
twodays = twodays.strftime("%Y%m%d")
threedays = threedays.strftime("%Y%m%d")
fourdays = fourdays.strftime("%Y%m%d")
fivedays = fivedays.strftime("%Y%m%d")
days = [today, tomorrow, twodays, threedays, fourdays, fivedays]

espn_data = []
i = 0
while True:
    if i < len(days):
        day = days[i]
        url_espn = 'http://www.espn.com/mens-college-basketball/bpi/_/view/predictions/group/50/date/' + str(day)
        html_espn = requests.get(url_espn)
        soup_espn = bs4.BeautifulSoup(html_espn.content, features='html.parser')
        if 'No games on this date.' in str(soup_espn):
            i += 1
            continue
        else:
            df_espn = pd.read_html('http://www.espn.com/mens-college-basketball/bpi/_/view/predictions/group/50/date/' + str(day))
            espn_data += df_espn[0].values.tolist()
            i += 1
            continue
    else:
        break

for elem in espn_data:
    print(elem)





# for elem in soup_espn:
#     print(elem)





# url_today = url_numberfire_NCAAB + str(today)
# html_today = requests.get(url_today)
# soup_today = bs4.BeautifulSoup(html_today.content, features='html.parser') 
# scrapeNumberfireNCAAB_today = soup_today.findAll('div', attrs={'class':'win-probability-wrap'})

# df_espn = pd.read_html('https://www.espn.com/mens-college-basketball/bpi/_/view/predictions/group/50/date/20211212')



# espn_data = df_espn[0].values.tolist()

# print('\n')
# print('ESPN DATAFRAME:')
# print('\n')

# for elem in espn_data:
#     print(elem)