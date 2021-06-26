from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>HFDSGF</p>")
print(soup.prettify())