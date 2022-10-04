from codecs import namereplace_errors
from decimal import Rounded
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


# url_f = 'https://www.teamrankings.com/mlb/stat/1st-inning-runs-per-game'
url_f = 'https://www.teamrankings.com/mlb/stat/1st-inning-scored-percentage'
df_f = pd.DataFrame(pd.read_html(url_f)[0])
df_f = df_f.drop(df_f.columns[[0, 2, 3, 4, 7]], axis=1)
df_f = df_f.rename(columns={'Home': 'Home_f_%', 'Away': 'Away_f_%'})
# url_a = 'https://www.teamrankings.com/mlb/stat/opponent-1st-inning-runs-per-game'
url_a = 'https://www.teamrankings.com/mlb/stat/opponent-1st-inning-scored-percentage'
df_a = pd.DataFrame(pd.read_html(url_a)[0])
df_a = df_a.drop(df_a.columns[[0, 2, 3, 4, 7]], axis=1)
df_a = df_a.rename(columns={'Home': 'Home_a_%', 'Away': 'Away_a_%'})
df = pd.merge(df_f, df_a, on='Team')


def per_to_num(col):
    nm = col[:-1]
    nm = float(nm)
    return round((nm / 100), 4)


df['Home_f'] = df.apply(lambda x: per_to_num(x['Home_f_%']), axis=1)
df['Away_f'] = df.apply(lambda x: per_to_num(x['Away_f_%']), axis=1)
df['Home_a'] = df.apply(lambda x: per_to_num(x['Home_a_%']), axis=1)
df['Away_a'] = df.apply(lambda x: per_to_num(x['Away_a_%']), axis=1)


# print(df)
# league_n_f = df['2022_f'].mean()
league_h_f = df['Home_f'].mean()
league_a_f = df['Away_f'].mean()
league_h_a = df['Home_a'].mean()
league_a_a = df['Away_a'].mean()


# def avg(league_avg, col):
#     return round(col * league_avg, 4)


# df['Away_f_avg'] = df.apply(lambda x: avg(league_a_f, x['Away_f']), axis=1)
# df['Home_a_avg'] = df.apply(lambda x: avg(league_h_a, x['Home_a']), axis=1)
# df['Away_a_avg'] = df.apply(lambda x: avg(league_a_a, x['Away_a']), axis=1)

df = df.drop(df.columns[[1, 2, 3, 4]], axis=1)
# df = df.drop(df.columns[[5, 6, 7, 8]], axis = 1)

# league_h_f_wt = df['Home_f_avg'].mean()
# league_a_f_wt = df['Away_f_avg'].mean()
# league_h_a_wt = df['Home_a_avg'].mean()
# league_a_a_wt = df['Away_a_avg'].mean()

# print('\n')
print(df)
# print('\n')

with pd.ExcelWriter('/Users/Hayden/OneDrive/Sports Betting/Baseball/nrfi.xlsx') as writer:  # doctest: +SKIP
    df.to_excel(writer, sheet_name='league 1st inning stats', index=False)


def nrfi(home, away):
    # home_avg_f = df.loc[df['Team'] == home, 'Home_f_avg'].iloc[0]
    # home_avg_a = df.loc[df['Team'] == home, 'Home_a_avg'].iloc[0]
    # away_avg_f = df.loc[df['Team'] == away, 'Away_f_avg'].iloc[0]
    # away_avg_a = df.loc[df['Team'] == away, 'Away_a_avg'].iloc[0]
    home_avg_f = df.loc[df['Team'] == home, 'Home_f'].iloc[0]
    home_avg_a = df.loc[df['Team'] == home, 'Home_a'].iloc[0]
    away_avg_f = df.loc[df['Team'] == away, 'Away_f'].iloc[0]
    away_avg_a = df.loc[df['Team'] == away, 'Away_a'].iloc[0]
    combo_for = round(((home_avg_f + away_avg_f) / 2), 4)
    combo_ag = round(((home_avg_a + away_avg_a) / 2), 4)
    home_fir = round(home_avg_f * away_avg_a / league_a_a, 4)
    home_fir_chance = round(1 - home_fir, 4)
    print('Home FIR = ' + str(home_fir) +
          ' and Home NRFI = ' + str(home_fir_chance))
    away_fir = round(away_avg_f * home_avg_a / league_h_a, 4)
    away_fir_chance = round(1 - away_fir, 4)
    print('Away FIR = ' + str(away_fir) +
          ' and Away NRFI = ' + str(away_fir_chance))
    chance = round(1 - (home_fir_chance * away_fir_chance), 4)
    matchup = str(away) + ' @ ' + str(home)
    lst = [matchup, chance]
    print(lst)
    # conclusion = str(away) + ' @ ' + str(home) + ' nrfi chance = ' + str(chance) + '%'
    # print(conclusion)
    # print(total_fir)
    return lst

############################################################################################################
#######################################       EDIT DATA      ###############################################
############################################################################################################


a3 = 'Miami'
h3 = 'Milwaukee'
a2 = 'Texas'
h2 = 'Seattle'
a1 = 'Colorado'
h1 = 'SF Giants'

# a4 = 'Boston'
# h4 = 'Houston'
# a5 = 'Seattle'
# h5 = 'NY Yankees'
# a6 = 'Colorado'
# h6 = ''

# (Home Team, Away Team)
g1 = nrfi(h1, a1)
g2 = nrfi(h2, a2)
g3 = nrfi(h3, a3)

# g4 = nrfi(h4, a4)
# g5 = nrfi(h5, a5)
# g6 = nrfi(h6, a6)

lst1 = [g1, g2, g3]

# lst2 = [g4, g5, g6]


all_chance = []


def chance(lst):
    lg = len(lst)
    i = 0
    name = ''
    name_lst = []
    chance_lst = []
    combo_lst = []
    chance = 1
    for team in lst:
        teamname = str(team[0]) + ', '
        team_name = str(team[0])
        name_lst.append(team_name)
        name += teamname
        team_chance = round(float(team[1]), 4)
        chance_lst.append(team_chance)
        chance *= team_chance
        chance = round(chance, 4)
        l = [team_name, team_chance]
        combo_lst.append(l)
    # chance = round(1 - chance, 4)
    name_lst.append('Combined')
    chance_lst.append(chance)
    combined_chance_row = ['Combined', chance]
    lg = len(name) - 2
    name = name[:30]
    # print(name)
    combo_lst.append(combined_chance_row)
    lsts = [combo_lst, name]
    # print(chance)
    # nrfi_df = pd.DataFrame(combo_lst, columns = headers)
    # nrfi_df.head()
    return lsts


b1 = chance(lst1)  # 'b' for 'bet'1

# b2 = chance(lst2)

lst_bets = [b1]  # , b2]


############################################################################################################
###################################        END EDIT DATA        ############################################
############################################################################################################

headers = ['Teams', 'Chance']

with pd.ExcelWriter('/Users/Hayden/OneDrive/Sports Betting/Baseball/nrfi.xlsx') as writer:  # doctest: +SKIP
    df.to_excel(writer, sheet_name='MLB', index=False)
    for elem in lst_bets:
        nrfi_df = pd.DataFrame(elem[0], columns=headers)
        nrfi_df.head()
        nrfi_df.to_excel(writer, sheet_name=str(elem[1]), index=False)

# chance(lst1)
