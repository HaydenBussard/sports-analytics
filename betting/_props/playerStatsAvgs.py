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

url_Hornets = 'https://www.espn.com/nba/team/stats/_/name/cha/charlotte-hornets'
df_Hornets = pd.read_html(url_Hornets)
names_Hornets = df_Hornets[0].values.tolist()
stats_Hornets = df_Hornets[1].values.tolist()
names_Hornets_1 = df_Hornets[2].values.tolist()
stats_Hornets_1 = df_Hornets[3].values.tolist()

i = 0
a = 0
while True:
    if i < len(stats_Hornets):
        if a < len(stats_Hornets[i]):
            names_Hornets[i].append(stats_Hornets[i][a])
            a += 1
            continue
        else:
            a = 0
            i += 1
            continue
    else:
        break
    
for elem in names_Hornets:
    print(elem)

print('\n')

i = 0
a = 0
while True:
    if i < len(stats_Hornets_1):
        if a < len(stats_Hornets[i]):
            names_Hornets_1[i].append(stats_Hornets_1[i][a])
            a += 1
            continue
        else:
            a = 0
            i += 1
            continue
    else:
        break
    
for elem in names_Hornets_1:
    print(elem)

i = 0
while True:
    if i < len(names_Hornets):
        names_Hornets[i] = names_Hornets[i] + names_Hornets_1[i][1:]
        i += 1
        continue
    else:
        break

print('\n')
for elem in names_Hornets:
    print(elem)