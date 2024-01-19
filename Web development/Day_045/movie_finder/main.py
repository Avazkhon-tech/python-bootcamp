import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

names = soup.find_all(name="h3")
movies_names = [name.text for name in names[::-1]]

with open("movies.txt", "w") as file:
    for i in movies_names:
        file.write(f"{i} \n")
