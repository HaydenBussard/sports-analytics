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


def game_links(team):
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

    url = 'https://www.espn.com/mlb/team/schedule/_/name/'
    url_end_1 = '/seasontype/2/half/1'
    url_end_2 = '/seasontype/2/half/2'
    url_schedule_1 = str(url + team_url + url_end_1)
    # print(url_schedule_1)
    html_schedule_1 = requests.get(url_schedule_1)
    soup_schedule_1 = bs4.BeautifulSoup(
        html_schedule_1.content, features='html.parser')
    schedule_1 = soup_schedule_1.findAll('a', attrs={'class': 'AnchorLink'})

    games_1 = []
    for elem in schedule_1:
        el = str(elem)
        # print('from game_1 list:')
        # print(el)
        if 'href="http://www.espn.com/mlb/game/_/gameId/' in el:
            games_1.append(el)

    # print(games_1)

    url_schedule_2 = str(url + team_url + url_end_2)
    # print(url_schedule_2)
    html_schedule_2 = requests.get(url_schedule_2)
    soup_schedule_2 = bs4.BeautifulSoup(
        html_schedule_2.content, features='html.parser')
    # print(soup_schedule)
    schedule_2 = soup_schedule_2.findAll('a', attrs={'class': 'AnchorLink'})
    # print('\n')
    # print(schedule_2)
    # print('\n')
    # sch_lst = [schedule_1, schedule_2]

    games_2 = []
    for elem in schedule_2:
        # print(elem.text)
        el = str(elem)
        # print('from game_2 list:')
        # print(el)
        if 'href="http://www.espn.com/mlb/game/_/gameId/' in el:
            # print(el)
            games_2.append(el)

    games = games_1 + games_2
    # for elem in games:
    #     print(elem)

    # print('GAMES:')
    links = []
    for elem in games:
        ind = elem.index('http://www.espn.com/mlb/game/_/gameId/')
        # print('the index of the link is ' + str(ind))
        lgth = len('http://www.espn.com/mlb/game/_/gameId/')
        # print('the length of "http://www.espn.com/mlb/game/_/gameId/" is ' + str(lgth))
        lgth += ind
        lnk = elem[lgth:lgth + 10]
        lnk = 'https://www.espn.com/mlb/boxscore/_/gameId/' + lnk
        # print(lnk)
        while True:
            if lnk[-1] == ' ' or lnk[-1] == '"':
                lnk = lnk[:-1]
                continue
            else:
                break
        links.append(lnk)

    for elem in links:
        url = elem
        html = requests.get(url)
        soup = bs4.BeautifulSoup(html.content, features='html.parser')
        str_soup = str(soup)
        if 'class="team-name"' not in str_soup:
            continue
        schedule = soup.findAll('span', attrs={'class': 'team-name'})
        game = []
        for elem in schedule:
            game.append(elem.text)
        # print(game)
        if game[0] == abbr:
            clss = 'boxscore-2017__wrap boxscore-2017__wrap--away'
        if game[1] == abbr:
            clss = 'boxscore-2017__wrap boxscore-2017__wrap--home'
        batting_ = soup.findAll('div', attrs={'class': clss})
        batting = []
        for elem in batting_:
            batting.append(elem.text)
        # print(batting)
        if 'No Statistics Available' in str(batting[0]):
            continue
        if 'HR:' in str(batting[0]):
            dingers += 1
            games_played += 1
        else:
            games_played += 1

    print(dingers)
    print(games_played)

    return links


game_links('Toronto')
game_links('St. Louis')
game_links('Atlanta')
