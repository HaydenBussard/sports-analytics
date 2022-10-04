from os import pipe
from typing import Match, Text
from urllib import request
from xml.etree.ElementTree import TreeBuilder
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


def onePlayer(league, team, player, stat, value, bet_type):
    if league == 'MLB':
        if team == 'Buffalo':
            team_url = 'buf/buffalo-bills'
        if team == 'Miami':
            team_url = 'mia/miami-dolphins'
        if team == 'New England':
            team_url = 'ne/new-england-patriots'
        if team == 'NY Jets':
            team_url = 'nyj/new-york-jets'
        if team == 'Baltimore':
            team_url = 'bal/baltimore-ravens'
        if team == 'Cincinnati':
            team_url = 'cin/cincinnati-bengals'
        if team == 'Cleveland':
            team_url = 'cle/cleveland-browns'
        if team == 'Pittsburgh':
            team_url = 'pit/pittsburgh-steelers'
        if team == 'Houston':
            team_url = 'hou/houston-texans'
        if team == 'Indianapolis':
            team_url = 'ind/indianapolis-colts'
        if team == 'Jacksonville':
            team_url = 'jax/jacksonville-jaguars'
        if team == 'Tennessee':
            team_url = 'ten/tennessee-titans'
        if team == 'Denver':
            team_url = 'den/denver-broncos'
        if team == 'Kansas City':
            team_url = 'kc/kansas-city-chiefs'
        if team == 'Las Vegas':
            team_url = 'lv/las-vegas-raiders'
        if team == 'LA Chargers':
            team_url = 'los-angeles-chargers'
        if team == 'Dallas':
            team_url = 'dal/dallas-cowboys'
        if team == 'NY Giants':
            team_url = 'nyg/new-york-giants'
        if team == 'Philly':
            team_url = 'phi/philadelphia-eagles'
        if team == 'Washington':
            team_url = 'wsh/washington-commanders'
        if team == 'Chicago':
            team_url = 'chi/chicago-bears'
        if team == 'Detroit':
            team_url = 'det/detroit-lions'
        if team == 'Green Bay':
            team_url = 'gb/green-bay-packers'
        if team == 'Minnesota':
            team_url = 'min/minnesota-vikings'
        if team == 'Atlanta':
            team_url = 'atl/atlanta-falcons'
        if team == 'Carolina':
            team_url = 'car/carolina-panthers'
        if team == 'New Orleans':
            team_url = 'no/new-orleans-saints'
        if team == 'Tampa Bay':
            team_url = 'tb/tampa-bay-buccaneers'
        if team == 'Arizona':
            team_url = 'ari/arizona-cardinals'
        if team == 'LA Rams':
            team_url = 'lar/los-angeles-rams'
        if team == 'San Francisco':
            team_url = 'sf/san-francisco-49ers'
        if team == 'Seattle':
            team_url = 'sea/seattle-seahawks'

    url_roster = 'https://www.espn.com/mlb/team/roster/_/name/'
    html_roster = requests.get(url_roster + team_url)
    soup_roster = bs4.BeautifulSoup(
        html_roster.content, features='html.parser')
    ids_roster = soup_roster.find_all('a', {'class': 'AnchorLink'})

    roster_ids = []
    for elem in ids_roster:
        if 'div' not in str(elem):
            if '/player/_/id/' in str(elem):
                roster_ids.append(str(elem))

    team_ids = []

    i = 0
    while True:
        if i < len(roster_ids):
            elem = roster_ids[i]
            name_index = elem.index('"0">')
            name_end_index = elem.index('</a>')
            id_index = elem.index('/id/')
            id_end_index = elem.index('" tabindex=')
            player_name = elem[name_index + 4: name_end_index]
            player_id = elem[id_index + 4: id_end_index]
            lst = [player_name, player_id]
            team_ids.append(lst)
            i += 1
            continue
        else:
            break

    if bet_type == 'batting':
        dict_team_ids = {x[0]: x[1:] for x in team_ids}
        team_ids_keys = (dict_team_ids.keys())
        if player in team_ids_keys:
            player_id = dict_team_ids[player]
            player_id = player_id[0]
        else:
            return('Wrong player name.')

        url_gbg = 'https://www.espn.com/mlb/player/gamelog/_/id/'
        url_gbg_end = '/category/batting'
        html_gbg = requests.get(url_gbg + player_id + url_gbg_end)
        soup_gbg = bs4.BeautifulSoup(html_gbg.content, features='html.parser')

        gbg = []

        for elem in soup_gbg:
            if 'Regular Season' in str(elem):
                gbg.append(str(elem))

        player_gbg = gbg[0]
        game = player_gbg.index(
            '"groups":[{"name":"2022 Regular Season","tbls":[{"name":')  # Regular Season
        # game = player_gbg.index('{"name":"Postseason","tbls":') # Post Season
        player_gbg = player_gbg[game:]
        player_gbg = str(player_gbg)
        # print('\n')
        # print(player_gbg)
        # print('\n')
        if '{"name":"Regular Season Stats","data":[["Totals",' in player_gbg:
            preseason_index = player_gbg.index(
                '{"name":"Regular Season Stats","data":[["Totals",')
            player_gbg = player_gbg[:preseason_index]
            # print('\n')
            # print(player_gbg)
            # print('\n')
        if ',"nt":null}],"totals":{"stats":[' in player_gbg:
            x = player_gbg.count(',"nt":null}],"totals":{"stats":[')
            # print('\n')
            # print(x)
            # print('\n')
            i = 0
            while True:
                if i < x:
                    # print('\n')
                    # print(str(player_gbg.count(',"nt":null}],"totals":{"stats":[')))
                    # print(str(player_gbg.count('"],"label":"')))
                    # print('\n')
                    if '"],"label":"' in player_gbg:
                        # print('pre length = ' + str(len(player_gbg)))
                        ind = player_gbg.index(
                            ',"nt":null}],"totals":{"stats":[')
                        # print(ind)
                        ind_end = player_gbg.index('"],"label":"') + 11
                        # print(ind_end)
                        player_gbg = player_gbg[:ind] + player_gbg[ind_end:]
                        # print('post length = ' + str(len(player_gbg)))
                        # ind_end = player_gbg.index('"],"label":"')
                        # print('New ending index ' + str(ind_end))
                        i += 1
                        continue
                    else:
                        player_gbg = player_gbg[:ind]
                        break
                else:
                    # print('\n')
                    # print(player_gbg)
                    # print('\n')
                    break
        player_stats = player_gbg.split('"stats":[')
        i = 0
        while True:
            if i < len(player_stats):
                if '"allStar":"' in player_stats[i]:
                    # print(player_stats[i])
                    # print(player_stats[i + 1])
                    del player_stats[i + 1]
                    i += 1
                    continue
                else:
                    i += 1
                    continue
            else:
                break
        i = 0
        while True:
            if i < len(player_stats):
                if ']' in str(player_stats[i]):
                    ind = player_stats[i].index(']')
                    player_stats[i] = player_stats[i][:ind]
                    player_stats[i] = player_stats[i].split(',')
                    lst = player_stats[i]
                    # print(lst)
                    a = 0
                    while True:
                        if a < len(player_stats[i]):
                            player_stats[i][a] = player_stats[i][a][1:-1]
                            if '.' in str(player_stats[i][a]):
                                player_stats[i][a] = float(player_stats[i][a])
                            elif str(player_stats[i][a]) == '-':
                                player_stats[i][a] = 0
                            else:
                                player_stats[i][a] = int(player_stats[i][a])
                            a += 1
                            continue
                        else:
                            break
                    i += 1
                    continue
                else:
                    del player_stats[i]
                    continue
            else:
                break

        batting_stats = [['at bats'],
                         ['runs'],
                         ['hits'],
                         ['doubles'],
                         ['triples'],
                         ['homers'],
                         ['rbi'],
                         ['walks'],
                         ['hits by pitch'],
                         ['strikeouts'],
                         ['stolen bases'],
                         ['caught steals'],
                         ['batting average'],
                         ['on base %'],
                         ['slugging %'],
                         ['OPS']
                         ]

        i = 0
        a = 0
        while True:
            if i < len(player_stats):
                if a < len(batting_stats):
                    batting_stats[a].append(player_stats[i][a])
                    a += 1
                    continue
                else:
                    a = 0
                    i += 1
                    continue
            else:
                break

        singles_list = ['singles']
        bases_list = ['bases']

        i = 1
        while True:
            if i < len(batting_stats[2]):
                # hits = 2
                hits = batting_stats[2][i]
                # doubles = 3
                doubles = batting_stats[3][i]
                doubles_multiple = 2
                # triples = 4
                triples = batting_stats[4][i]
                triples_multiple = 3
                # homers = 5
                homers = batting_stats[5][i]
                homers_multiple = 4
                singles = hits - doubles - triples - homers
                bases = singles + (doubles * doubles_multiple) + \
                    (triples * triples_multiple) + (homers * homers_multiple)
                singles_list.append(singles)
                bases_list.append(bases)
                i += 1
                continue
            else:
                batting_stats.append(singles_list)
                batting_stats.append(bases_list)
                break

        # print('\n')
        # for elem in batting_stats:
        #     print(elem)
        # print('\n')

        # for elem in batting_stats:
        #     print(elem)

        dict_batting_stats = {x[0]: x[1:] for x in batting_stats}
        batting_stats_keys = (dict_batting_stats.keys())

        if stat in batting_stats_keys:
            stat_list = dict_batting_stats[stat]
            # print(stat_list)
        else:
            return('Wrong stat.')

        avg = statistics.mean(stat_list)
        std = statistics.pstdev(stat_list)
        # count = np.count_nonzero(stat_list)
        # count = int(count)
        i = 0
        count = 0
        while True:
            if i < len(stat_list):
                if float(stat_list[i]) > float(value):
                    count += 1
                    i += 1
                    continue
                else:
                    i += 1
                    continue
            else:
                break
        game_count = int(len(stat_list))
        # team, player, stat
        print('\n')
        print(str(player) + "'s count for " + str(stat) +
              ' = ' + str(count) + '/' + str(game_count))
        # team, player, stat
        print('\n')
        print(str(player) + "'s average " + str(stat) + ' = ' + str(avg))
        print(str(player) + "'s " + str(stat) +
              ' standard deviation = ' + str(std))
        player_chance = scipy.stats.norm.cdf(value, avg, std)
        player_chance = round(1 - player_chance, 6)
        player_chance = round(player_chance * 100, 4)
        print(str(player) + ' has a ' + str(player_chance) +
              '% chance of ' + str(value) + '+ ' + str(stat) + '.')
        print('\n')
        return
    if bet_type == 'pitching':
        dict_team_ids = {x[0]: x[1:] for x in team_ids}
        team_ids_keys = (dict_team_ids.keys())
        if player in team_ids_keys:
            player_id = dict_team_ids[player]
            player_id = player_id[0]
        else:
            return('Wrong player name.')

        url_gbg = 'https://www.espn.com/mlb/player/gamelog/_/id/'
        url_gbg_end = '/category/pitching'  # or     /category/batting
        html_gbg = requests.get(url_gbg + player_id + url_gbg_end)
        # print(url_gbg + player_id + url_gbg_end)
        soup_gbg = bs4.BeautifulSoup(html_gbg.content, features='html.parser')

        gbg = []

        for elem in soup_gbg:
            if 'Regular Season' in str(elem):
                gbg.append(str(elem))

        player_gbg = gbg[0]
        player_gbg = gbg[0]
        game = player_gbg.index(
            '"groups":[{"name":"2022 Regular Season","tbls":[{"name":')  # Regular Season
        # game = player_gbg.index('{"name":"Postseason","tbls":') # Post Season
        player_gbg = player_gbg[game:]
        player_gbg = str(player_gbg)
        # print('\n')
        # print(player_gbg)
        # print('\n')
        if '{"name":"Regular Season Stats","data":[["Totals",' in player_gbg:
            preseason_index = player_gbg.index(
                '{"name":"Regular Season Stats","data":[["Totals",')
            player_gbg = player_gbg[:preseason_index]
            # print('\n')
            # print(player_gbg)
            # print('\n')
        if ',"nt":null}],"totals":{"stats":[' in player_gbg:
            x = player_gbg.count(',"nt":null}],"totals":{"stats":[')
            # print('\n')
            # print(x)
            # print('\n')
            i = 0
            while True:
                if i < x:
                    # print('\n')
                    # print(str(player_gbg.count(',"nt":null}],"totals":{"stats":[')))
                    # print(str(player_gbg.count('"],"label":"')))
                    # print('\n')
                    if '"],"label":"' in player_gbg:
                        # print('pre length = ' + str(len(player_gbg)))
                        ind = player_gbg.index(
                            ',"nt":null}],"totals":{"stats":[')
                        # print(ind)
                        ind_end = player_gbg.index('"],"label":"') + 11
                        # print(ind_end)
                        player_gbg = player_gbg[:ind] + player_gbg[ind_end:]
                        # print('post length = ' + str(len(player_gbg)))
                        # ind_end = player_gbg.index('"],"label":"')
                        # print('New ending index ' + str(ind_end))
                        i += 1
                        continue
                    else:
                        player_gbg = player_gbg[:ind]
                        break
                else:
                    # print('\n')
                    # print(player_gbg)
                    # print('\n')
                    break
        player_stats = player_gbg.split('"stats":[')
        i = 0
        while True:
            if i < len(player_stats):
                if '"allStar":"' in player_stats[i]:
                    # print(player_stats[i])
                    # print(player_stats[i + 1])
                    del player_stats[i + 1]
                    i += 1
                    continue
                else:
                    i += 1
                    continue
            else:
                break
        i = 0
        while True:
            if i < len(player_stats):
                if ']' in str(player_stats[i]):
                    ind = player_stats[i].index(']')
                    player_stats[i] = player_stats[i][:ind]
                    player_stats[i] = player_stats[i].split(',')
                    lst = player_stats[i]
                    a = 0
                    while True:
                        if a < len(player_stats[i]):
                            # print(player_stats[i])
                            player_stats[i][a] = player_stats[i][a][1:-1]
                            if '.' in str(player_stats[i][a]):
                                player_stats[i][a] = float(player_stats[i][a])
                            # just made any 'decision' values zero since that isnt used at all right now
                            elif str(player_stats[i][a]) == '-' or str(player_stats[i][a][0]) == 'L' or str(player_stats[i][a][0]) == 'W' or 'BLSV' in str(player_stats[i][a]) or 'HLD(' in str(player_stats[i][a]):
                                player_stats[i][a] = 0
                            else:
                                player_stats[i][a] = int(player_stats[i][a])
                            a += 1
                            continue
                        else:
                            break
                    i += 1
                    continue
                else:
                    del player_stats[i]
                    continue
            else:
                break

        pitching_stats = [['innings pitched'],
                          ['hits'],
                          ['runs'],
                          ['earned runs'],
                          ['homers'],
                          ['walks'],
                          ['strikeouts'],
                          ['ground balls'],
                          ['fly balls'],
                          ['pitches'],
                          ['batters faced'],
                          ['game score'],
                          ['decision'],
                          ['saves-blown/saves-holds'],
                          ['era']
                          ]

        i = 0
        a = 0
        while True:
            if i < len(player_stats):
                if a < len(pitching_stats):
                    pitching_stats[a].append(player_stats[i][a])
                    a += 1
                    continue
                else:
                    a = 0
                    i += 1
                    continue
            else:
                break

        # for elem in pitching_stats:
        #     print(elem)

        dict_pitcher_stats = {x[0]: x[1:] for x in pitching_stats}
        pitcher_stats_keys = (dict_pitcher_stats.keys())

        if stat in pitcher_stats_keys:
            stat_list = dict_pitcher_stats[stat]
            # print(stat_list)
        else:
            return('Wrong stat.')

        avg = statistics.mean(stat_list)
        std = statistics.pstdev(stat_list)
        # team, player, stat
        print('\n')
        i = 0
        count = 0
        while True:
            if i < len(stat_list):
                if float(stat_list[i]) > float(value):
                    count += 1
                    i += 1
                    continue
                else:
                    i += 1
                    continue
            else:
                break
        game_count = int(len(stat_list))
        # team, player, stat
        print('\n')
        print(str(player) + "'s count for " + str(stat) +
              ' = ' + str(count) + '/' + str(game_count))
        print(str(player) + "'s average " + str(stat) + ' = ' + str(avg))
        print(str(player) + "'s " + str(stat) +
              ' standard deviation = ' + str(std))
        player_chance = scipy.stats.norm.cdf(value, avg, std)
        player_chance = round(1 - player_chance, 6)
        player_chance = round(player_chance * 100, 4)
        allowed_list = ['hits', 'runs', 'earned runs',
                        'homers', 'walks', 'ground balls', 'fly balls']
        if stat in allowed_list:
            print(str(player) + ' has a ' + str(player_chance) +
                  '% chance of allowing ' + str(value) + '+ ' + str(stat) + '.')
        else:
            print(str(player) + ' has a ' + str(player_chance) +
                  '% chance of ' + str(value) + '+ ' + str(stat) + '.')
        print('\n')

        return

    return


onePlayer('MLB', 'Houston', 'Jose Altuve', 'hits', 0.5, 'batting')
onePlayer('MLB', 'Atlanta', 'Dansby Swanson', 'hits', 0.5, 'batting')
onePlayer('MLB', 'Kansas City', 'Vinnie Pasquantino', 'hits', 0.5, 'batting')


# batting_stats = [['at bats'],
#                     ['runs'],
#                     ['hits'],
#                     ['doubles'],
#                     ['triples'],
#                     ['homers'],
#                     ['rbi'],
#                     ['walks'],
#                     ['hits by pitch'],
#                     ['strikeouts'],


#                     ['stolen bases'],
#                     ['caught steals'],
#                     ['batting average'],
#                     ['on base %'],
#                     ['slugging %'],
#                     ['OPS']
#                     ]

# pitching_stats = [['innings pitched'],
#             ['hits'],
#             ['runs'],
#             ['earned runs'],
#             ['homers'],
#             ['walks'],
#             ['strikeouts'],
#             ['ground balls'],
#             ['fly balls'],
#             ['pitches'],
#             ['batters faced'],
#             ['game score'],
#             ['decision'],
#             ['saves-blown/saves-holds'],
#             ['era']
#             ]
