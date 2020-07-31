def extract_statistics(row):
    """Returns a dictionary of registered, envelopes and valid, extracted from the first table"""
    try:
        registered = delete_space(row.find_all('td')[3].text)
        envelopes = delete_space(row.find_all('td')[6].text)
        valid = delete_space(row.find_all('td')[7].text)
    except (AttributeError, IndexError):
        print("Invalid cell index!")
    else:
        return {'Registered': registered, 'Envelopes': envelopes, 'Valid': valid}


def extract_results(rows):
    """Returns a dictionary of results of all parties extracted from table rows"""
    results = {}
    for row in rows:
        party = row.find_all('td')[1].text
        result = delete_space(row.find_all('td')[2].text)
        results.update({party: result})
    return results


def delete_space(raw_numstring):
    """Returns a number string without escape sequence for space between thousands"""
    return raw_numstring.replace('\xa0', '')
