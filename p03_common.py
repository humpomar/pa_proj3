from urllib3.exceptions import HTTPError

import requests
from bs4 import BeautifulSoup


def get_soup(url):
    """Gets a response from selected url and returns a BeautifulSoup object"""
    try:
        with requests.Session() as session:
            response = session.get(url)
    except HTTPError as error:
        print(f"Could not retrieve the page ({error.__class__.__name__}).")
    return BeautifulSoup(response.text, "html.parser")


def find_tables(soup):
    """Returns a list of tables extracted from a BeautifulSoup object"""
    return soup.find_all("table", {"class": "table"})


def find_rows(table):
    """Returns a list of rows (except headers) extracted from a table"""
    return table.find_all("tr")[2:]


def collect_all_rows(tables):
    """Collects rows from all tables into one list"""
    all_rows = []
    for table in tables:
        rows = find_rows(table)
        for row in rows:
            if row.find_all('td')[0].text != "-":
                all_rows.append(row)
    return all_rows
