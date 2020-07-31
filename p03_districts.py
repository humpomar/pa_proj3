def get_regions(soup):
    """Returns a list of regions extracted from BeautifulSoup object"""
    return [item.text for item in soup.find_all("h3", {"class": "kraj"})]


def extract_urls(rows):
    """Returns a list of dictionaries {district_name: district_url} extracted from table rows"""
    urls = {}
    for row in rows:
        try:
            district_name = row.find_all('td')[1].text
            href_content = row.find_all('a')[-1].get("href")   # using the last a, because Zahranici has only 2, not 3
        except (AttributeError, IndexError):
            print("Invalid cell index!")
        else:
            district_url = 'https://volby.cz/pls/ps2017nss/' + href_content
            if district_name != 'Zahraničí':
                urls.update({district_name: district_url})
    return urls
