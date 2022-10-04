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

# url_pll = 'https://stats.premierlacrosseleague.com/teams'
url_pll = 'https://stats.premierlacrosseleague.com/pll-team-table'
pll_browser = webdriver.Chrome()
pll_browser.get(url_pll)
time.sleep(20)
# pll = pll_browser.find_elements(By.CLASS_NAME, 'MuiTableContainer-root') # this works for whole table
pll_ = pll_browser.find_elements(By.CLASS_NAME, 'MuiTableRow-root') # this works to separate each row


# for elem in pll_:
#     print(elem.text)
#     print('\n')

league_pts_for = []
league_pts_against = []
headers = []
pll = []
i = 0
while True:
    if i < len(pll_):
        if i == 0:
            hd = pll_[i].text
            hd = hd.split()
            name = str(hd[0])
            pts_for_avg = 'Points-For-Avg'
            pts_against_avg = 'Points-Against-Avg'
            headers.append(name)
            headers.append(pts_for_avg)
            headers.append(pts_against_avg)
            i += 1
            continue
        if i > 0:
            rw = pll_[i].text
            rw = rw.split()
            name = str(rw[0])
            gp = int(int(rw[1]) + int(rw[2]))
            pts_for = int(rw[3])
            pts_against = int(rw[18])
            pts_for_avg = round(pts_for / gp, 2)
            pts_against_avg = round(pts_against / gp, 2)
            league_pts_for.append(pts_for_avg)
            league_pts_against.append(pts_against_avg)
            lst = [name, pts_for_avg, pts_against_avg]
            pll.append(lst)
            i += 1
            continue
        else:
            i += 1
            continue
    else:
        break

league_for_avg = round(statistics.mean(league_pts_for), 2)
print(league_for_avg)
league_against_avg = round(statistics.mean(league_pts_against), 2)
print(league_against_avg)
for elem in pll:
    print(elem)
        