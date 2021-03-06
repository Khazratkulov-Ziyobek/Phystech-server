import requests
from bs4 import BeautifulSoup

create_table = []
url = ''


def scraping():
    create_table.clear()
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    league_table = soup.find('table', class_='standing-table__table callfn')
    for team in league_table.find_all('tbody'):
        rows = team.find_all('tr')
        for row in rows:
            table_info = {
                'place': row.find('td', class_='standing-table__cell').text,
                'teams': row.find('td', class_='standing-table__cell standing-table__cell--name').text.strip(),
                'played': row.find_all('td', class_='standing-table__cell')[2].text,
                'wins': row.find_all('td', class_='standing-table__cell')[3].text,
                'draws': row.find_all('td', class_='standing-table__cell')[4].text,
                'losses': row.find_all('td', class_='standing-table__cell')[5].text,
                'goals_for': row.find_all('td', class_='standing-table__cell')[6].text,
                'goals_against': row.find_all('td', class_='standing-table__cell')[7].text,
                'goals_difference': row.find_all('td', class_='standing-table__cell')[8].text,
                'points': row.find_all('td', class_='standing-table__cell')[9].text
            }
            create_table.append(table_info)
