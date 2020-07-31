line = '=' * 90


def print_regions(regions):
    """Prints a list of regions with their keys"""
    print(line)
    print("WELCOME TO OUR ELECTIONS SCRAPER!")
    print(line)
    print("List of regions:")
    for number, region in enumerate(regions, 1):
        print(f"{number:>3} {region}")


def select_region():
    """Asks user to select a region by typing its key"""
    print(line)
    print("Please select a region!")
    region = 0
    while region not in range(1, 15):
        user = input("Write region number or 'q' to quit: ")
        if user.lower() == 'q':
            print("See you later!")
            exit()
        try:
            region = int(user)
        except ValueError:
            region = 0
            print("Invalid input. Please enter a number!")
        else:
            if region not in range(1, 15):
                print("Invalid number. Please try again!")
    return region


def print_districts(region_number, region_name, district_dict):
    """Prints a list of districts and their urls for a selected region"""
    print(line)
    print(f"Districts in {region_name}:")
    for district_name, district_url in district_dict[region_number].items():
        print(f"{district_name:<20} {district_url}")


def select_district(region_number, district_dict):
    """Asks user to select a district by typing its name"""
    print(line)
    print("Please select a district!")
    district = ''
    while district not in district_dict[region_number].keys():
        district = input("Write district name or 'q' to quit: ")
        if district.lower() == 'q':
            print("See you later!")
            exit()
    url = district_dict[region_number].get(district)
    print(line)
    print(f"Your choice: {district} {url}")
    return district, url


def select_delimiter():
    """Asks user to select a delimiter for the csv file (',' or ';')"""
    print(line)
    print("Please select delimiter for your csv file!")
    d = ''
    while d not in [',', ';']:
        d = input("Write ',' or ';' or 'q' to quit: ")
        if d.lower() == 'q':
            print("See you later!")
            exit()
    print(line)
    return d
