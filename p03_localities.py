def extract_locality_info(rows):
    """Returns a list of dictionaries (each containing locality code and name) and a list of urls"""
    data = []
    urls = []
    for row in rows:
        try:
            locality_code = row.find_all('td')[0].text
            locality_name = row.find_all('td')[1].text
            href_content = row.find('a').get("href")
        except (AttributeError, IndexError):
            print("Invalid cell index!")
        else:
            data.append({'Code': locality_code, 'Name': locality_name})
            urls.append('https://volby.cz/pls/ps2017nss/' + href_content)
    return data, urls
