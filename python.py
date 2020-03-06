#!/usr/bin/env python3

import csv
import urllib.request

from bs4 import BeautifulSoup

def get_html(url):
	response = urllib.request.urlopen(url)
	return response.read()

def parse(cryptocurrencies, html):
	soup = BeautifulSoup(html)
	table = soup.find('tbody')

	for row in table.find_all('tr'):
		cols = row.find_all('td')

		cryptocurrencies.append({
			'name': cols[1].a.text,
			'market_cap': cols[3].div.text,
			'price': cols[4].a.text
			})

	return cryptocurrencies

def save (cryptocurrencies, path):
	with open(path, 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(("Name", 'Market_cap', 'Price'))

		for cryptocurrencies in cryptocurrencies:
			writer.writerow((cryptocurrencies['name'], cryptocurrencies['market_cap'], cryptocurrencies['price']))

def main():

	cryptocurrencies = []

	parse(cryptocurrencies, get_html('https://coinmarketcap.com/all/views/all/'))

	save(cryptocurrencies, 'cryptocurrencies.csv')

if __name__ == '__main__':
	main()