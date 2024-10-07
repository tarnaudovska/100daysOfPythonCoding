from bs4 import BeautifulSoup
import requests


response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web = response.text
soup = BeautifulSoup(web, "html.parser")
all_movies = soup.find_all(name = "h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("./day_45/best_movies/movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
