import requests
from bs4 import BeautifulSoup
import _sqlite3
import time


def createtable():
    cursor.execute("CREATE TABLE IF NOT EXISTS TopAccountsByCountries(Username TEXT, Owner TEXT, Followers_Million INT, Profession TEXT, Country TEXT)")


def addvalue(username_f, owner_f, followers_f, profession_f, country_f):
    cursor.execute("INSERT INTO TopAccountsByCountries(Username, Owner, Followers_Million, Profession,Country) VALUES(?,?,?,?,?)", (username_f, owner_f, followers_f, profession_f, country_f))
    con.commit()


def delete():
    cursor.execute("DELETE FROM TopAccountsByCountries")
    con.commit()


con = _sqlite3.connect("instagram.db")
cursor = con.cursor()

process = int(input("Create: 1\nDelete: 2\n"))

t0 = time.time()

if process == 1:
    createtable()
    url = "https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    table = soup.find_all("table")[1]
    table = table.contents[1].find_all("tr")
    table = table[1:-1]

    for i in range(20):
        var = table[i].find_all("td")

        username = var[0].text
        owner = var[1].text
        followers = int(var[2].text)
        profession = var[3].text
        country = var[4].text

        addvalue(username, owner, followers, profession, country)

elif process == 2:
    delete()

con.close()

t1 = time.time()

print("Process time:", (str(t1-t0))[:6])
