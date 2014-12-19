#!/usr/bin/python

import json

from urllib2 import urlopen, URLError


def read_url(url):
    """
    Tries to open a url, read its response and return it. If there is a
    problem connecting to the url or if there is a non-successful status
    code returned from the server, an error in JSON is returned.

    :param url: str
    :return: str
    """
    content = ''

    try:
        response = urlopen(url)
        content = response.read()
    except ValueError:
        content = '{"error": "Bad url"}'
    except URLError as error:
        # Can't get to the url
        if hasattr(error, 'reason'):
            content = '{"error": "' + error.reason + '"}'
        # Non-successful response code
        elif hasattr(error, 'code'):
            content = '{"error": ' + error.code + '}'
    else:
        pass

    return content


def pretty_print_content(content):
    """
    Takes a string, makes sure it's in JSON and prettifies it.
    If the string is not in JSON, it will return an error in JSON

    :param content: str
    :return: str
    """
    try:
        parsed_content = json.loads(content)
    except ValueError:
        return '{"error": "Invalid JSON"}'
    return json.dumps(parsed_content, sort_keys=True, indent=4, separators=(',', ': '))


def get_contents_of_urls(urls):
    """
    Reads the content found at each url in the urls list,
    converts it to JSON and extends it onto the returned list.

    :param urls: list
    :return: list
    """
    contents = []

    for url in urls:
            content = read_url(url)
            parsed_content = json.loads(content)
            contents.extend(parsed_content)
    return contents


def write_urls_to_file(urls, file_name):
    """
    Reads the content found at each url in the list and
    writes it into a file.

    :param urls: list
    :param file_name: str
    :return:
    """
    with open(file_name, 'w') as file_handler:
        for url in urls:
            content = read_url(url)
            pretty_content = pretty_print_content(content)
            file_handler.write(pretty_content)


# Main program to run on command line.
if __name__ == "__main__":
    states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]

    base_url = "http://api.sba.gov/geodata/city_county_links_for_state_of/"
    state_urls = [base_url + state + '.json' for state in states]
    states_file_name = 'states_data.txt'
    write_urls_to_file(state_urls, states_file_name)