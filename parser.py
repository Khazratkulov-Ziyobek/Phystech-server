import requests
from bs4 import BeautifulSoup

world_leagues = ["Premier League", "La Liga", "Bundesliga", "Serie A", "Ligue 1"]
choosing_league = True
while choosing_league:
    print("Here are World Competitions 🏆 🏆 🏆: ")
    for leagues in world_leagues:
        print(leagues)
    selected_league = input("Choose on of the League table ⚽️ ⚽️ ⚽️ : ")
    if selected_league in world_leagues:
        print('Congratulations! 🥳 🥳 🥳 Thank you, for choosing this league, just moment 😉 😉 😉')
        url_league = selected_league.split()
        url_league = '-'.join(url_league).lower()
        url = 'https://www.skysports.com/' + url_league + '-table'
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')

        league_table = soup.find('table', class_='standing-table__table callfn')

        for team in league_table.find_all('tbody'):
            rows = team.find_all('tr')
            for row in rows:
                num_team = row.find('td', class_='standing-table__cell').text
                pl_team = row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip()
                pl_points = row.find_all('td', class_='standing-table__cell')[9].text
                print(num_team, pl_team, pl_points)
        choosing_league = False
    else:
        print("Sorry, we can not found this league 😢 😢 😢")
