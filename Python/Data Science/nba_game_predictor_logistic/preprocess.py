import numpy as np
import pandas as pd
from team import *

def preprocess(schedule_file, team_stats_file):

    key_stats = ["Age","W","L","PW","PL","MOV","SOS","SRS","ORtg","DRtg","NRtg","Pace"]
#    key_stats = ["Age","SOS"]

    raw_schedule = pd.read_csv(schedule_file, names = ["date","time","home team","home score","away team","away score","box score","nan1","attendance","nan2"])
    raw_schedule = raw_schedule[["date","home team","home score","away team","away score"]]

    teams = dict(np.c_[pd.unique(raw_schedule["home team"]),range(len(pd.unique(raw_schedule["home team"])))])

    schedule = []
    
    for i,row in raw_schedule.iterrows():
#        schedule.append([teams[row["home team"]],teams[row["away team"]],int(row["home score"]) > int(row["away score"])])
        schedule.append([row["home team"],row["away team"],int(row["home score"]) > int(row["away score"])])

    team_stats_raw = pd.read_csv(team_stats_file)

    team_dict = {}
    for i, row in team_stats_raw.iterrows():
        name = str(row["Team"])
        if "*" in name: name = name[:-1]
        team_dict[name] = Team(name,key_stats, row[key_stats])

    output = []
    for row in schedule:
        home_team = team_dict[row[0]]
        away_team = team_dict[row[1]]
        stat_difference = list(np.asarray(home_team.stats) - np.asarray(away_team.stats))
#        output.append(stat_difference + [int(row[2])] + [int(row[2])])
        output.append(stat_difference + [int(row[2])])

    output = np.asarray(output)
    return output
