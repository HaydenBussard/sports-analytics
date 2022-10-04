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


def Europa():
    def team_rename(teamName):
        print('RENAMING: .' + str(teamName) + '.')
        if teamName == 'Freiburg':
            teamName = 'Freiburg'
            return teamName
        if teamName == 'Real Bettis':
            teamName = 'Real Bettis'
            return teamName
        if teamName == 'Sporting Braga':
            teamName = 'Braga'
            return teamName
        if teamName == 'Ferencvaros':
            teamName = 'Ferencvaros'
            return teamName
        if teamName == 'Royale Union SG':
            teamName = 'Saint Gilloise'
            return teamName
        if teamName == 'Real Sociedad':
            teamName = 'Real Sociedad'
            return teamName
        if teamName == 'Fenerbahce':
            teamName = 'Fenerbahce'
            return teamName
        if teamName == 'Real Betis':
            teamName = 'Real Betis'
            return teamName
        if teamName == 'Rennes':
            teamName = 'Stade Rennes'
            return teamName
        if teamName == 'Bodo / Glimt':
            teamName = 'Bodo Glimt'
            return teamName
        if teamName == 'Feyenoord':
            teamName = 'Feyenoord'
            return teamName
        if teamName == 'FC Midtjylland':
            teamName = 'Midtjylland'
            return teamName
        if teamName == 'AS Roma':
            teamName = 'AS Roma'
            return teamName
        if teamName == 'Qarabag':
            teamName = 'FK Qarabag'
            return teamName
        if teamName == 'Arsenal':
            teamName = 'Arsenal'
            return teamName
        if teamName == 'Manchester Utd':
            teamName = 'Man Utd'
            return teamName
        if teamName == 'Ludogorets':
            teamName = 'Ludogorets Razgrad'
            return teamName
        if teamName == 'Trabzonspor':
            teamName = 'Trabzonspor'
            return teamName
        if teamName == 'AEK Larnaca':
            teamName = 'AEK Larnaca'
            return teamName
        if teamName == 'Monaco':
            teamName = 'Monaco'
            return teamName
        if teamName == 'Lazio':
            teamName = 'Lazio'
            return teamName
        if teamName == 'Nantes':
            teamName = 'Nantes'
            return teamName
        if teamName == 'Sturm Graz':
            teamName = 'Sturm Graz'
            return teamName
        if teamName == 'PSV Eindhoven':
            teamName = 'PSV Eindhoven'
            return teamName
        if teamName == 'FC Zurich':
            teamName = 'Zurich'
            return teamName
        if teamName == 'Dynamo Kyiv':
            teamName = 'Dynamo Kiev'
            return teamName
        if teamName == 'Red Star':
            teamName = 'Red Star Belgrade'
            return teamName
        if teamName == 'Union Berlin':
            teamName = 'Union Berlin'
            return teamName
        if teamName == 'Malmo FF':
            teamName = 'Malmo FF'
            return teamName
        if teamName == 'Olympiakos':
            teamName = 'Olympiakos'
            return teamName
        if teamName == 'Omonia Nicosia':
            teamName = 'Omonia Nicosia'
            return teamName
        if teamName == 'HJK Helsinki':
            teamName = 'HJK Helsinki'
            return teamName
        if teamName == 'S. Tiraspol':
            teamName = 'Sheriff Tiraspol'
            return teamName
        else:
            return teamName

    url_ss_Europa = 'https://www.soccerstats.com/leagueview.asp?league=uefa'
    df_stats_champs_5 = pd.DataFrame(pd.read_html(
        requests.get(url_ss_Europa).content)[5])
    # print('INITIAL SCRAPE')
    # print(df_stats_champs_5)

    df_stats_champs_5.columns = df_stats_champs_5.iloc[0]
    df_5_headers = df_stats_champs_5.columns.values.tolist()
    print(df_5_headers)
    print(type(df_5_headers))
    print('Index 0 = .' + str(df_5_headers[0]) + '.')
    print('Index 1 = .' + str(df_5_headers[1]) + '.')
    df_5_headers[0] = 'rank'
    df_5_headers[1] = 'Team'
    df_stats_champs_5.columns = df_5_headers
    df_stats_champs_5 = df_stats_champs_5.iloc[1:].reset_index(drop=True)
    df_stats_champs_5 = df_stats_champs_5.drop(
        columns=df_stats_champs_5.columns[0], axis=1)
    # print('FIXING COLUMNS')
    # print(df_stats_champs_5)

    stats_df = df_stats_champs_5
    stats_df['Team'] = stats_df.apply(lambda x: team_rename(x['Team']), axis=1)
    # print(stats_df)

    def avg_gf(team):
        gf = stats_df.loc[stats_df['Team'] == team, 'GF'].iloc[0]
        gp = stats_df.loc[stats_df['Team'] == team, 'GP'].iloc[0]
        if int(gp) == 0:
            gp = 1
        avg_gf = round(float(gf) / float(gp), 3)
        return avg_gf

    stats_df['avg_GF'] = stats_df.apply(
        lambda x: avg_gf(x['Team']), axis=1
    )

    def avg_ga(team):
        ga = stats_df.loc[stats_df['Team'] == team, 'GA'].iloc[0]
        gp = stats_df.loc[stats_df['Team'] == team, 'GP'].iloc[0]
        if int(gp) == 0:
            gp = 1
        avg_ga = round(float(ga) / float(gp), 3)
        return avg_ga

    stats_df['avg_GA'] = stats_df.apply(
        lambda x: avg_ga(x['Team']), axis=1
    )

    league_avg_against = stats_df['avg_GA'].mean()

    url_dk = 'https://sportsbook.draftkings.com/leagues/soccer/europa-league'
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
            if '-' in dk[i]:
                if 't-G' in dk[i]:
                    print(dk[i])
                    team = dk[i]
                    ind = team.index('Germain-') + 7
                    name = team[:ind]
                    odds = team[ind:]
                    odds = int(odds)
                    lst = [name, odds]
                    dk[i] = lst
                    i += 1
                    continue
                else:
                    print(dk[i])
                    team = dk[i]
                    ind = team.index('-')
                    name = team[:ind]
                    odds = team[ind:]
                    odds = int(odds)
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

    def team_total(team):
        opponent = df_dk.loc[df_dk['Team'] == team, 'Opponent'].iloc[0]
        # print('Opponent = ' + str(opponent))
        home_away = df_dk.loc[df_dk['Team'] == team, 'H/A'].iloc[0]
        if home_away == 'home':
            print(team)
            print(stats_df)
            home_goals_for = stats_df.loc[stats_df['Team']
                                          == team, 'avg_GF'].iloc[0]
            away_goals_against = stats_df.loc[stats_df['Team']
                                              == opponent, 'avg_GA'].iloc[0]
            score = round(home_goals_for * away_goals_against /
                          league_avg_against, 3)
            return score
        if home_away == 'away':
            away_goals_for = stats_df.loc[stats_df['Team']
                                          == team, 'avg_GF'].iloc[0]
            home_goals_against = stats_df.loc[stats_df['Team']
                                              == opponent, 'avg_GA'].iloc[0]
            score = round(away_goals_for * home_goals_against /
                          league_avg_against, 3)
            return score
    df_dk['team_total'] = df_dk.apply(
        lambda x: team_total(x['Team']), axis=1)

    def opp_total(team):
        opponent = df_dk.loc[df_dk['Team'] == team, 'Opponent'].iloc[0]
        # print('Opponent = ' + str(opponent))
        home_away = df_dk.loc[df_dk['Team'] == team, 'H/A'].iloc[0]
        if home_away == 'home':
            away_goals_for = stats_df.loc[stats_df['Team']
                                          == opponent, 'avg_GF'].iloc[0]
            home_goals_against = stats_df.loc[stats_df['Team']
                                              == team, 'avg_GA'].iloc[0]
            opp_score = round(
                away_goals_for * home_goals_against / league_avg_against, 3)
            return opp_score
        if home_away == 'away':
            home_goals_for = stats_df.loc[stats_df['Team']
                                          == opponent, 'avg_GF'].iloc[0]
            away_goals_against = stats_df.loc[stats_df['Team']
                                              == team, 'avg_GA'].iloc[0]
            opp_score = round(
                home_goals_for * away_goals_against / league_avg_against, 3)
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

    url_fte = 'https://projects.fivethirtyeight.com/soccer-predictions/matches/'

    html_fte = requests.get(url_fte)  # urlopen
    soup_fte = bs4.BeautifulSoup(html_fte.content, features="html.parser")

    soup_fte = str(soup_fte)

    ind_start = soup_fte.index('<table class="forecast-table')
    ind_end = soup_fte.index('<table id="all-matches">') + 20

    table_count = soup_fte[ind_start:ind_end].count('<table') - 1

    url_fte = 'https://projects.fivethirtyeight.com/soccer-predictions/matches/'

    df_fte_4 = pd.DataFrame(pd.read_html(url_fte)[table_count])

    df_fte_4 = df_fte_4.drop(df_fte_4.columns[[3, 4, 5]], axis=1)

    bl = []
    bl_indices = df_fte_4.League[df_fte_4.League ==
                                 'UEFA Europa League'].index.tolist()

    df_bl_ = df_fte_4.iloc[bl_indices]

    isempty = df_bl_.empty

    def fte_home_name(chances):
        print(chances)
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        chance_split = chances.split('%')
        home_name = chance_split[0]
        print(home_name)
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
        if away_name[-1] == ' ':  # Unique to Champs/ "Schalke 04" team
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

    if isempty == True:
        print('FTE has no Europa Chances so df is fookin empty. Will not complete without FTE chances.')
    if isempty != True:
        print('FTE HAS LISTED PREDICTIONS FOR NEXT EUROPA GAMES')

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

    print(df_bl_)

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
        lambda x: team_rename(x['home_name']), axis=1
    )
    df_bl_['away_name'] = df_bl_.apply(
        lambda x: team_rename(x['away_name']), axis=1
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

    # def dk_merge_column(team):
    #     opponent = df_dk.loc[df_dk['Team']
    #                          == team, 'Opponent'].iloc[0]
    #     home_away = df_dk.loc[df_dk['Team']
    #                           == team, 'H/A'].iloc[0]
    #     if home_away == 'home':
    #         matchup = str(opponent) + ' @ ' + str(team)
    #         return matchup
    #     else:
    #         matchup = str(team) + ' @ ' + str(opponent)
    #         return matchup

    # df_dk['merge_column'] = df_dk.apply(
    #     lambda x: dk_merge_column(x['Team']), axis=1
    # )

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
        '/Users/Hayden/OneDrive/Sports Betting/Soccer/europa.xlsx', index=False, sheet_name='Sorted By FTE Value'
    )


Europa()
