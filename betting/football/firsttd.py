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


def team_rename(team):
    if team == 'Buffalo' or 'BUF Bills' in team or team == 'BUF' or team == 'Buffalo Bills' or team == 'Bills':
        name = 'BUF Bills'
        return name
    if team == 'LA Rams' or 'LA Rams' in team or team == 'LAR' or team == 'Los Angeles Rams' or team == 'Rams':
        name = 'LA Rams'
        return name
    if team == 'Dallas' or 'DAL Cowboys' in team or team == 'DAL' or team == 'Dallas Cowboys' or team == 'Cowboys':
        name = 'DAL Cowboys'
        return name
    if team == 'Atlanta' or 'ATL Falcons' in team or team == 'ATL' or team == 'Atlanta Falcons' or team == 'Falcons':
        name = 'ATL Falcons'
        return name
    if team == 'Washington' or 'WAS Commanders' in team or team == 'WSH' or team == 'Washington Commanders' or team == 'Commanders':
        name = 'WAS Commanders'
        return name
    if team == 'Pittsburgh' or 'PIT Steelers' in team or team == 'PIT' or team == 'Pittsburgh Steelers' or team == 'Steelers':
        name = 'PIT Steelers'
        return name
    if team == 'New Orleans' or 'NO Saints' in team or team == 'NO' or team == 'New Orleans Saints' or team == 'Saints':
        name = 'NO Saints'
        return name
    if team == 'Las Vegas' or 'LV Raiders' in team or team == 'LV' or team == 'Las Vegas Raiders' or team == 'Raiders':
        name = 'LV Raiders'
        return name
    if team == 'Detroit' or 'DET Lions' in team or team == 'DET' or team == 'Detroit Lions' or team == 'Lions':
        name = 'DET Lions'
        return name
    if team == 'Chicago' or 'CHI Bears' in team or team == 'CHI' or team == 'Chicago Bears' or team == 'Bears':
        name = 'CHI Bears'
        return name
    if team == 'Jacksonville' or 'JAX Jaguars' in team or team == 'JAX' or team == 'Jacksonville Jaguars' or team == 'Jaguars':
        name = 'JAX Jaguars'
        return name
    if team == 'San Francisco' or 'SF 49ers' in team or team == 'SF' or team == 'San Francisco 49ers' or team == '49ers':
        name = 'SF 49ers'
        return name
    if team == 'NY Jets' or 'NY Jets' in team or team == 'NYJ' or team == 'New York Jets' or team == 'Jets':
        name = 'NY Jets'
        return name
    if team == 'Miami' or 'MIA Dolphins' in team or team == 'MIA' or team == 'Miami Dolphins' or team == 'Dolphins':
        name = 'MIA Dolphins'
        return name
    if team == 'Tennessee' or 'TEN Titans' in team or team == 'TEN' or team == 'Tennessee Titans' or team == 'Titans':
        name = 'TEN Titans'
        return name
    if team == 'Cleveland' or 'CLE Browns' in team or team == 'CLE' or team == 'Cleveland Browns' or team == 'Browns':
        name = 'CLE Browns'
        return name
    if team == 'Houston' or 'HOU Texans' in team or team == 'HOU' or team == 'Houston Texans' or team == 'Texans':
        name = 'HOU Texans'
        return name
    if team == 'Tampa Bay' or 'TB Buccaneers' in team or team == 'TB' or team == 'Tampa Bay Buccaneers' or team == 'Buccaneers':
        name = 'TB Buccaneers'
        return name
    if team == 'Arizona' or 'ARI Cardinals' in team or team == 'ARI' or team == 'Arizona Cardinals' or team == 'Cardinals':
        name = 'ARI Cardinals'
        return name
    if team == 'New England' or 'NE Patriots' in team or team == 'NE' or team == 'New England Patriots' or team == 'Patriots':
        name = 'NE Patriots'
        return name
    if team == 'Kansas City' or 'KC Chiefs' in team or team == 'KC' or team == 'Kansas City Chiefs' or team == 'Chiefs':
        name = 'KC Chiefs'
        return name
    if team == 'Denver' or 'DEN Broncos' in team or team == 'DEN' or team == 'Denver Broncos' or team == 'Broncos':
        name = 'DEN Broncos'
        return name
    if team == 'Carolina' or 'CAR Panthers' in team or team == 'CAR' or team == 'Carolina Panthers' or team == 'Panthers':
        name = 'CAR Panthers'
        return name
    if team == 'LA Chargers' or 'LA Chargers' in team or team == 'LAC' or team == 'Los Angeles Chargers' or team == 'Chargers':
        name = 'LA Chargers'
        return name
    if team == 'NY Giants' or 'NY Giants' in team or team == 'NYG' or team == 'New York Giants' or team == 'Giants':
        name = 'NY Giants'
        return name
    if team == 'Green Bay' or 'GB Packers' in team or team == 'GB' or team == 'Green Bay Packers' or team == 'Packers':
        name = 'GB Packers'
        return name
    if team == 'Cincinnati' or 'CIN Bengals' in team or team == 'CIN' or team == 'Cincinnati Bengals' or team == 'Bengals':
        name = 'CIN Bengals'
        return name
    if team == 'Baltimore' or 'BAL Ravens' in team or team == 'BAL' or team == 'Baltimore Ravens' or team == 'Ravens':
        name = 'BAL Ravens'
        return name
    if team == 'Seattle' or 'SEA Seahawks' in team or team == 'SEA' or team == 'Seattle Seahawks' or team == 'Seahawks':
        name = 'SEA Seahawks'
        return name
    if team == 'Philadelphia' or 'PHI Eagles' in team or team == 'PHI' or team == 'Philadelphia Eagles' or team == 'Eagles':
        name = 'PHI Eagles'
        return name
    if team == 'Minnesota' or 'MIN Vikings' in team or team == 'MIN' or team == 'Minnesota Vikings' or team == 'Vikings':
        name = 'MIN Vikings'
        return name
    if team == 'Indianapolis' or 'IND Colts' in team or team == 'IND' or team == 'Indianapolis Colts' or team == 'Colts':
        name = 'IND Colts'
        return name
    else:
        return team


def first_tds_lst(play):
    play = str(play)
    ind0 = play.index(':') + 3
    play = play[ind0:]
    num_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    type_lst = [' run ', ' Run ', ' pass ', ' Pass ']
    ind1 = 0
    while True:
        if ind1 < len(play):
            if play[ind1] not in num_lst:
                ind1 += 1
                continue
            else:
                break
        else:
            break
    ind1 -= 1
    name = play[:ind1]
    for elem in type_lst:
        if elem in name:
            ind2 = name.index(elem) - 1
            name = name[:ind2]
            continue
        else:
            continue
    if 'Run' in play or 'run' in play:
        play_type = 'run'
    elif 'pass' in play or 'Pass' in play:
        play_type = 'pass'
    elif 'Kickoff Return' in play:
        play_type = 'kick return'
    elif 'Fumble Return' in play:
        play_type = 'fumble return'
    elif 'Interception' in play:
        play_type = 'pick 6'
    else:
        play_type = 'other'
    lst = [name, play_type]
    return lst


def first_td_player(lst):
    name = lst[0]
    return name


def first_td_type(lst):
    play_type = lst[1]
    return play_type


df_first_td = pd.DataFrame(columns=['play', 'scoring_team', 'opponent'])

dfs = []
firsttds = []
df_espn = pd.DataFrame(columns=['Team', 'Matchup', 'espn_%'])
url_main = 'https://www.espn.com/nfl/scoreboard'
html_main = requests.get(url_main)  # urlopen
soup_main = bs4.BeautifulSoup(html_main.content, features="html.parser")
scrape_main = soup_main.findAll(
    'div', attrs={'class': 'react-swipe-container DateCarousel__List'}
)
str_main = str(soup_main)
splt_main = str_main.split(
    '"year":2022,"url":"/nfl/scoreboard')

del splt_main[0]

week_urls = []

for elem in splt_main:
    # print(elem)
    ind = elem.index('","isActive":')
    url = elem[:ind]
    url = 'https://www.espn.com/nfl/scoreboard' + url
    if url in week_urls:
        continue
    else:
        week_urls.append(url)

for elem in week_urls:
    print(elem)

# df_espn = pd.DataFrame(columns=['Team', 'Matchup', 'espn_%'])

for elem in week_urls:
    url_main = elem
    html_main = requests.get(url_main)  # urlopen
    soup_main = bs4.BeautifulSoup(
        html_main.content, features="html.parser")
    scrape_main = soup_main.findAll(
        'div', attrs={'class': 'ScoreCell__Time ScoreboardScoreCell__Time h9 clr-gray-01'}
    )

    str_main = str(soup_main)

    # str_main = str_main.split(
    #     '<div class="ScoreCell__Time ScoreboardScoreCell__Time h9 clr-gray-01"></div>')
    str_main = str_main.split(
        '"link":"/nfl/game/_/gameId/'
    )

    # last_completed = str_main[-1]
    # ind_last_comp = last_completed.index('</section') + 8
    # last_completed = last_completed[ind_last_comp:]
    # each_game = last_completed.split(
    #     'Scoreboard bg-clr-white flex flex-auto justify-between" id="')
    each_game = str_main
    i = 0
    while True:
        if i < len(each_game):
            print('Game ID = ' + str(each_game[i])[:9])
            each_game[i] = each_game[i][:9]
            i += 1
            continue
        else:
            break

    each_game = each_game[1:]
    print('\n')
    print('Each game ID list:')
    print(each_game)
    print('\n')

    weeks = soup_main.findAll(
        'div', attrs={'class': 'custom--week'}
    )

    for elem in weeks:
        print(elem.text)

    for el in each_game:
        url_games = 'https://www.espn.com/nfl/game/_/gameId/' + el
        html_games = requests.get(url_games)  # urlopen
        soup_games = bs4.BeautifulSoup(
            html_games.content, features="html.parser")
        preseason_tag = soup_games.findAll(
            'div', attrs={'class': 'game-details header'}  # chart-container
        )
        if len(preseason_tag) > 0:
            print(preseason_tag[0].text)
            preseason_filter = preseason_tag[0].text
            if preseason_filter == 'Preseason':
                continue
        # for e in scrape_games:
        #     print(e.text)

        html_text = urllib.request.urlopen(
            url_games
        )
        bs_obj = BeautifulSoup(html_text)
        # , attrs={'class': 'sportsbook-table'}
        tables = bs_obj.findAll('table')
        for table in tables:
            df = pd.DataFrame(pd.read_html(str(table))[0])
            df.columns.values.tolist()
            col_lst = list(df.columns)

            print('ITERATING THRU COL LIST')
            for h in col_lst:
                print(h)
            print('DONE ITERATING THRU COL LIST')
            # print('col_lst[0] = ' + str(col_lst[0]))
            if 'Quarter' not in str(col_lst[0]):
                continue
            if len(col_lst) > 1:
                td_col = str(col_lst[1])
                away_team = str(col_lst[2])
                home_team = str(col_lst[3])
                print(td_col)
                print('col_lst[0] = ' + str(col_lst[0]))
                print(df)
            df = df.drop(df.columns[[0]], axis=1)
            print('\n')
            print('ITERATING THRU SCORING PLAY LIST')
            first_only = 0
            for ind in df.index:
                away_score = df[away_team][ind]
                home_score = df[home_team][ind]
                scoring_play = df[td_col][ind]
                if 'TD' in str(scoring_play[:3]) and first_only == 0:
                    print(df[td_col][ind])
                    if away_score > home_score:
                        lst = [scoring_play, away_team, home_team]
                        df_espn_game = pd.DataFrame(np.array([lst]), columns=[
                            'play', 'scoring_team', 'opponent'])
                        df_first_td = df_first_td.append(
                            df_espn_game, ignore_index=True)
                        first_only += 1
                        continue
                    else:
                        lst = [scoring_play, home_team, away_team]
                        df_espn_game = pd.DataFrame(np.array([lst]), columns=[
                            'play', 'scoring_team', 'opponent'])
                        df_first_td = df_first_td.append(
                            df_espn_game, ignore_index=True)
                        first_only += 1
                        continue
                else:
                    continue
            print('DONE ITERATING THRU SCORING PLAY LIST')
            print('\n')

            # i = 0
            # while True:
            #     if i < len(df):
            #         td = df.loc[df[td_col]].iloc[0]
            #         print(td)
            #         print(td)
            #         print(df.loc[[i]])
            #         print('\n')
            #         i += 1
            #         continue
            #     else:
            #         break
            # print(col_lst)
            # print(df.columns.to_list())

            # df.columns.values.tolist()
            # col_lst = list(df.columns)
            # dat_e = col_lst[0]
            # df = df.rename(
            #     columns={dat_e: 'Team'})
            # df['date'] = df.apply(lambda x: dat_e, axis=1)
            dfs.append(df)

        print(url_games)


df_first_td['play_lst'] = df_first_td.apply(
    lambda x: first_tds_lst(x['play']), axis=1
)
df_first_td['player'] = df_first_td.apply(
    lambda x: first_td_player(x['play_lst']), axis=1
)
df_first_td['type'] = df_first_td.apply(
    lambda x: first_td_type(x['play_lst']), axis=1
)

new_cols = ['player', 'type', 'scoring_team', 'opponent']

df_first_td = df_first_td.reindex(columns=new_cols)

df_team = df_first_td.sort_values(by=['scoring_team'])  # , ascending=False
df_opp = df_first_td.sort_values(by=['opponent'])
df_player = df_first_td.sort_values(by=['player'])

print('\n')
print(df_first_td)
print('\n')


with pd.ExcelWriter('/Users/Hayden/OneDrive/Sports Betting/Football/first_td.xlsx') as writer:  # doctest: +SKIP
    df_first_td.to_excel(writer, sheet_name='first td draft', index=False)
    df_team.to_excel(writer, sheet_name='sorted by team', index=False)
    df_opp.to_excel(writer, sheet_name='sorted by opponent', index=False)
    df_player.to_excel(writer, sheet_name='sorted by player', index=False)
