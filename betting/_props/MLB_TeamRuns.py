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
from selenium.webdriver.chrome.options import Options
from webdriver_auto_update import check_driver
import copy


def team_links(team, value):
    if team == 'CHW':
        # team_url = 'chw/chicago-white-sox'
        team_url = 'chw'
        abbr = 'CHW'
    if team == 'Cleveland':
        # team_url = 'cle/cleveland-guardians'
        team_url = 'cle'
        abbr = 'CLE'
    if team == 'Detroit':
        # team_url = 'det/detroit-tigers'
        team_url = 'det'
        abbr = 'DET'
    if team == 'Kansas City':
        # team_url = 'kc/kansas-city-royals'
        team_url = 'kc'
        abbr = 'KC'
    if team == 'Minnesota':
        # team_url = 'min/minnesota-twins'
        team_url = 'min'
        abbr = 'MIN'
    if team == 'CHC':
        # team_url = 'chc/chicago-cubs'
        team_url = 'chc'
        abbr = 'CHC'
    if team == 'Cincinnati':
        # team_url = 'cin/cincinnati-reds'
        team_url = 'cin'
        abbr = 'CIN'
    if team == 'Milwaukee':
        # team_url = 'mil/milwaukee-brewers'
        team_url = 'mil'
        abbr = 'MIL'
    if team == 'Pittsburgh':
        # team_url = 'pit/pittsburgh-pirates'
        team_url = 'pit'
        abbr = 'PIT'
    if team == 'St. Louis':
        # team_url = 'stl/st-louis-cardinals'
        team_url = 'stl'
        abbr = 'STL'
    if team == 'Baltimore':
        # team_url = 'bal/baltimore-orioles'
        team_url = 'bal'
        abbr = 'BAL'
    if team == 'Boston':
        # team_url = 'bos/boston-red-sox'
        team_url = 'bos'
        abbr = 'BOS'
    if team == 'NYY':
        # team_url = 'nyy/new-york-yankees'
        team_url = 'nyy'
        abbr = 'NYY'
    if team == 'Tampa Bay':
        # team_url = 'tb/tampa-bay-rays'
        team_url = 'tb'
        abbr = 'TB'
    if team == 'Toronto':
        # team_url = 'tor/toronto-blue-jays'
        team_url = 'tor'
        abbr = 'TOR'
    if team == 'Atlanta':
        # team_url = 'atl/atlanta-braves'
        team_url = 'atl'
        abbr = 'ATL'
    if team == 'Miami':
        # team_url = 'mia/miami-marlins'
        team_url = 'mia'
        abbr = 'MIA'
    if team == 'NYM':
        # team_url = 'nym/new-york-mets'
        team_url = 'nym'
        abbr = 'NYM'
    if team == 'Philly':
        # team_url = 'phi/philadelphia-phillies'
        team_url = 'phi'
        abbr = 'PHI'
    if team == 'Washington':
        # team_url = 'wsh/washington-nationals'
        team_url = 'wsh'
        abbr = 'WSH'
    if team == 'Houston':
        # team_url = 'hou/houston-astros'
        team_url = 'hou'
        abbr = 'HOU'
    if team == 'LAA':
        # team_url = 'laa/los-angeles-angels'
        team_url = 'laa'
        abbr = 'LAA'
    if team == 'Oakland':
        # team_url = 'oak/oakland-athletics'
        team_url = 'oak'
        abbr = 'OAK'
    if team == 'Seattle':
        # team_url = 'sea/seattle-mariners'
        team_url = 'sea'
        abbr = 'SEA'
    if team == 'Texas':
        # team_url = 'tex/texas-rangers'
        team_url = 'tex'
        abbr = 'TEX'
    if team == 'Arizona':
        # team_url = 'ari/arizona-diamondbacks'
        team_url = 'ari'
        abbr = 'ARI'
    if team == 'Colorado':
        # team_url = 'col/colorado-rockies'
        team_url = 'col'
        abbr = 'COL'
    if team == 'LAD':
        # team_url = 'lad/los-angeles-dodgers'
        team_url = 'lad'
        abbr = 'LAD'
    if team == 'San Diego':
        # team_url = 'sd/san-diego-padres'
        team_url = 'sd'
        abbr = 'SD'
    if team == 'San Francisco':
        # team_url = 'sf/san-francisco-giants'
        team_url = 'sf'
        abbr = 'SF'

    dingers = 0
    games_played = 0

    team_schedule = []

    filter_list = ['W0', 'W1', 'W2', 'W3', 'W4', 'W5', 'W6', 'W7', 'W8',
                   'W9', 'L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9']

    url = 'https://www.espn.com/mlb/team/schedule/_/name/'
    url_end_1 = '/seasontype/2/half/1'
    url_end_2 = '/seasontype/2/half/2'
    url_schedule_1 = str(url + team_url + url_end_1)
    # print(url_schedule_1)
    html_schedule_1 = requests.get(url_schedule_1)
    soup_schedule_1 = bs4.BeautifulSoup(
        html_schedule_1.content, features='html.parser')
    schedule_1 = soup_schedule_1.findAll('td', attrs={'class': 'Table__TD'})

    for elem in schedule_1:
        txt = elem.text
        txt_f2 = txt[:2]
        if txt_f2 in filter_list or txt_f2 in filter_list:
            team_schedule.append(txt)
            # print(elem.text)

    games_1 = []
    for elem in schedule_1:
        el = str(elem)
        # print(el)
        if 'href="http://www.espn.com/mlb/game/_/gameId/' in el:
            games_1.append(el)

    # print(games_1)

    url_schedule_2 = str(url + team_url + url_end_2)
    html_schedule_2 = requests.get(url_schedule_2)
    soup_schedule_2 = bs4.BeautifulSoup(
        html_schedule_2.content, features='html.parser')
    # print(soup_schedule)
    schedule_2 = soup_schedule_2.findAll('td', attrs={'class': 'Table__TD'})

    for elem in schedule_2:
        txt = elem.text
        txt_f2 = txt[:2]
        if txt_f2 in filter_list or txt_f2 in filter_list:
            team_schedule.append(txt)
            # print(elem.text)

    i = 0
    while True:
        if i < len(team_schedule):
            if team_schedule[i][0] == 'W':
                game = team_schedule[i]
                ind = game.index('-')
                score = game[1:ind]
                score = int(score)
                team_schedule[i] = score
                i += 1
                continue
            if team_schedule[i][0] == 'L':
                game = team_schedule[i]
                ind_start = game.index('-') + 1
                if 'F' in game:
                    ind_end = game.index('F') - 1
                    score = game[ind_start:ind_end]
                    score = int(score)
                    team_schedule[i] = score
                    i += 1
                    continue
                else:
                    score = game[ind_start:]
                    score = int(score)
                    team_schedule[i] = score
                    i += 1
                    continue
        else:
            break

    # print(team_schedule)

    i = 0
    count = 0
    while True:
        if i < len(team_schedule):
            if float(team_schedule[i]) > float(value):
                count += 1
                i += 1
                continue
            else:
                i += 1
                continue
        else:
            break
    game_count = int(len(team_schedule))
    print(str(team) + "'s count for >" + str(value) +
          ' runs = ' + str(count) + '/' + str(game_count))
    # sch_lst = [schedule_1, schedule_2]

    games_2 = []
    for sch in schedule_2:
        for elem in sch:
            el = str(elem)
            # print(el)
            if 'href="http://www.espn.com/mlb/game/_/gameId/' in el:
                games_2.append(el)

    games = games_1 + games_2

    # for elem in games:
    #     print(elem)
    return


print('\n')
team_links('NYM', 2.5)
team_links('San Francisco', 2.5)
team_links('LAD', 2.5)
print('\n')
