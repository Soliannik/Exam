import sqlite3
import requests
from bs4 import BeautifulSoup as bs
URL_TEMPLATE = "https://sinoptik.ua/погода-киев"
r = requests.get(URL_TEMPLATE)
class Site:
    def __init__(self, database):
        self.database = database
    def create(self):
        connection = sqlite3.connect('sitebase.db')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE name(VARCHAR(50) NOT NULL)""")
        connection.commit()

    def insert(self, name, url):
        connection = sqlite3.connect('sitebase.db')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS sites(id INTEGER PRIMARY KEY,
         url VARCHAR(150) NOT NULL UNIQUE, name(VARCHAR(50) NOT NULL);""")
        connection.commit()
    def select(self, name):
        results = []
        connection = sqlite3.connect('sitebase.db')
        cursor = connection.cursor()
        cursor.execute("""SELECT * FROM sites""")
        connection.commit()
        return results


class Parcing:
    def __init__(self, database):
        self.database = Site(database)

    def interface(self):
        url = input("Enter the URL of the site: ")
        connection = sqlite3.connect('sitebase.db')
        cursor = connection.cursor()
        print("Successfully.")

    def search(self, query):
        results = []

        return results

    def fetch_page(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")

while True:
    print("What would you like to do?")
    print("1. Add a website to the database")
    choice = input("Enter your choice: ")





