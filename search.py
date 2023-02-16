#!/usr/bin/env python3

import argparse
import os
import typing
from urllib.parse import urlparse

from colorama import Fore, Style
from serpapi import GoogleSearch

DEFAULT_TERMS = [
    'osrs gold',
    'runescape gold',
    'osrs bot',
    'runescape bot',
]


def search(term, page=0):
    # Testing with cached results
    # with open('results.json', 'r') as f:
    #     return json.loads(f.read())
    search_results = GoogleSearch({
        'q': term,
        'start': page * args.per_page,
        'num': args.per_page,
        'api_key': serpapi_api_key
    })
    return search_results.get_dict()


def search_all_terms(terms: list[str]):
    with open('./blocklist.txt', 'a') as blocklist:
        for term in terms:
            for page in range(args.pages):
                results = search(term=term, page=page)
                handle_results(results=results, blocklist=blocklist)


def handle_results(results: dict, blocklist: typing.IO):
    """
    Handle the results from the search and write domains to blocklist
    :param blocklist:
    :param results:
    :return:
    """
    organic = results['organic_results']

    for result in organic:
        title = result['title']
        domain = urlparse(result['link']).netloc
        print(f'{Fore.LIGHTBLUE_EX}{title}{Style.RESET_ALL}\t{Fore.GREEN}{domain}{Style.RESET_ALL}')
        write_domain(blocklist=blocklist, domain=domain)


def write_domain(blocklist: typing.IO, domain: str):
    if domain[:4] == 'www.':
        write_domain(blocklist, domain[4:])
    else:
        blocklist.write(domain + '\n')


def get_api_key():
    api_key = os.getenv("SERPAPI_API_KEY")
    if api_key is None:
        print("Please set SERPAPI_API_KEY env variable")
        exit(1)
    return api_key


if __name__ == "__main__":
    serpapi_api_key = get_api_key()

    parser = argparse.ArgumentParser()
    parser.add_argument('--query', type=str, required=False, nargs='*', help='Search query')
    parser.add_argument('--pages', type=int, default=1, help='Number of pages to fetch')
    parser.add_argument('--per-page', type=int, default=50, help='Number of results per page')
    args = parser.parse_args()

    # Get desired search terms
    search_terms = args.query or DEFAULT_TERMS

    search_all_terms(terms=search_terms)
