from doctest import DocFileCase
from locale import D_FMT
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


def mlb():
    url_parkFactor = 'https://baseballsavant.mlb.com/leaderboard/statcast-park-factors?type=year&year=2021&batSide=&stat=index_wOBA&condition=All&rolling=&sort=6&sortDir=desc'
    url_pitching = 'https://www.mlb.com/stats/team/pitching?sortState=asc'
    url_rpg = 'https://www.teamrankings.com/mlb/stat/runs-per-game'
    url_o_rpg = 'https://www.teamrankings.com/mlb/stat/opponent-runs-per-game'
    url_o_fir = 'https://www.teamrankings.com/mlb/stat/opponent-1st-inning-scored-percentage'
    url_fir = 'https://www.teamrankings.com/mlb/stat/1st-inning-scored-percentage'
    url_soa = 'https://www.teamrankings.com/mlb/stat/strikeouts-per-game'
    url_pitchers = 'https://www.cbssports.com/fantasy/baseball/probable-pitchers/'  # + date
    url_matchups = 'https://www.espn.com/mlb/scoreboard/_/date/'  # + date
    url_bullpen_ERAs = 'https://www.espn.com/mlb/stats/team/_/view/pitching/table/pitching'
    url_innings_avg = 'https://www.espn.com/mlb/team/stats/_/type/pitching/name/'
    url_nf = 'https://www.numberfire.com/mlb/games/'
    url_relievers = 'https://www.mlb.com/stats/team/pitching?split=rp&sortState=asc'
    url_dk = 'https://sportsbook.draftkings.com/leagues/baseball/mlb'

    today = date.today()
    tomorrow = today + timedelta(1)
    day_lst = ['Today', 'Tomorrow']
    days = 8  # ADJUST DAYS INCLUDED IN ABBREVIATED SHEET HERE
    i = 1
    while True:
        if i < days:
            day = today + timedelta(i)
            day_lst.append(str(day))
            i += 1
            continue
        else:
            break

    def date_dig_to_words(lst):
        if len(lst) == 1:
            days = []
            th = ['10', '11', '12', '13', '14', '15', '16', '17', '18',
                  '19', '20', '24', '25', '26', '27', '28', '29', '30']
            st = ['21', '31']
            i = 0
            while True:
                if i < len(lst):
                    if str(lst[i]) == 'Today':
                        game_day = 'Today'
                        days.append(game_day)
                        i += 1
                        continue
                    elif str(lst[i]) == 'Tomorrow':
                        game_day = 'Tomorrow'
                        days.append(game_day)
                        i += 1
                        continue
                    elif str(lst[i]) == str(today):
                        if 'Today' in days:
                            i += 1
                            continue
                        game_day = 'Today'
                        days.append(game_day)
                        i += 1
                        continue
                    elif str(lst[i]) == str(tomorrow):
                        if 'Tomorrow' in days:
                            i += 1
                            continue
                        game_day = 'Tomorrow'
                        days.append(game_day)
                        i += 1
                        continue
                    elif str(lst[i][:4]) == '2022':
                        if '-' in lst[i]:
                            l = lst[i].split('-')
                            m = l[1]
                            d = l[2]
                        print('THIS IS WHAT WONT SPLIT -')
                        print(lst[i])
                        # l = lst[i].split('-')
                        # m = l[1]
                        # d = l[2]
                        if '-' not in lst[i]:
                            m = str(lst[i][4:6])
                            d = str(lst[i][6:])
                        # m = str(lst[i][4:6])
                        # d = str(lst[i][6:])
                        if m == '08':
                            m = 'AUG'
                        if m == '09':
                            m = 'SEP'
                        if m == '10':
                            m = 'OCT'
                        if m == '11':
                            m = 'NOV'
                        if m == '12':
                            m = 'DEC'
                        if m == '01':
                            m = 'JAN'
                        if d == '01':
                            d = '1ST'
                        if d == '02':
                            d = '2ND'
                        if d == '03':
                            d = '3RD'
                        if d == '04':
                            d = '4TH'
                        if d == '05':
                            d = '5TH'
                        if d == '06':
                            d = '6TH'
                        if d == '07':
                            d = '7TH'
                        if d == '08':
                            d = '8TH'
                        if d == '09':
                            d = '9TH'
                        if d == '22':
                            d = '22ND'
                        if d == '23':
                            d = '23RD'
                        if d in th:
                            d = str(d) + 'TH'
                        if d in st:
                            d = str(d) + 'ST'
                        game_day = str(m) + ' ' + str(d)
                        days.append(game_day)
                        i += 1
                        continue
                    else:
                        day = str(lst[i])
                        day_strip = day.replace('-', '')
                        print('Day Strip = ' + str(day_strip))
                        print(day)
                        gd = day.split('-')
                        print(gd)
                        day = gd[2]
                        print('day = ')
                        print(gd[2])
                        print('month = ')
                        m = gd[1]
                        if m == '08':
                            m = 'AUG'
                        if m == '09':
                            m = 'SEP'
                        if m == '10':
                            m = 'OCT'
                        if m == '11':
                            m = 'NOV'
                        if m == '12':
                            m = 'DEC'
                        if m == '01':
                            m = 'JAN'
                        if day == '01':
                            day = '1ST'
                        if day == '02':
                            day = '2ND'
                        if day == '03':
                            day = '3RD'
                        if day == '04':
                            day = '4TH'
                        if day == '05':
                            day = '5TH'
                        if day == '06':
                            day = '6TH'
                        if day == '07':
                            day = '7TH'
                        if day == '08':
                            day = '8TH'
                        if day == '09':
                            day = '9TH'
                        if day == '22':
                            day = '22ND'
                        if day == '23':
                            day = '23RD'
                        if day in th:
                            day = str(day) + 'TH'
                        if day in st:
                            day = str(day) + 'ST'
                        game_day = str(m) + ' ' + str(day)
                        days.append(game_day)
                        i += 1
                        continue
                else:
                    break
            return days
        days = ['Today', 'Tomorrow']
        th = ['10', '11', '12', '13', '14', '15', '16', '17', '18',
              '19', '20', '24', '25', '26', '27', '28', '29', '30']
        st = ['21', '31']
        i = 0
        while True:
            if i < len(lst):
                if str(lst[i]) == 'Today' or str(lst[i]) == 'Tomorrow':
                    i += 1
                    continue
                elif str(lst[i]) == str(today):
                    if 'Today' in days:
                        i += 1
                        continue
                    game_day = 'Today'
                    days.append(game_day)
                    i += 1
                    continue
                elif str(lst[i]) == str(tomorrow):
                    if 'Tomorrow' in days:
                        i += 1
                        continue
                    game_day = 'Tomorrow'
                    days.append(game_day)
                    i += 1
                    continue
                elif str(lst[i][:4]) == '2022':
                    if '-' in lst[i]:
                        l = lst[i].split('-')
                        m = l[1]
                        d = l[2]
                    print('THIS IS WHAT WONT SPLIT -')
                    print(lst[i])
                    # l = lst[i].split('-')
                    # m = l[1]
                    # d = l[2]
                    if '-' not in lst[i]:
                        m = str(lst[i][4:6])
                        d = str(lst[i][6:])
                    # m = str(lst[i][4:6])
                    # d = str(lst[i][6:])
                    if m == '08':
                        m = 'AUG'
                    if m == '09':
                        m = 'SEP'
                    if m == '10':
                        m = 'OCT'
                    if m == '11':
                        m = 'NOV'
                    if m == '12':
                        m = 'DEC'
                    if m == '01':
                        m = 'JAN'
                    if d == '01':
                        d = '1ST'
                    if d == '02':
                        d = '2ND'
                    if d == '03':
                        d = '3RD'
                    if d == '04':
                        d = '4TH'
                    if d == '05':
                        d = '5TH'
                    if d == '06':
                        d = '6TH'
                    if d == '07':
                        d = '7TH'
                    if d == '08':
                        d = '8TH'
                    if d == '09':
                        d = '9TH'
                    if d == '22':
                        d = '22ND'
                    if d == '23':
                        d = '23RD'
                    if d in th:
                        d = str(d) + 'TH'
                    if d in st:
                        d = str(d) + 'ST'
                    game_day = str(m) + ' ' + str(d)
                    days.append(game_day)
                    i += 1
                    continue
                else:
                    day = str(lst[i])
                    day_strip = day.replace('-', '')
                    print('Day Strip = ' + str(day_strip))
                    print(day)
                    gd = day.split('-')
                    print(gd)
                    day = gd[2]
                    print('day = ')
                    print(gd[2])
                    print('month = ')
                    m = gd[1]
                    if m == '08':
                        m = 'AUG'
                    if m == '09':
                        m = 'SEP'
                    if m == '10':
                        m = 'OCT'
                    if m == '11':
                        m = 'NOV'
                    if m == '12':
                        m = 'DEC'
                    if m == '01':
                        m = 'JAN'
                    if day == '01':
                        day = '1ST'
                    if day == '02':
                        day = '2ND'
                    if day == '03':
                        day = '3RD'
                    if day == '04':
                        day = '4TH'
                    if day == '05':
                        day = '5TH'
                    if day == '06':
                        day = '6TH'
                    if day == '07':
                        day = '7TH'
                    if day == '08':
                        day = '8TH'
                    if day == '09':
                        day = '9TH'
                    if day == '22':
                        day = '22ND'
                    if day == '23':
                        day = '23RD'
                    if day in th:
                        day = str(day) + 'TH'
                    if day in st:
                        day = str(day) + 'ST'
                    game_day = str(m) + ' ' + str(day)
                    days.append(game_day)
                    i += 1
                    continue
            else:
                break
        return days
    print('Day search list for making abbreviated list of bets:')

    print(day_lst)

    day_lst = date_dig_to_words(day_lst)

    print(day_lst)

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
    # days = [today, tomorrow, twodays, threedays, fourdays, fivedays]
    days = [today, tomorrow, twodays]  # , threedays, fourdays, fivedays]

    def team_rename(teamName):
        if teamName == 'Houston' or teamName == 'HOU' or teamName == 'Houston Astros' or teamName == 'null(Houston, Texas)' or teamName == 'Astros Minute Maid Park' or teamName == 'HOUAstros' or 'HOU Astros' in teamName or teamName == 'Astros' or 'Astros' in teamName:
            teamName = 'HOU Astros'
            return teamName
        if teamName == 'Tampa Bay' or teamName == 'TB' or teamName == 'Tampa Bay Rays' or teamName == 'null(St. Petersburg, Florida)' or teamName == 'Rays Tropicana Field' or teamName == 'TBRays' or 'TB Rays' in teamName or teamName == 'Rays' or 'Rays' in teamName:
            teamName = 'TB Rays'
            return teamName
        if teamName == 'Toronto' or teamName == 'TOR' or teamName == 'Toronto Blue Jays' or teamName == 'Rogers Centre(Toronto, Ontario)' or teamName == 'Blue Jays Rogers Centre' or teamName == 'TORBlue Jays' or 'TOR Blue Jays' in teamName or teamName == 'Blue Jays' or 'Blue Jays' in teamName:
            teamName = 'TOR Blue Jays'
            return teamName
        if teamName == 'Boston' or teamName == 'BOS' or teamName == 'Boston Red Sox' or teamName == 'null(Boston, Massachusetts)' or teamName == 'Red Sox Fenway Park' or teamName == 'BOSRed Sox' or 'BOS Red Sox' in teamName or teamName == 'Red Sox' or 'Red Sox' in teamName:
            teamName = 'BOS Red Sox'
            return teamName
        if teamName == 'LA Dodgers' or teamName == 'LAD' or teamName == 'Los Angeles Dodgers' or teamName == 'null(Los Angeles, California)' or teamName == 'Dodgers Dodger Stadium' or teamName == 'LADDodgers' or 'LA Dodgers' in teamName or teamName == 'Dodgers' or 'Dodgers' in teamName:
            teamName = 'LA Dodgers'
            return teamName
        if teamName == 'Chi Sox' or teamName == 'Chicago White Sox' or teamName == 'CHW' or teamName == 'White Sox Guaranteed Rate Field' or teamName == 'White Sox Guaranteed Rate Field' or teamName == 'CHWWhite Sox' or 'CHI White Sox' in teamName or teamName == 'White Sox' or 'White Sox' in teamName:
            teamName = 'CHI White Sox'
            return teamName
        # SF Giants
        if teamName == 'SF Giants' or teamName == 'SF' or teamName == 'San Francisco Giants' or teamName == 'null(San Francisco, California)' or teamName == 'Giants Oracle Park' or teamName == 'SFGiants' or 'SF Giants' in teamName or teamName == 'Giants' or 'Giants' in teamName:
            teamName = 'SF Giants'
            return teamName
        if teamName == 'Cincinnati' or teamName == 'CIN' or teamName == 'Cincinnati Reds' or teamName == 'null(Cincinnati, Ohio)' or teamName == 'Reds Great American Ball Park' or teamName == 'CINReds' or 'CIN Reds' in teamName or teamName == 'Reds' or 'Reds' in teamName:
            teamName = 'CIN Reds'
            return teamName
        if teamName == 'Atlanta' or teamName == 'ATL' or teamName == 'Atlanta Braves' or teamName == 'null(Atlanta, Georgia)' or teamName == 'Braves Truist Park' or teamName == 'ATLBraves' or 'ATL Braves' in teamName or teamName == 'Braves' or 'Braves' in teamName:
            teamName = 'ATL Braves'
            return teamName
        if teamName == 'Colorado' or teamName == 'COL' or teamName == 'Colorado Rockies' or teamName == 'null(Denver, Colorado)' or teamName == 'Rockies Coors Field' or teamName == 'COLRockies' or 'COL Rockies' in teamName or teamName == 'Rockies' or 'Rockies' in teamName:
            teamName = 'COL Rockies'
            return teamName
        if teamName == 'Oakland' or teamName == 'OAK' or teamName == 'Oakland Athletics' or teamName == 'null(Oakland, California)' or teamName == 'Athletics Oakland Coliseum' or teamName == 'OAKAthletics' or 'OAK Athletics' in teamName or teamName == 'Athletics' or 'Athletics' in teamName:
            teamName = 'OAK Athletics'
            return teamName
        if teamName == 'Philadelphia' or teamName == 'PHI' or teamName == 'Philadelphia Phillies' or teamName == 'null(Philadelphia, Pennsylvania)' or teamName == 'Phillies Citizens Bank Park' or teamName == 'PHIPhillies' or 'PHI Phillies' in teamName or teamName == 'Phillies' or 'Phillies' in teamName:
            teamName = 'PHI Phillies'
            return teamName
        if teamName == 'San Diego' or teamName == 'SD' or teamName == 'San Diego Padres' or teamName == 'null(San Diego, California)' or teamName == 'Padres Petco Park' or teamName == 'SDPadres' or 'SD Padres' in teamName or teamName == 'Padres' or 'Padres' in teamName:
            teamName = 'SD Padres'
            return teamName
        if teamName == 'Minnesota' or teamName == 'MIN' or teamName == 'Minnesota Twins' or teamName == 'null(Minneapolis, Minnesota)' or teamName == 'Twins Target Field' or teamName == 'MINTwins' or 'MIN Twins' in teamName or teamName == 'Twins' or 'Twins' in teamName:
            teamName = 'MIN Twins'
            return teamName
        if teamName == 'Milwaukee' or teamName == 'MIL' or teamName == 'Milwaukee Brewers' or teamName == 'Miller Park(Milwaukee, Wisconsin)' or teamName == 'Brewers American Family Field' or teamName == 'MILBrewers' or 'MIL Brewers' in teamName or teamName == 'Brewers' or 'Brewers' in teamName:
            teamName = 'MIL Brewers'
            return teamName
        if teamName == 'Washington' or teamName == 'WSH' or teamName == 'WAS' or teamName == 'Washington Nationals' or teamName == 'null(Washington, District of Columbia)' or teamName == 'Nationals Nationals Park' or teamName == 'WSHNationals' or 'WAS Nationals' in teamName or teamName == 'Nationals' or 'Nationals' in teamName:
            teamName = 'WAS Nationals'
            return teamName
        if teamName == 'LA Angels' or teamName == 'LAA' or teamName == 'Los Angeles Angels' or teamName == 'null(Anaheim, California)' or teamName == 'Angels Angel Stadium' or teamName == 'LAAAngels' or 'LA Angels' in teamName or teamName == 'Angels' or 'Angels' in teamName:
            teamName = 'LA Angels'
            return teamName
        if teamName == 'Cleveland' or teamName == 'CLE' or teamName == 'Cleveland Guardians' or teamName == 'Cleveland Indians' or teamName == 'null(Cleveland, Ohio)' or teamName == 'Indians Progressive Field' or teamName == 'Guardians Progressive Field' or teamName == 'CLEGuardians' or 'CLE Guardians' in teamName or teamName == 'Guardians' or teamName == 'Indians' or 'Guardians' in teamName:
            teamName = 'CLE Guardians'
            return teamName
        if teamName == 'NY Yankees' or teamName == 'NYY' or teamName == 'New York Yankees' or teamName == 'null(Bronx, New York)' or teamName == 'Yankees Yankee Stadium' or teamName == 'NYYYankees' or 'NY Yankees' in teamName or teamName == 'Yankees' or 'Yankees' in teamName:
            teamName = 'NY Yankees'
            return teamName
        if teamName == 'Chi Cubs' or teamName == 'Chicago Cubs' or teamName == 'CHC' or teamName == 'Cubs Wrigley Field' or teamName == 'CHCCubs' or 'CHI Cubs' in teamName or teamName == 'Cubs' or 'Cubs' in teamName:
            teamName = 'CHI Cubs'
            return teamName
        if teamName == 'St. Louis' or teamName == 'STL' or teamName == 'St. Louis Cardinals' or teamName == 'null(St. Louis, Missouri)' or teamName == 'Cardinals Busch Stadium' or teamName == 'STLCardinals' or 'STL Cardinals' in teamName or teamName == 'Cardinals' or 'Cardinals' in teamName:
            teamName = 'STL Cardinals'
            return teamName
        if teamName == 'Detroit' or teamName == 'DET' or teamName == 'Detroit Tigers' or teamName == 'null(Detroit, Michigan)' or teamName == 'Tigers Comerica Park' or teamName == 'DETTigers' or 'DET Tigers' in teamName or teamName == 'Tigers' or 'Tigers' in teamName:
            teamName = 'DET Tigers'
            return teamName
        if teamName == 'Seattle' or teamName == 'SEA' or teamName == 'Seattle Mariners' or teamName == 'null(Seattle, Washington)' or teamName == 'Mariners T-Mobile Park' or teamName == 'SEAMariners' or 'SEA Mariners' in teamName or teamName == 'Mariners' or 'Mariners' in teamName:
            teamName = 'SEA Mariners'
            return teamName
        if teamName == 'Kansas City' or teamName == 'KC' or teamName == 'Kansas City Royals' or teamName == 'null(Kansas City, Missouri)' or teamName == 'Royals Kauffman Stadium' or teamName == 'KCRoyals' or 'KC Royals' in teamName or teamName == 'Royals' or 'Royals' in teamName:
            teamName = 'KC Royals'
            return teamName
        if teamName == 'Arizona' or teamName == 'ARI' or teamName == 'Arizona Diamondbacks' or teamName == 'null(Phoenix, Arizona)' or teamName == 'D-backs Chase Field' or teamName == 'ARIDiamondbacks' or 'ARI Diamondbacks' in teamName or teamName == 'Diamondbacks' or 'Diamondbacks' in teamName:
            teamName = 'ARI Diamondbacks'
            return teamName
        if teamName == 'Baltimore' or teamName == 'BAL' or teamName == 'Baltimore Orioles' or teamName == 'null(Baltimore, Maryland)' or teamName == 'Orioles Oriole Park at Camden Yards' or teamName == 'BALOrioles' or 'BAL Orioles' in teamName or teamName == 'Orioles' or 'Orioles' in teamName:
            teamName = 'BAL Orioles'
            return teamName
        if teamName == 'NY Mets' or teamName == 'NYM' or teamName == 'New York Mets' or teamName == 'null(Queens, New York)' or teamName == 'Mets Citi Field' or teamName == 'NYMMets' or 'NY Mets' in teamName or teamName == 'Mets' or 'Mets' in teamName:
            teamName = 'NY Mets'
            return teamName
        if teamName == 'Texas' or teamName == 'TEX' or teamName == 'Texas Rangers' or teamName == 'null(Arlington, Texas)' or teamName == 'TEXRangers' or 'TEX Rangers' in teamName or teamName == 'Rangers' or 'Rangers' in teamName:
            teamName = 'TEX Rangers'
            return teamName
        if teamName == 'Miami' or teamName == 'MIA' or teamName == 'Miami Marlins' or teamName == 'Marlins Park(Miami, Florida)' or teamName == 'Marlins loanDepot park' or teamName == 'MIAMarlins' or 'MIA Marlins' in teamName or teamName == 'Marlins' or 'Marlins' in teamName:
            teamName = 'MIA Marlins'
            return teamName
        if teamName == 'Pittsburgh' or teamName == 'PIT' or teamName == 'Pittsburgh Pirates' or teamName == 'null(Pittsburgh, Pennsylvania)' or teamName == 'Pirates PNC Park' or teamName == 'PITPirates' or 'PIT Pirates' in teamName or teamName == 'Pirates' or 'Pirates' in teamName:
            teamName = 'PIT Pirates'
            return teamName
        else:
            return teamName

    def espn(teamName, player):
        if teamName == 'HOU Astros':
            teamName = 'hou'
        if teamName == 'TB Rays':
            teamName = 'tb'
        if teamName == 'TOR Blue Jays':
            teamName = 'tor'
        if teamName == 'BOS Red Sox':
            teamName = 'bos'
        if teamName == 'LA Dodgers':
            teamName = 'lad'
        if teamName == 'CHI White Sox':
            teamName = 'chw'
        if teamName == 'SF Giants':
            teamName = 'sf'
        if teamName == 'CIN Reds':
            teamName = 'cin'
        if teamName == 'ATL Braves':
            teamName = 'atl'
        if teamName == 'COL Rockies':
            teamName = 'col'
        if teamName == 'OAK Athletics':
            teamName = 'oak'
        if teamName == 'PHI Phillies':
            teamName = 'phi'
        if teamName == 'SD Padres':
            teamName = 'sd'
        if teamName == 'MIN Twins':
            teamName = 'min'
        if teamName == 'MIL Brewers':
            teamName = 'mil'
        if teamName == 'WAS Nationals':
            teamName = 'wsh'
        if teamName == 'LA Angels':
            teamName = 'laa'
        if teamName == 'CLE Guardians':
            teamName = 'cle'
        if teamName == 'NY Yankees':
            teamName = 'nyy'
        if teamName == 'CHI Cubs':
            teamName = 'chc'
        if teamName == 'STL Cardinals':
            teamName = 'stl'
        if teamName == 'DET Tigers':
            teamName = 'det'
        if teamName == 'SEA Mariners':
            teamName = 'sea'
        if teamName == 'KC Royals':
            teamName = 'kc'
        if teamName == 'ARI Diamondbacks':
            teamName = 'ari'
        if teamName == 'BAL Orioles':
            teamName = 'bal'
        if teamName == 'NY Mets':
            teamName = 'nym'
        if teamName == 'TEX Rangers':
            teamName = 'tex'
        if teamName == 'MIA Marlins':
            teamName = 'mia'
        if teamName == 'PIT Pirates':
            teamName = 'pit'
        print(str(url_innings_avg) + str(teamName))
        df_innings = pd.read_html(url_innings_avg + teamName)
        innings_name = df_innings[0].values.tolist()
        innings_stats = df_innings[1].values.tolist()
        pitchers = []
        i = 0
        while True:
            if i < len(innings_name):
                lgth = len(str(innings_name[i][0])) - 3
                name = str(innings_name[i][0])
                name = name[:lgth]
                name = [name]
                stat = innings_stats[i]
                # print(stat)
                y = 0
                while True:
                    if y < len(stat):
                        if stat[y] == '---' or stat[y] == '--' or stat[y] == '-':
                            y += 1
                            continue
                        # print(stat[y])
                        stat[y] = float(stat[y])
                        y += 1
                        continue
                    else:
                        break
                lst = name + stat
                pitchers.append(lst)
                i += 1
                continue
            else:
                break
        i = 0
        while True:
            if i < len(pitchers):
                gp = pitchers[i][1]
                inn = pitchers[i][8]
                ipg = round(inn / gp, 3)
                pitchers[i].append(ipg)
                i += 1
                continue
            else:
                break
        dict_pitchers = {x[0]: x[1:] for x in pitchers}
        keys_pitchers = (dict_pitchers.keys())
        if player in keys_pitchers:
            player_stats = dict_pitchers[player]
            del player_stats[3:5]
            del player_stats[5]
            del player_stats[8:10]
            # should give 'games_played', 'starts', 'qual_starts', 'saves', 'holds', 'hits', 'earned_runs', 'homers', 'ks_per_9', 'pitches_per_start', 'WAR', 'ipg'
            del player_stats[11:13]
            return player_stats
        else:
            lst = ['use bullpen avg', '-', '-', '-',
                   '-', '-', '-', '-', '-', '-', '-', '-']
            return lst

    def get_index_positions(list_of_elems, element):
        ''' Returns the indexes of all occurrences of give element in
        the list- listOfElements '''
        index_pos_list = []
        index_pos = 0
        while True:
            try:
                # Search for item in list from indexPos to the end of list
                index_pos = list_of_elems.index(element, index_pos)
                # Add the index position in list
                index_pos_list.append(index_pos)
                index_pos += 1
            except ValueError as e:
                break
        return index_pos_list

    # CREATING PARK FACTOR LIST

    pf_browser = webdriver.Chrome()
    pf_browser.get(url_parkFactor)
    time.sleep(20)
    pf = pf_browser.find_elements(By.CLASS_NAME, 'default-table-row  ')

    pf_mlb = []
    for elem in pf:
        txt = elem.text
        txt = txt.split('\n')
        lng = len(txt)
        end = lng - 1
        a = 0
        while True:
            if a < lng:
                pf_mlb.append(txt[a])
                a += 1
                continue
            else:
                break

    pf = []
    pf_val = 0
    wOBACon = 0
    bacon = 0
    r = 0
    obp = 0
    h = 0
    one_b = 0
    two_b = 0
    three_b = 0
    hr = 0
    bb = 0
    so = 0
    pa = 0
    for elem in pf_mlb:
        ind0 = elem.index('-202')
        ind1 = ind0 - 5
        name = elem[:ind1]
        spaces = name.count(' ')
        inds = name.index(' ') + 1
        name = team_rename(name[inds:])
        name = [name]
        # print('.' + name + '.')
        # print(spaces)
        # print(elem)
        stat = elem[ind0 + 6:]
        stat = stat.split(' ')
        i = 0
        while True:
            if i < len(stat):
                stat[i] = stat[i].replace(',', '')
                stat[i] = float(stat[i])
                i += 1
                continue
            else:
                break
        lst = name + stat
        pf_val = pf_val + lst[1]
        wOBACon = wOBACon + lst[2]
        bacon = bacon + lst[3]
        r = r + lst[4]
        obp = obp + lst[5]
        h = h + lst[6]
        one_b = one_b + lst[7]
        two_b = two_b + lst[8]
        three_b = three_b + lst[9]
        hr = hr + lst[10]
        bb = bb + lst[11]
        so = so + lst[12]
        pa = pa + lst[13]
        pf.append(lst)

    pf_browser.quit()

    # TEX RANGERS NOT IN PF LIST ON WEBSITE. HAVE TO MANUALLY CALCULATE BASED ON SITE AVERAGES

    print('r = ' + str(round(r / 29, 4)))
    print('TEX Rangers PF = ' + str(round((100 * 30) - r, 4)))
    pf_val = round((100 * 30) - pf_val, 4)
    wOBACon = round((100 * 30) - wOBACon, 4)
    bacon = round((100 * 30) - bacon, 4)
    r = round((100 * 30) - r, 4)
    obp = round((100 * 30) - obp, 4)
    h = round((100 * 30) - h, 4)
    one_b = round((100 * 30) - one_b, 4)
    two_b = round((100 * 30) - two_b, 4)
    three_b = round((100 * 30) - three_b, 4)
    hr = round((100 * 30) - hr, 4)
    bb = round((100 * 30) - bb, 4)
    so = round((100 * 30) - so, 4)
    pa = round((15000 * 30) - pf_val, 4)
    lst = ['TEX Rangers', pf_val, wOBACon, bacon, r,
           obp, h, one_b, two_b, three_b, hr, bb, so, pa]
    pf.append(lst)
    print('\n')
    print('PARK FACTORS')
    for elem in pf:
        print(elem)
    print('\n')
    pf_cols = ['Team', 'pf', 'wOBACon', 'bacon', 'run_factor',
               'OBP', 'H', '1B', '2B', '3B', 'HR', 'BB', 'SO', 'PA']
    df_pf = pd.DataFrame(pf, columns=pf_cols)
    print(df_pf)

    # url_rpg
    df_rpg = pd.DataFrame(pd.read_html(url_rpg)[0])
    df_o_rpg = pd.DataFrame(pd.read_html(url_o_rpg)[0])

    # print(df_rpg)
    # print(df_o_rpg)

    df_rpg = df_rpg.drop(['Rank', 'Last 3', 'Last 1', '2021'], axis=1)
    df_o_rpg = df_o_rpg.drop(['Rank', 'Last 3', 'Last 1', '2021'], axis=1)

    df_rpg = df_rpg.rename(
        columns={'2022': '2022_for', 'Home': 'home_for', 'Away': 'away_for'}
    )
    df_o_rpg = df_o_rpg.rename(
        columns={'2022': '2022_against',
                 'Home': 'home_against', 'Away': 'away_against'}
    )

    df_stats = pd.merge(
        df_rpg, df_o_rpg, on=['Team']
    )

    df_stats['Team'] = df_stats.apply(
        lambda x: team_rename(x['Team']), axis=1
    )

    df = pd.merge(
        df_stats, df_pf, on=['Team']
    )

    league_avg_against_home = df['home_against'].mean()
    league_avg_against_home = round(league_avg_against_home, 3)
    league_avg_against_away = df['away_against'].mean()
    league_avg_against_away = round(league_avg_against_away, 3)

    print(df)
    print(days)
    #
    df_starters = []
    for elem in days:
        url = str(url_pitchers) + str(elem)
        print(url)
        # df_rpg = pd.DataFrame(pd.read_html(url)[0])
        html_text = urllib.request.urlopen(
            url
        )
        # print(html_text)
        bs_obj = BeautifulSoup(html_text)
        tables = bs_obj.findAll('table', attrs={'class': 'TableBase-table'})
        print(tables)
        for table in tables:
            print('Date = ' + str(elem))
            df_table = pd.DataFrame(pd.read_html(str(table))[0])
            dat_e = date_dig_to_words([elem])
            print(dat_e)
            print(type(dat_e))
            df_table['date'] = dat_e[0]
            player = df_table['players']
            away_starter = df_table.iloc[0, 0]
            home_starter = df_table.iloc[1, 0]
            print('away starter: ' + str(away_starter))
            print('home starter: ' + str(home_starter))
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            print('PLAYER')
            print(type(player[0]))
            away_player_lst = away_starter.split('  ')
            home_player_lst = home_starter.split('  ')
            df_table['starter'] = [away_player_lst[3], home_player_lst[3]]
            df_table['team'] = [team_rename(
                away_player_lst[4]), team_rename(home_player_lst[4])]
            df_table['rhp/lhp'] = [away_player_lst[5], home_player_lst[5]]
            # print(player[0].split('  '))
            df_table['Matchup'] = str(team_rename(
                away_player_lst[4])) + ' @ ' + str(team_rename(home_player_lst[4])) + ' on ' + str(dat_e[0])
            new_cols_starters = ['starter', 'team', 'Matchup', 'rhp/lhp', 'date', 'W  Wins', 'L  Losses', 'IP  Innings Pitched', 'ERA  Earned Run Average',
                                 'BB  Base on Balls/Walks', 'SO  Strikeouts', 'WHIP  Walks And Hits Allowed Per Inning']
            df_table = df_table.reindex(columns=new_cols_starters)
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            # print(df)
            df_table.columns.values.tolist()
            df_starters.append(df_table)

    df_starters = pd.concat(df_starters)
    df_starters = df_starters.reset_index(drop=True)

    print('\n')
    print(df_starters)

    df_dk = pd.DataFrame(pd.read_html(url_dk)[0])

    html_dk = requests.get(url_dk)  # urlopen
    soup_dk = bs4.BeautifulSoup(html_dk.content, features="html.parser")
    soup_dk = str(soup_dk)

    table_count = soup_dk.count(
        '<div class="parlay-card-10-a">')

    print(table_count)

    df_lst = []  # pd.read_html(url_dk)[:table_count]
    i = 0
    while True:
        if i < table_count:
            dk = pd.DataFrame(pd.read_html(url_dk)[i])
            print('df')
            print(dk)
            col_lst = list(dk.columns)
            print('col lst')
            print(col_lst)
            dat_e = col_lst[0]
            dat_e = date_dig_to_words([dat_e])
            print('date fixed for df')
            print(dat_e)
            dat_e = dat_e[0]
            dk['date'] = dk.apply(lambda x: dat_e, axis=1)
            dk = dk.rename(columns={dat_e: 'Team'})
            df_lst.append(dk)
            i += 1
            continue
        else:
            break

    df_dk = pd.concat(df_lst)
    df_dk = df_dk.reset_index(drop=True)

    len_dk_df = len(df_dk.index)
    # print(df_dk.index)

    df_dk['Team'] = df_dk.apply(
        lambda x: team_rename(x['Team']), axis=1
    )

    opponent_lst = []
    mtch = []
    home_away = []
    odds_lst = []
    i = 0
    while True:
        if i < len_dk_df:
            if i % 2 == 0:
                o = i + 1
                team = df_dk['Team'][i]
                odds = df_dk['MONEYLINE'][i]
                dy = df_dk['date'][i]
                if odds[0] == '−':
                    odds = odds[1:]
                    odds = float(odds)
                    odds = round(-1 * odds, 2)
                odds = int(odds)
                team = team_rename(team)
                opp = df_dk['Team'][o]
                opp = team_rename(opp)
                matchup = team + ' @ ' + opp + ' on ' + str(dy)
                opponent_lst.append(opp)
                mtch.append(matchup)
                home_away.append('away')
                odds_lst.append(odds)
                i += 1
                continue
            else:
                o = i - 1
                odds = df_dk['MONEYLINE'][i]
                dy = df_dk['date'][i]
                if odds[0] == '−':
                    odds = odds[1:]
                    odds = float(odds)
                    odds = round(-1 * odds, 2)
                odds = int(odds)
                team = df_dk['Team'][i]
                team = team_rename(team)
                opp = df_dk['Team'][o]
                opp = team_rename(opp)
                matchup = opp + ' @ ' + team + ' on ' + str(dy)
                opponent_lst.append(opp)
                mtch.append(matchup)
                home_away.append('home')
                odds_lst.append(odds)
                i += 1
                continue
        else:
            break

    df_dk['Matchup'] = mtch
    df_dk['Opponent'] = opponent_lst
    df_dk['H/A'] = home_away
    df_dk['MONEYLINE'] = odds_lst

    df_dk = df_dk.rename(
        columns={'RUN LINE': 'run line', 'TOTAL': 'total', 'MONEYLINE': 'ml'})

    print(df_dk)

    df = pd.merge(
        df_dk, df, on=['Team']
    )

    # def merge_df_and_starters(mtch):
    #     df_starters.index[df_starters['column_name']==mtch].tolist()

    len_df = len(df.index)
    i = 0
    mtch_record = []
    dfs_strt = []
    while True:
        if i < len_df:
            mtch = df['Matchup'][i]
            c = mtch_record.count(mtch)
            lst_mtch = df_starters.index[df_starters['Matchup'] == mtch].tolist(
            )
            ind = lst_mtch[c]
            strt = df_starters.iloc[ind]
            print(strt)
            dfs_strt.append(strt)
            # df[i].append(strt)
            i += 1
            continue
            # if len(lst_mtch) == 2:
            #     if i % 2 == 0:
            #         ind = lst_mtch[0]

            #         i += 1
            #         continue
            #     else:
            #         ind = lst_mtch[1]
            #         i += 1
            #         continue
        else:
            break

    dfs_strt = pd.concat(dfs_strt)

    print(dfs_strt)

    df = df.join(dfs_strt)

    print(df)

    with pd.ExcelWriter('/Users/Hayden/OneDrive/Sports Betting/Baseball/Dont Use/mlb.xlsx') as writer:  # doctest: +SKIP
        df.to_excel(writer, sheet_name='main', index=False)
        df_pf.to_excel(writer, sheet_name='park factor', index=False)
        df_stats.to_excel(writer, sheet_name='stats', index=False)
        df_starters.to_excel(
            writer, sheet_name='probable starters', index=False)
        df_dk.to_excel(writer, sheet_name='DraftKings', index=False)

    # html_text = urllib.request.urlopen(
    #     url_games
    # )
    # bs_obj = BeautifulSoup(html_text)
    # # , attrs={'class': 'sportsbook-table'}
    # tables = bs_obj.findAll('table')
    # for table in tables:
    #     df = pd.DataFrame(pd.read_html(str(table))[0])

    return


mlb()
