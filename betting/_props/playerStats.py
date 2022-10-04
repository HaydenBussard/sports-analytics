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

# html_espn_pbp = requests.get(url_espn_pbp + str(id))
#             soup_espn_pbp = bs4.BeautifulSoup(html_espn_pbp.content, features='html.parser') 
#             for ultag in soup_espn_pbp.find_all('ul', {'class': 'shots away-team'}):
#                 for litag in ultag.find('li', {'class': 'made'}):

url_hornets = 'https://www.espn.com/nba/team/roster/_/name/cha/charlotte-hornets'
html_hornets = requests.get(url_hornets)
soup_hornets = bs4.BeautifulSoup(html_hornets.content, features='html.parser')
ids_hornets = soup_hornets.find_all('a', {'class': 'AnchorLink'})

new = []

for elem in ids_hornets:
    if 'div' not in str(elem):
        if '/player/_/id/' in str(elem):
            new.append(str(elem))

for elem in new:
    print(elem)
    print('\n')

team_ids = []

i = 0
while True:
    if i < len(new):
        elem = new[i]
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
    
print('\n')

for elem in team_ids:
    print(elem)

# NOW GETTING GAME BY GAME STATS FOR EACH PLAYER

# url_espn_pbp = 'https://www.espn.com/nba/playbyplay/_/gameId/'#401360116
# url_espn_starters = 'https://www.espn.com/nba/boxscore/_/gameId/'
# h = 0
# b = 0
# i = 0
# while True:
#     if i < length_game_ids:
#         id = game_ids[i]
#         html_espn_pbp = requests.get(url_espn_pbp + str(id))
#         soup_espn_pbp = bs4.BeautifulSoup(html_espn_pbp.content, features='html.parser') 
#         for ultag in soup_espn_pbp.find_all('ul', {'class': 'shots away-team'}):

# url_gbg = 'https://www.espn.com/nba/player/gamelog/_/id/'

# i = 0
# while True:
#     if i < len(team_ids):
#         print('\n')
#         print(team_ids[i][0])
#         print('\n')
#         html_gbg = requests.get(url_gbg + str(team_ids[i][1]))
#         soup_gbg = bs4.BeautifulSoup(html_gbg.content, features='html.parser')
#         for elem in soup_gbg:
#             print(elem)
#         i += 1
#         continue
#     else:
#         break
        
        

