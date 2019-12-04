#!/bin/bash/python3

import csv
import re
import requests
from bs4 import BeautifulSoup as bs

url='https://bulletin.case.edu/course-descriptions/'

def main():
	page = requests.get(url)
	soup = bs(page.text, 'html.parser')

	map_dict = {}
	course_code = "\\([a-zA-Z]{4}\\)"

	strong = soup.find_all('strong')
	for item in strong:
		code = re.search(course_code, item.text)
		if code:
			just_letters = code.group(0).strip('()')

			title = re.sub(course_code, '', item.text)
			if just_letters not in map_dict:
				map_dict[just_letters] = title

	# Save to csv
	w = csv.writer(open("course_dict.csv", "w"))
	for key, val in map_dict.items():
	    w.writerow([key, val])


main()