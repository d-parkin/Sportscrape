# David Parkin
# Expand to see betting odds and predictions or analyze other data given by the API
# Uses Hidden API Endpoints to get game information

# Tasks: Create classes for the team and score type so that they can be used for more things


import json
import requests

def getNBA():
    # gets information from API by sending a request to the URL
    r = requests.get('http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard')
    data = r.text
    # reads JSON file into python
    parse = json.loads(data)
    # gets the number of events for the day for iterating
    num_events = len(parse['events'])

    # figure out a way to determine how many games are playing and replace the 8
    for i in range(num_events):
        # gets url for all packages of json
        # r = requests.get('http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard')
        # data = r.text
        # parse = json.loads(data)
        game_name = parse['events'][i]['name']

        # gets team name and score for all events today
        team1 = parse['events'][i]['competitions'][0]['competitors'][0]['team']['name']
        team2 = parse['events'][i]['competitions'][0]['competitors'][1]['team']['name']
        score1 = parse['events'][i]['competitions'][0]['competitors'][0]['score']
        score2 = parse['events'][i]['competitions'][0]['competitors'][1]['score']

        print(game_name)
        print(team2, score2)
        print(team1, score1,"\n")

    return ("Enter:")

def getNFL():
    r = requests.get('http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard')
    data = r.text
    parse = json.loads(data)
    num_events = len(parse['events'])

    # figure out a way to determine how many games are playing and replace the 8
    for i in range(num_events):
        game_name = parse['events'][i]['name']

        team1 = parse['events'][i]['competitions'][0]['competitors'][0]['team']['name']
        team2 = parse['events'][i]['competitions'][0]['competitors'][1]['team']['name']
        score1 = parse['events'][i]['competitions'][0]['competitors'][0]['score']
        score2 = parse['events'][i]['competitions'][0]['competitors'][1]['score']

        print(game_name)
        print(team2, score2)
        print(team1, score1,"\n")

    return ("Enter:")

def getMLB():
    r = requests.get('http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard')
    data = r.text
    parse = json.loads(data)
    num_events = len(parse['events'])

    # figure out a way to determine how many games are playing and replace the 8
    for i in range(num_events):
        game_name = parse['events'][i]['name']

        team1 = parse['events'][i]['competitions'][0]['competitors'][0]['team']['name']
        team2 = parse['events'][i]['competitions'][0]['competitors'][1]['team']['name']
        score1 = parse['events'][i]['competitions'][0]['competitors'][0]['score']
        score2 = parse['events'][i]['competitions'][0]['competitors'][1]['score']

        print(game_name)
        print(team2, score2)
        print(team1, score1,"\n")

    return ("Enter:")

def getNHL():
    r = requests.get('http://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard')
    data = r.text
    parse = json.loads(data)
    num_events = len(parse['events'])

    # figure out a way to determine how many games are playing and replace the 8
    for i in range(num_events):
        game_name = parse['events'][i]['name']

        team1 = parse['events'][i]['competitions'][0]['competitors'][0]['team']['name']
        team2 = parse['events'][i]['competitions'][0]['competitors'][1]['team']['name']
        score1 = parse['events'][i]['competitions'][0]['competitors'][0]['score']
        score2 = parse['events'][i]['competitions'][0]['competitors'][1]['score']

        print(game_name)
        print(team2, score2)
        print(team1, score1,"\n")

    return ("Enter:")

def getEPL():
    r = requests.get('https://site.api.espn.com/apis/site/v2/sports/soccer/eng.1/scoreboard')
    data = r.text
    parse = json.loads(data)
    num_events = len(parse['events'])

    # figure out a way to determine how many games are playing and replace the 8
    for i in range(num_events):
        game_name = parse['events'][i]['name']

        team1 = parse['events'][i]['competitions'][0]['competitors'][0]['team']['name']
        team2 = parse['events'][i]['competitions'][0]['competitors'][1]['team']['name']
        score1 = parse['events'][i]['competitions'][0]['competitors'][0]['score']
        score2 = parse['events'][i]['competitions'][0]['competitors'][1]['score']

        print(game_name)
        print(team2, score2)
        print(team1, score1,"\n")

    return ("Enter:")

choice = 0
while choice != 6:
    choice = int(input("1: NBA Scores\n2: NFL Scores\n3: MLB Scores\n4: NHL Scores\n5: EPL Scores\n6: Exit"))
    if choice == 1:
        print(getNBA())
    if choice == 2:
        print(getNFL())
    if choice == 3:
        print(getMLB())
    if choice == 4:
        print(getNHL())
    if choice == 5:
        print(getEPL())







