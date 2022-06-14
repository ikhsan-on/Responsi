import os #Access kaggle data
import pandas as pd # data processing, CSV file I/O 
import matplotlib.pyplot as plt #Visualization
import numpy as np # linear algebra

plt.style.use('ggplot')    #style

Read Data

df=pd.read_csv("../input/ballon-dor-nominees/Ballon Dor - Sheet1.csv")

print("Number of Nominees : ",df.shape[0])

df.head()

Candidates by Position

positions=df.Position.value_counts().index
no_players=df.Position.value_counts().values

explode=np.zeros_like(positions)
explode+=0.02

plt.figure(figsize=(8,6))
plt.title("Candidates by Positions")
plt.pie(x=no_players, labels=positions, explode=explode, autopct='%0.2f%%', startangle=90)
plt.show()

Candidates by Club

clubs=df.Club.value_counts().index
no_players=df.Club.value_counts().values

plt.figure(figsize=(8,6))
plt.title("Players by Clubs")
plt.barh(y=clubs,width=no_players)
plt.gca().invert_yaxis()
plt.show()

Players by Country

ctry=df.Country.value_counts().index
no_players=df.Country.value_counts().values

plt.figure(figsize=(8,6))
plt.title("Players by Clubs")
plt.barh(y=ctry,width=no_players)
plt.gca().invert_yaxis()
plt.show()

Players by League

df.Club.unique()

#list of clubs in each league
EPL=['Manchester City','Chelsea','Liverpool', 'Tottenham Hotspur','Manchester United']
LaLiga=[  'Real Madrid','Villarreal','FC Barcelona', 'Atletico Madrid']
SerieA=['Inter Milan','AC Milan','Juventus', ]
Bundesliga=['Bayern Munich','Borussia Dortmund']
Leage1=['PSG']

#function to classify Clubs based on League
def league_setter(team):
    if team in EPL:
        return "EPL"
    elif team in LaLiga:
        return "La Liga"
    elif team in SerieA:
        return "Serie A"
    elif team in Bundesliga:
        return "Bundesliga"
    else:
        return "League 1"

#Add new Column: League
df['League']=df.Club.apply(lambda x:league_setter(x))

df.head()

league=df.League.value_counts().index
no_players=df.League.value_counts().values

explode=np.zeros_like(league)
explode+=0.02

plt.figure(figsize=(8,6))
plt.title("Candidates by Leagues")
plt.pie(x=no_players, labels=league, explode=explode, autopct='%0.2f%%', startangle=90)
plt.show()
