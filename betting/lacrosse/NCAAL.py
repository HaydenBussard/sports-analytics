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
from webdriver_auto_update import check_driver
import copy



url_offense_page1 = 'https://www.ncaa.com/stats/lacrosse-men/d1/current/team/228'
url_offense_page2 = 'https://www.ncaa.com/stats/lacrosse-men/d1/current/team/228/p2'
url_defense_page1 = 'https://www.ncaa.com/stats/lacrosse-men/d1/current/team/229'
url_defense_page2 = 'https://www.ncaa.com/stats/lacrosse-men/d1/current/team/229/p2'
stat_lst = [url_offense_page1, url_offense_page2, url_defense_page1, url_defense_page2]

team_stats_o = []
team_stats_d = []
i = 0
while True:
    if i < len(stat_lst):
        df_ncaal = pd.read_html(stat_lst[i])
        lst = df_ncaal[0].values.tolist()
        for elem in lst:
            name = str(elem[1])
            stat = float(elem[4])
            if i != 0 and i != 1:
                lst_ = [name, stat]
                team_stats_d.append(lst_)
            else:
                lst_ = [name, stat]
                team_stats_o.append(lst_)
        i += 1
        continue
    else:
        break

dict_stats_d = {x[0]:x[1:] for x in team_stats_d}
keys_stats_d = (dict_stats_d.keys())

i = 0
while True:
    if i < len(team_stats_o):
        team = team_stats_o[i][0]
        if team in keys_stats_d:
            stat = dict_stats_d[team]
            stat = stat[0]
            team_stats_o[i].append(stat)
            i += 1
            continue
        else:
            i += 1
            continue
    else:
        break

team_stats = team_stats_o

        
        

# df_ncaal = pd.read_html(url_offense_page1)
# ncaal_stats = df_ncaal[0].values.tolist()

for elem in team_stats:
    print(elem)
