```python
import os #Access kaggle data
import pandas as pd # data processing, CSV file I/O 
import matplotlib.pyplot as plt #Visualization
import numpy as np # linear algebra
```
```python
plt.style.use('ggplot')    #style
```
#Read Data
```python
df=pd.read_csv("../input/ballon-dor-nominees/Ballon Dor - Sheet1.csv")
```
```python
print("Number of Nominees : ",df.shape[0])
```
#Number of Nominees :  30
```python
df.head()
```
#Player	Club	Country	Position
```python
0	Riyad Mahrez	Manchester City	Algeria	FW
1	Lautaro Martinez	Inter Milan	Argentina	FW
2	Lionel Messi	PSG	Argentina	FW
3	Kevin De Bruyne	Manchester City	Belgium	MF
4	Romelu Lukaku	Chelsea	Belgium	FW
```
#Candidates by Position
```python
positions=df.Position.value_counts().index
no_players=df.Position.value_counts().values

explode=np.zeros_like(positions)
explode+=0.02
```
```python
plt.figure(figsize=(8,6))
plt.title("Candidates by Positions")
plt.pie(x=no_players, labels=positions, explode=explode, autopct='%0.2f%%', startangle=90)
plt.show()
```
#Candidates by Club
```python
clubs=df.Club.value_counts().index
no_players=df.Club.value_counts().values

plt.figure(figsize=(8,6))
plt.title("Players by Clubs")
plt.barh(y=clubs,width=no_players)
plt.gca().invert_yaxis()
plt.show()
```
#Players by Country
```python
ctry=df.Country.value_counts().index
no_players=df.Country.value_counts().values

plt.figure(figsize=(8,6))
plt.title("Players by Clubs")
plt.barh(y=ctry,width=no_players)
plt.gca().invert_yaxis()
plt.show()
```
#Players by League
```python
df.Club.unique()
```
```python
array(['Manchester City', 'Inter Milan', 'PSG', 'Chelsea', 'Real Madrid',
       'AC Milan', 'Liverpool', 'Tottenham Hotspur', 'Bayern Munich',
       'Juventus', 'Borussia Dortmund', 'Manchester United', 'Villarreal',
       'FC Barcelona', 'Atletico Madrid'], dtype=object)
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
        ```
```python
#Add new Column: League
df['League']=df.Club.apply(lambda x:league_setter(x))
```
```python
df.head()
```
```python
Player	Club	Country	Position	League
0	Riyad Mahrez	Manchester City	Algeria	FW	EPL
1	Lautaro Martinez	Inter Milan	Argentina	FW	Serie A
2	Lionel Messi	PSG	Argentina	FW	League 1
3	Kevin De Bruyne	Manchester City	Belgium	MF	EPL
4	Romelu Lukaku	Chelsea	Belgium	FW	EPL
```
```python
league=df.League.value_counts().index
no_players=df.League.value_counts().values


explode=np.zeros_like(league)
explode+=0.02

plt.figure(figsize=(8,6))
plt.title("Candidates by Leagues")
plt.pie(x=no_players, labels=league, explode=explode, autopct='%0.2f%%', startangle=90)
plt.show()

script program
```