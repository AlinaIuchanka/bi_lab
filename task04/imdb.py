import collections
import csv
from pathlib import Path


films_list = []
path = Path('IMDB-Movie-Data.csv')
if path.is_file():
    with open(path, 'r') as films_file:
        reader = csv.DictReader(films_file)
        for film in reader:
            film_row = {"Title": film["Title"], "Year": film["Year"],
                        "Rating": film["Rating"]}
            films_list.append(film_row)
else:
    print("File not found!")

films_list.sort(key=lambda film_rating: film_rating["Rating"], reverse=True)

film_rank = 1
for film in films_list:
    film["Rank"] = film_rank
    film_rank += 1

with open('top250_movies.csv', 'w', newline='') as top250_file:
    fieldnames = ["Rank", "Title", "Year", "Rating"]
    writer = csv.DictWriter(top250_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(films_list[:250])

year_info = {}
for film in films_list:
    year_value = year_info.get(film["Year"], [0, 0.0])
    year_value[0] += 1
    year_value[1] += float(film["Rating"])
    year_info[film["Year"]] = year_value

avg_year = {}
for year, values in year_info.items():
    avg_year[year] = values[1] / values[0]

sorted_rating_dict = dict(collections.OrderedDict(sorted(avg_year.items())))

with open('ratings.csv', 'w', newline='') as ratings:
    fieldnames = ["Year", "Avg_Rating"]
    writer = csv.DictWriter(ratings, fieldnames=fieldnames)
    writer.writeheader()
    for year, rating in sorted_rating_dict.items():
        row = {"Year": year, "Avg_Rating": rating}
        writer.writerow(row)
