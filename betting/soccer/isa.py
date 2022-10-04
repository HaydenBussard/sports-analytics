from operator import itemgetter
import bs4
import numpy as np
import json
from json import scanner
from numpy.lib.arraysetops import in1d
import requests
import re
import datetime
from datetime import date, datetime, timedelta
# import urllib
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
import schedule


def ISA():
    def rename(teamName):
        if teamName == 'Napoli':
            teamName = 'Napoli'
            return teamName
        if teamName == 'Atalanta':
            teamName = 'Atalanta'
            return teamName
        if teamName == 'Torino':
            teamName = 'Torino'
            return teamName
        if teamName == 'AS Roma':
            teamName = 'AS Roma'
            return teamName
        if teamName == 'Udinese':
            teamName = 'Udinese'
            return teamName
        if teamName == 'Inter Milan':
            teamName = 'Inter Milan'
            return teamName
        if teamName == 'AC Milan':
            teamName = 'AC Milan'
            return teamName
        if teamName == 'Hellas Verona':
            teamName = 'Verona'
            return teamName
        if teamName == 'Fiorentina':
            teamName = 'Fiorentina'
            return teamName
        if teamName == 'Juventus':
            teamName = 'Juventus'
            return teamName
        if teamName == 'Lazio':
            teamName = 'Lazio'
            return teamName
        if teamName == 'Salernitana':
            teamName = 'Salernitana'
            return teamName
        if teamName == 'Sampdoria':
            teamName = 'Sampdoria'
            return teamName
        if teamName == 'Bologna':
            teamName = 'Bologna'
            return teamName
        if teamName == 'Empoli':
            teamName = 'Empoli'
            return teamName
        if teamName == 'Lecce':
            teamName = 'Lecce'
            return teamName
        if teamName == 'Cremonese':
            teamName = 'Cremonese'
            return teamName
        if teamName == 'Sassuolo':
            teamName = 'Sassuolo'
            return teamName
        if teamName == 'Spezia':
            teamName = 'Spezia'
            return teamName
        if teamName == 'Monza':
            teamName = 'Monza Brianza'
            return teamName
        else:
            return teamName

    url_soccerstats_ISA = 'https://www.soccerstats.com/homeaway.asp?league=italy'
    html_soccerstats_ISA = requests.get(url_soccerstats_ISA)
    soup_soccerstats_ISA = bs4.BeautifulSoup(
        html_soccerstats_ISA.content, 'html.parser')
    df_soccerstats_ISA = soup_soccerstats_ISA.findAll('tr', attrs={
        'class': 'odd'})
    stats = []
    a = 0
    for elem in df_soccerstats_ISA:
        r = str(elem.text)
        r = r.split('\n')
        # r = r[1:]
        data = []
        for el in r:
            if el != '':
                data.append(el)
            else:
                continue
        data = data[1:]
        # print(data)
        stats.append(data)
    stats = stats[:40]
    i = 0
    y = 1
    while True:
        if i < len(stats):
            if y < len(stats[i]):
                stat = int(stats[i][y])
                stats[i][y] = stat
                y += 1
                continue
            else:
                i += 1
                y = 1
                continue
        else:
            break
    # print('\n')

    # for elem in stats:
    #     print(elem)
    home_stats = stats[:20]
    away_stats = stats[20:]
    home_stat_headers = ['Team', 'home_gp', 'home_w', 'home_d',
                         'home_l', 'home_gf', 'home_ga', 'home_gd', 'home_pts']
    away_stat_headers = ['Team', 'away_gp', 'away_w', 'away_d',
                         'away_l', 'away_gf', 'away_ga', 'away_gd', 'away_pts']
    home_stats_df = pd.DataFrame(
        home_stats, columns=home_stat_headers)
    # home_avg_f = df.loc[df['Team'] == home, 'Home_f'].iloc[0]
    print(home_stats_df)
    # print('\n')
    away_stats_df = pd.DataFrame(
        away_stats, columns=away_stat_headers)
    print(away_stats_df)

    home_stats_df['away_gp'] = away_stats_df.apply(
        lambda x: x['away_gp'], axis=1)
    home_stats_df['away_w'] = away_stats_df.apply(
        lambda x: x['away_w'], axis=1)
    home_stats_df['away_d'] = away_stats_df.apply(
        lambda x: x['away_d'], axis=1)
    home_stats_df['away_l'] = away_stats_df.apply(
        lambda x: x['away_l'], axis=1)
    home_stats_df['away_gf'] = away_stats_df.apply(
        lambda x: x['away_gf'], axis=1)
    home_stats_df['away_ga'] = away_stats_df.apply(
        lambda x: x['away_ga'], axis=1)
    home_stats_df['away_gd'] = away_stats_df.apply(
        lambda x: x['away_gd'], axis=1)
    home_stats_df['away_pts'] = away_stats_df.apply(
        lambda x: x['away_pts'], axis=1)

    stats_df = home_stats_df
    # print(stats_df)
    stats_df['Team'] = stats_df.apply(lambda x: rename(x['Team']), axis=1)
    # print(stats_df)

    url_dk = 'https://sportsbook.draftkings.com/leagues/soccer/italy---serie-a'
    # df_dk = pd.DataFrame(pd.read_html(url_dk))
    # print(df_dk)
    html_dk = requests.get(url_dk)  # urlopen
    soup_dk = bs4.BeautifulSoup(html_dk.content, features="html.parser")

    dk = soup_dk.findAll(
        'div', attrs={'class': 'sportsbook-outcome-body-wrapper'})
    newlist = []
    for span in dk:
        newlist.append(span.text)
    dk = newlist

    i = 0
    while True:
        if i < len(dk):
            if '−' in dk[i]:
                team = dk[i]
                ind = team.index('−')
                name = team[:ind]
                odds = team[ind + 1:]
                odds = int(odds) * -1
                lst = [name, odds]
                dk[i] = lst
                i += 1
                continue
            if '+' in dk[i]:
                team = dk[i]
                ind = team.index('+')
                name = team[:ind]
                odds = team[ind:]
                odds = int(odds)
                lst = [name, odds]
                dk[i] = lst
                i += 1
                continue
        else:
            break

    i = 0
    while True:
        if i < len(dk):
            if dk[i][0] == 'Draw':
                h = i - 1
                a = i + 1
                dk[h].append(dk[i][1])
                dk[a].append(dk[i][1])
                del dk[i]
                continue
            else:
                i += 1
                continue
        else:
            break

    i = 0
    while True:
        if i < len(dk):
            if i == 0 or i % 2 == 0:
                o = i + 1
                team = dk[i][0]
                odds = dk[i][1]
                draw_odds = dk[i][2]
                opponent = dk[o][0]
                lst = [team, odds, draw_odds, opponent,
                       str(opponent) + ' @ ' + str(team)]
                dk[i] = lst
                i += 1
                continue
            if i != 0 and i % 2 != 0:
                o = i - 1
                team = dk[i][0]
                odds = dk[i][1]
                draw_odds = dk[i][2]
                opponent = dk[o][0]
                lst = [team, odds, draw_odds, opponent,
                       str(team) + ' @ ' + str(opponent)]
                dk[i] = lst
                i += 1
                continue
        else:
            break

    i = 0
    while True:
        if i < len(dk):
            if i == 0 or i % 2 == 0:
                dk[i].append(
                    'home'
                )
                i += 1
                continue
            else:
                dk[i].append(
                    'away'
                )
                i += 1
                continue
        else:
            break

    dk_headers = ['Team', 'ml', 'draw_odds', 'Opponent', 'merge_column', 'H/A']
    df_dk = pd.DataFrame(
        dk, columns=dk_headers)
    print(df_dk)
    # print('\n')
    # print(stats_df)

    avg_home_against = stats_df['home_ga'].mean()
    avg_away_against = stats_df['away_ga'].mean()

    def team_total(team):
        # print('Team = ' +
        #       str(team))
        opponent = df_dk.loc[df_dk['Team'] == team, 'Opponent'].iloc[0]
        # print('Opponent = ' +
        #   str(opponent))
        home_away = df_dk.loc[df_dk['Team'] == team, 'H/A'].iloc[0]
        if home_away == 'home':
            home_goals_for = stats_df.loc[stats_df['Team']
                                          == team, 'home_gf'].iloc[0]
            away_goals_against = stats_df.loc[stats_df['Team']
                                              == opponent, 'away_ga'].iloc[0]
            score = round(home_goals_for * away_goals_against /
                          avg_away_against, 3)
            return score
        if home_away == 'away':
            away_goals_for = stats_df.loc[stats_df['Team']
                                          == team, 'away_gf'].iloc[0]
            home_goals_against = stats_df.loc[stats_df['Team']
                                              == opponent, 'home_ga'].iloc[0]
            score = round(away_goals_for * home_goals_against /
                          avg_home_against, 3)
            return score

    df_dk['team_total'] = df_dk.apply(
        lambda x: team_total(x['Team']), axis=1)

    def opp_total(team):
        opponent = df_dk.loc[df_dk['Team'] == team, 'Opponent'].iloc[0]
        # print('Opponent = ' + str(opponent))
        home_away = df_dk.loc[df_dk['Team'] == team, 'H/A'].iloc[0]
        if home_away == 'home':
            away_goals_for = stats_df.loc[stats_df['Team']
                                          == opponent, 'away_gf'].iloc[0]
            home_goals_against = stats_df.loc[stats_df['Team']
                                              == team, 'home_ga'].iloc[0]
            opp_score = round(
                away_goals_for * home_goals_against / avg_home_against, 3)
            return opp_score
        if home_away == 'away':
            home_goals_for = stats_df.loc[stats_df['Team']
                                          == opponent, 'home_gf'].iloc[0]
            away_goals_against = stats_df.loc[stats_df['Team']
                                              == team, 'away_ga'].iloc[0]
            opp_score = round(
                home_goals_for * away_goals_against / avg_away_against, 3)
            return opp_score

    df_dk['opp_total'] = df_dk.apply(
        lambda x: opp_total(x['Team']), axis=1)

    # print('\n')
    # print(df_dk)

    def calc_total(team):
        team_total = df_dk.loc[df_dk['Team'] == team, 'team_total'].iloc[0]
        opp_total = df_dk.loc[df_dk['Team'] == team, 'opp_total'].iloc[0]
        total = round(team_total + opp_total, 3)
        return total

    df_dk['total'] = df_dk.apply(
        lambda x: calc_total(x['Team']), axis=1
    )
    # print('\n')
    # print(df_dk)

    def team_poisson(team):
        possiblePoints = []
        p = 0
        while True:
            if p < 10:
                possiblePoints.append(int(p))
                p += 1
                continue
            else:
                break
        team_poisson = []
        team_total = df_dk.loc[df_dk['Team'] == team, 'team_total'].iloc[0]
        # print(team_total)
        i = 0
        while True:
            if i < len(possiblePoints):
                chance_of_total_team = ((team_total**(possiblePoints[i])) * (
                    math.exp(-team_total)) / math.factorial(possiblePoints[i]))
                team_poisson.append(chance_of_total_team)
                i += 1
                continue
            else:
                break
        return team_poisson

    def opp_poisson(team):
        opponent = df_dk.loc[df_dk['Team'] == team, 'Opponent'].iloc[0]
        possiblePoints = []
        p = 0
        while True:
            if p < 10:
                possiblePoints.append(int(p))
                p += 1
                continue
            else:
                break
        opp_poisson = []
        opp_total = df_dk.loc[df_dk['Team'] == team, 'opp_total'].iloc[0]
        # print(opp_total)
        i = 0
        while True:
            if i < len(possiblePoints):
                chance_of_total_opp = ((opp_total**(possiblePoints[i])) * (
                    math.exp(-opp_total)) / math.factorial(possiblePoints[i]))
                opp_poisson.append(chance_of_total_opp)
                i += 1
                continue
            else:
                break
        return opp_poisson

    df_dk['team_poisson'] = df_dk.apply(
        lambda x: team_poisson(x['Team']), axis=1
    )
    df_dk['opp_poisson'] = df_dk.apply(
        lambda x: opp_poisson(x['Team']), axis=1
    )
    # print('\n')
    # print(df_dk)

    def list_chance(team):
        t = 0
        o = 0
        possiblePoints = []
        p = 0
        while True:
            if p < 10:
                possiblePoints.append(int(p))
                p += 1
                continue
            else:
                break
        team_poisson = df_dk.loc[df_dk['Team'] == team, 'team_poisson'].iloc[0]
        opp_poisson = df_dk.loc[df_dk['Team'] == team, 'opp_poisson'].iloc[0]
        rg = 100000
        q = np.asarray(possiblePoints)
        team_array = np.asarray(team_poisson)
        opp_array = np.asarray(opp_poisson)
        for i in range(rg):
            chance = random.choices(q, team_array)
            opp_chance = random.choices(q, opp_array)
            if chance > opp_chance:
                t += 1
            elif opp_chance > chance:
                o += 1
        d = rg - (t + o)
        d = round((d / 100000) * 100, 2)
        t = round((t / 100000) * 100, 2)
        o = round((o / 100000) * 100, 2)
        lst = [d, t, o]
        return lst

    df_dk['chance_list'] = df_dk.apply(
        lambda x: list_chance(x['Team']), axis=1
    )

    def draw_chance(team):
        lst = df_dk.loc[df_dk['Team'] == team, 'chance_list'].iloc[0]
        chance = lst[0]
        return chance

    def team_chance(team):
        lst = df_dk.loc[df_dk['Team'] == team, 'chance_list'].iloc[0]
        chance = lst[1]
        return chance

    def opp_chance(team):
        lst = df_dk.loc[df_dk['Team'] == team, 'chance_list'].iloc[0]
        chance = lst[2]
        return chance

    df_dk['calc_draw_%'] = df_dk.apply(
        lambda x: draw_chance(x['Team']), axis=1
    )
    df_dk['calc_%'] = df_dk.apply(
        lambda x: team_chance(x['Team']), axis=1
    )
    df_dk['calc_opp_chance'] = df_dk.apply(
        lambda x: opp_chance(x['Team']), axis=1
    )

    # print('\n')
    # print(df_dk)

    url_fte = 'https://projects.fivethirtyeight.com/soccer-predictions/matches/'
    # df_dk = pd.DataFrame(pd.read_html(url_dk))
    # print(df_dk)
    html_fte = requests.get(url_fte)  # urlopen
    soup_fte = bs4.BeautifulSoup(html_fte.content, features="html.parser")
    # print('\n')
    # print(soup_fte)
    soup_fte = str(soup_fte)

    ind_start = soup_fte.index('<table class="forecast-table')
    ind_end = soup_fte.index('<table id="all-matches">') + 20

    # print('\n')
    # print(df_fte_0)
    # print(df_fte_1)
    # print(df_fte_2)
    # print(df_fte_3)
    # print(df_fte_4
    # print(soup_fte[ind_start:ind_end])
    # print(soup_fte[ind_start:ind_end].count('<table'))
    table_count = soup_fte[ind_start:ind_end].count('<table') - 1

    url_fte = 'https://projects.fivethirtyeight.com/soccer-predictions/matches/'
    # df_fte_0 = pd.DataFrame(pd.read_html(url_fte)[0])
    # df_fte_1 = pd.DataFrame(pd.read_html(url_fte)[1])
    # df_fte_2 = pd.DataFrame(pd.read_html(url_fte)[2])
    # df_fte_3 = pd.DataFrame(pd.read_html(url_fte)[3])
    df_fte_4 = pd.DataFrame(pd.read_html(url_fte)[table_count])

    df_fte_4 = df_fte_4.drop(df_fte_4.columns[[3, 4, 5]], axis=1)

    # df_fte_4.to_excel(
    #   '/Users/Hayden/OneDrive/Sports Betting/Soccer/ISA22.xlsx', index=False
    # )
    bl = []
    bl_indices = df_fte_4.League[df_fte_4.League ==
                                 'Serie AItaly'].index.tolist()  # NEEDS TO CHANGE FOR EACH LEAGUE

    df_bl_ = df_fte_4.iloc[bl_indices]

    # print(df_bl_)

    def fte_home_name(chances):
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        chance_split = chances.split('%')
        home_name = chance_split[0]
        if '1. ' in home_name:
            ind = home_name.index(
                '1. '
            ) + 3
            home_name = home_name[ind:]
        i = 0
        while True:
            if home_name[i] not in num_list:
                i += 1
                continue
            else:
                break
        home_name = home_name[:i]
        if home_name[-1] == ' ':
            i -= 1
            home_name = home_name[:i]
        return home_name

    def fte_home_chance(chances):
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        chance_split = chances.split('%')
        home_name = chance_split[0]
        if '1. ' in home_name:
            ind = home_name.index(
                '1. '
            ) + 3
            home_name = home_name[ind:]
        i = 0
        while True:
            if home_name[i] not in num_list:
                i += 1
                continue
            else:
                break
        home_chance = home_name[i:]
        if len(str(home_chance)) == 4 and str(home_chance[:2]) == '04':
            home_chance = home_chance[2:]
        return home_chance

    def fte_draw_chance(chances):
        chance_split = chances.split('%')
        draw_chance = chance_split[1]
        draw_chance = int(draw_chance)
        return draw_chance

    def fte_away_name(chances):
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        chance_split = chances.split('%')
        away_name = chance_split[2]
        if '1. ' in away_name:
            ind = away_name.index(
                '1. '
            ) + 3
            away_name = away_name[ind:]
        i = 0
        while True:
            if away_name[i] not in num_list:
                i += 1
                continue
            else:
                break
        if away_name[-1] == ' ':  # Unique to ISA/ "Schalke 04" team
            i -= 1
        away_name = away_name[:i]
        return away_name

    def fte_away_chance(chances):
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        chance_split = chances.split('%')
        away_name = chance_split[2]
        if '1. ' in away_name:
            ind = away_name.index(
                '1. '
            ) + 3
            away_name = away_name[ind:]
        i = 0
        while True:
            if away_name[i] not in num_list:
                i += 1
                continue
            else:
                break
        away_chance = away_name[i:]
        return away_chance

    df_bl_['home_name'] = df_bl_.apply(
        lambda x: fte_home_name(x['Match']), axis=1
    )
    df_bl_['home_chance'] = df_bl_.apply(
        lambda x: fte_home_chance(x['Match']), axis=1
    )
    df_bl_['fte_draw_%'] = df_bl_.apply(
        lambda x: fte_draw_chance(x['Match']), axis=1
    )
    df_bl_['away_name'] = df_bl_.apply(
        lambda x: fte_away_name(x['Match']), axis=1
    )
    df_bl_['away_chance'] = df_bl_.apply(
        lambda x: fte_away_chance(x['Match']), axis=1
    )

    def get_date(time):
        ind = time.index(
            ', '
        ) + 2
        ind_month_end = time.index('. ')
        month = time[ind:ind_month_end]
        ind_start_date = ind_month_end + 2
        time = time[ind_start_date:]
        ind_end_date = time.index(
            month
        )
        dat_e = time[:ind_end_date]
        game_date = str(month) + '. ' + str(dat_e)
        return game_date

    df_bl_['Date'] = df_bl_.apply(
        lambda x: get_date(x['Time (ET)']), axis=1
    )

    df_bl_ = df_bl_.drop(df_bl_.columns[[0, 1, 2]], axis=1)

    df_bl_['home_name'] = df_bl_.apply(
        lambda x: rename(x['home_name']), axis=1
    )
    df_bl_['away_name'] = df_bl_.apply(
        lambda x: rename(x['away_name']), axis=1
    )

    def fte_merge_column(home_team):
        away_team = df_bl_.loc[df_bl_['home_name']
                               == home_team, 'away_name'].iloc[0]
        opponent = str(away_team) + ' @ ' + str(home_team)
        # opponent = df_dk.loc[df_dk['Team'] == home_team, 'Opponent'].iloc[0]
        return opponent
        # fte_home_chance = df_bl_.loc[df_bl_[

    df_bl_['merge_column'] = df_bl_.apply(
        lambda x: fte_merge_column(x['home_name']), axis=1
    )
    # print(df_bl_)

    df = pd.merge(
        df_dk, df_bl_, on=['merge_column']
    )

    def fte_team_chance(team):
        home_away = df.loc[df['Team']
                           == team, 'H/A'].iloc[0]
        if home_away == 'home':
            team_chance = df.loc[df['Team']
                                 == team, 'home_chance'].iloc[0]
            team_chance = int(team_chance)
            return team_chance
        else:
            team_chance = df.loc[df['Team']
                                 == team, 'away_chance'].iloc[0]
            team_chance = int(team_chance)
            return team_chance

    df['fte_%'] = df.apply(
        lambda x: fte_team_chance(x['Team']), axis=1
    )
    # print(df)

    df = df.drop(
        df.columns[[3, 4, 5, 7, 9, 10, 11, 14, 15, 16, 18, 19]], axis=1)

    def avg_draw(team):
        calc = df.loc[df['Team'] == team, 'calc_draw_%'].iloc[0]
        fte = df.loc[df['Team'] == team, 'fte_draw_%'].iloc[0]
        calc = float(calc)
        fte = float(fte)
        avg = round((calc + fte) / 2, 3)
        return avg

    def avg_chance(team):
        calc = df.loc[df['Team'] == team, 'calc_%'].iloc[0]
        fte = df.loc[df['Team'] == team, 'fte_%'].iloc[0]
        calc = float(calc)
        fte = float(fte)
        avg = round((calc + fte) / 2, 3)
        return avg

    # def ml_value(team):

    df['avg_draw_%'] = df.apply(
        lambda x: avg_draw(x['Team']), axis=1
    )
    df['avg_%'] = df.apply(
        lambda x: avg_chance(x['Team']), axis=1
    )

    def calc_draw_value(team):
        chance = df.loc[df['Team'] == team, 'calc_draw_%'].iloc[0]
        odds = df.loc[df['Team'] == team, 'draw_odds'].iloc[0]
        chance = float(chance)
        odds = float(odds)
        if odds > 0:
            value = round(((odds / 10) + 10) * chance / 100, 3)
            return value
        else:
            value = round(chance / 100 * (10 + 10 /
                          ((-1 * odds) / 10) * 10), 3)
            return value

    def calc_chance_value(team):
        chance = df.loc[df['Team'] == team, 'calc_%'].iloc[0]
        odds = df.loc[df['Team'] == team, 'ml'].iloc[0]
        chance = float(chance)
        odds = float(odds)
        if odds > 0:
            value = round(((odds / 10) + 10) * chance / 100, 3)
            return value
        else:
            value = round(chance / 100 * (10 + 10 /
                          ((-1 * odds) / 10) * 10), 3)
            return value

    def fte_draw_value(team):
        chance = df.loc[df['Team'] == team, 'fte_draw_%'].iloc[0]
        odds = df.loc[df['Team'] == team, 'draw_odds'].iloc[0]
        chance = float(chance)
        odds = float(odds)
        if odds > 0:
            value = round(((odds / 10) + 10) * chance / 100, 3)
            return value
        else:
            value = round(chance / 100 * (10 + 10 /
                          ((-1 * odds) / 10) * 10), 3)
            return value

    def fte_chance_value(team):
        chance = df.loc[df['Team'] == team, 'fte_%'].iloc[0]
        odds = df.loc[df['Team'] == team, 'ml'].iloc[0]
        chance = float(chance)
        odds = float(odds)
        if odds > 0:
            value = round(((odds / 10) + 10) * chance / 100, 3)
            return value
        else:
            value = round(chance / 100 * (10 + 10 /
                          ((-1 * odds) / 10) * 10), 3)
            return value

    def avg_draw_value(team):
        chance = df.loc[df['Team'] == team, 'avg_draw_%'].iloc[0]
        odds = df.loc[df['Team'] == team, 'draw_odds'].iloc[0]
        chance = float(chance)
        odds = float(odds)
        if odds > 0:
            value = round(((odds / 10) + 10) * chance / 100, 3)
            return value
        else:
            value = round(chance / 100 * (10 + 10 /
                          ((-1 * odds) / 10) * 10), 3)
            return value

    def avg_chance_value(team):
        chance = df.loc[df['Team'] == team, 'avg_%'].iloc[0]
        odds = df.loc[df['Team'] == team, 'ml'].iloc[0]
        chance = float(chance)
        odds = float(odds)
        if odds > 0:
            value = round(((odds / 10) + 10) * chance / 100, 3)
            return value
        else:
            value = round(chance / 100 * (10 + 10 /
                          ((-1 * odds) / 10) * 10), 3)
            return value

    df['calc_draw_value'] = df.apply(
        lambda x: calc_draw_value(x['Team']), axis=1
    )
    df['calc_%_value'] = df.apply(
        lambda x: calc_chance_value(x['Team']), axis=1
    )
    df['fte_draw_value'] = df.apply(
        lambda x: fte_draw_value(x['Team']), axis=1
    )
    df['fte_%_value'] = df.apply(
        lambda x: fte_chance_value(x['Team']), axis=1
    )
    df['avg_draw_value'] = df.apply(
        lambda x: avg_draw_value(x['Team']), axis=1
    )
    df['avg_%_value'] = df.apply(
        lambda x: avg_chance_value(x['Team']), axis=1
    )

    df = df.sort_values(by=['fte_%_value'], ascending=False)

    new_cols = ['Team', 'ml', 'draw_odds', 'team_total', 'total', 'Date', 'calc_draw_%', 'fte_draw_%', 'avg_draw_%', 'calc_%', 'fte_%',
                'avg_%', 'calc_draw_value', 'fte_draw_value', 'avg_draw_value', 'calc_%_value', 'fte_%_value', 'avg_%_value']

    df = df.reindex(columns=new_cols)

    print(df)

    df.to_excel(
        '/Users/Hayden/OneDrive/Sports Betting/Soccer/ISA22.xlsx', index=False, sheet_name='Sorted By FTE Value'
    )


ISA()
