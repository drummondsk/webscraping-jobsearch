from bs4 import BeautifulSoup
import requests

# send a get request to the web page to retrieve the html text of the webpage
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

# create a beautifulSoup instance and pass in the html text to scrape and the parser
soup = BeautifulSoup(html_text, 'lxml')

# parses through the html and find the first list tage with the class description
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# iterate through each job listing on the HTML page
for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    if 'few' in published_date:

        # search for the related h3 tag and display the related text while eliminating the blank spaces
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = job.find('span', class_='srp-skills').text.replace(' ', '')
        published_date = job.find('span', class_='sim-posted').span.text

        print(f'''
        Company Name: {company_name}
        Required Skills: {skills}
        ''')
        print(" ")
