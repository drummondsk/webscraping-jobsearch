from bs4 import BeautifulSoup
import requests
import time

print('Please enter an unfamiliar skill')
unfamiliar_skill = input('>')
print(f'filtering out {unfamiliar_skill}')

def find_jobs():

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
            for index, job in enumerate(jobs):
                published_date = job.find('span', class_='sim-posted').span.text
                more_info = job.header.h2.a['href']
                if unfamiliar_skill not in skills:
                    with open(f'posts/{index}.txt', 'w') as f:
                        f.write(f"Company Name: {company_name.strip()} \n")
                        f.write(f"Required Skills: {skills.strip()} \n")
                        f.write(f"More Info: {more_info}")
                    print(f'file saved {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        wait_time = 30
        print(f'Waiting {wait_time} minutes...')
        time.sleep(wait_time * 60)