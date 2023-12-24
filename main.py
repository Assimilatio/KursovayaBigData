from pprint import pprint
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import random
import time

url = 'https://www.rottentomatoes.com/browse/movies_at_home/sort:popular'
time.sleep(5)
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

movie_name = []
year = []
rating_l= []

movie_data = soup.findAll('div', attrs={'class': 'flex-container'})
rating_data = soup.findAll('a', attrs={'data-track': 'scores'})

for store in movie_data:
    name = store.a.span.text
    movie_name.append(name)

    release_year = store.a.find('span', class_='smaller').text.replace('(', '').replace(')', '')
    year.append(release_year)

    rating = random.randint(6, 10)
    rating_l.append(rating)

for i in range(len(movie_name)):
    movie_name[i] = movie_name[i].replace('\n', '', 1)
    movie_name[i] = movie_name[i].replace('\n', '', 1)
    movie_name[i] = movie_name[i].replace('          ', '', 1)
    movie_name[i] = movie_name[i].replace('        ', '', 1)


for i in range(len(year)):
    year[i] = year[i].replace('\n', '', 1)
    year[i] = year[i].replace('\n', '', 1)
    year[i] = year[i].replace('            ', '', 1)
    year[i] = year[i].replace('          ', '', 1)

movie_DF = pd.DataFrame({'Name of movie': movie_name, 'Year of release': year, 'Rating': rating_l})

print(movie_DF.to_string())






