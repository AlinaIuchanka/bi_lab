import argparse
import os.path
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--year',
                    help='Displays Top250 movies titles with year',
                    action='store_true')

parser.add_argument('--rate',
                    help='Displays Top250 movies titles with rate',
                    action='store_true')

parser.add_argument('--all',
                    help='Shows title, rate, year',
                    action='store_true')

parser.add_argument('--histogram',
                    help='Displays histogram for rating or for years (in text format)')

parser.add_argument('--output',
                    help='Stores data to specified filename file')

args = parser.parse_args()
filename = 'IMDB-Movie-Data.csv'

if os.path.exists(filename):
    films = pd.read_csv(filename)

    if args.year:
        films_sorted = films.sort_values(by=['Year', 'Title'],
                                         ascending=[False, True])[: 250]
        out = films_sorted[['Title', 'Year']]

    if args.rate:
        films_sorted = films.sort_values(by=['Rating', 'Title'],
                                         ascending=[False, True])[: 250]
        out = films_sorted[['Title', 'Rating']]

    if args.all:
        out = films[['Title', 'Rating', 'Year']]

    if args.histogram == 'rating':
        films_grouped = films.groupby('Rating')['Rating'].count()
        out = films_grouped.sort_index(ascending=False)

    if args.histogram == 'year':
        films_grouped = films.groupby('Year')['Year'].count()
        out = films_grouped.sort_index(ascending=False)

    if args.output:
        out.to_csv(args.output)
    else:
        print(out.to_string())
else:
    print('No such file')
