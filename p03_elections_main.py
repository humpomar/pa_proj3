import csv

from p03_districts import get_regions, extract_urls
from p03_user import print_regions, select_region, print_districts, select_district, select_delimiter
from p03_localities import extract_locality_info
from p03_common import get_soup, find_tables, find_rows, collect_all_rows
from p03_results import extract_statistics, extract_results

elections_url = 'https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ'


def main():
    district_dictionary, list_of_regions = get_district_urls(elections_url)
    district_name, district_url, delimiter = get_user_choice(district_dictionary, list_of_regions)
    locality_info, result_urls = get_localities(district_url)
    statistics, results = get_results(result_urls)
    complete_data = merge_data(locality_info, statistics, results)
    save_csv(district_name, complete_data, delimiter)


def get_district_urls(elections_url: str):
    """Returns a dictionary of dictionaries {region1: {district1: url1, district2: url2}, region2: {}...}
    and a list of region names"""
    elections_soup = get_soup(elections_url)
    region_list = get_regions(elections_soup)
    region_tables = find_tables(elections_soup)
    district_dict = {}
    for region_index, table in enumerate(region_tables, 1):
        district_rows = find_rows(table)
        district_urls = extract_urls(district_rows)
        district_dict[region_index] = district_urls
    return district_dict, region_list


def get_user_choice(district_dict, regions_list):
    """Asks user to select a region, district and a delimiter for a csv file"""
    print_regions(regions_list)
    region_number = select_region()
    region_name = regions_list[region_number-1]
    print_districts(region_number, region_name, district_dict)
    name, url = select_district(region_number, district_dict)
    delim = select_delimiter()
    return name, url, delim


def get_localities(district_url):
    """Returns a list of dictionaries (each containing locality code and name)
    and a list of locality urls to get results"""
    district_soup = get_soup(district_url)
    locality_tables = find_tables(district_soup)
    locality_rows = collect_all_rows(locality_tables)
    return extract_locality_info(locality_rows)


def get_results(urls):
    """Returns two lists of dictionaries for all localities: statistics (containing registered, envelopes and valid)
     and results (containing all parties)"""
    all_statistics = []
    all_results = []
    for url in urls:
        result_soup = get_soup(url)
        all_tables = find_tables(result_soup)
        all_rows = collect_all_rows(all_tables)
        statistics = extract_statistics(all_rows[0])    # the first row is the first table
        results = extract_results(all_rows[1:-1])  # the last row is empty
        all_statistics.append(statistics)
        all_results.append(results)
    return all_statistics, all_results


def merge_data(first_parts, second_parts, third_parts):
    """Takes three lists of dictionaries, merges the dictionaries and returns one list of dictionaries"""
    merged = []
    for first, second, third in zip(first_parts, second_parts, third_parts):
        first.update(second)
        first.update(third)
        merged.append(first)
    return merged


def save_csv(district, data, d):
    """Writes data to a csv file (named as the selected district) with a selected delimiter"""
    try:
        with open(f"{district}.csv", "w", newline="", encoding='windows-1250') as file:
            header = data[0].keys()
            writer = csv.DictWriter(file, fieldnames=header, delimiter=d)
            writer.writeheader()
            for item in data:
                writer.writerow(item)
        print(f"Done! {len(data)} lines has been written to file '{district}.csv'.")
    except OSError as error:
        print(f"Sorry, could not write '{district}.csv' file ({error.__class__.__name__}).")


if __name__ == "__main__":
    main()
