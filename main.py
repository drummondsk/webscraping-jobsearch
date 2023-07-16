"""
Purpose:
"""
import time
from bs4 import BeautifulSoup
import requests


# Function to get the unfamiliar skill from user
def get_unfamiliar_skill():
    """

    :return:
    """
    unfamiliar_skill = 'Django'
    print(f'filtering out {unfamiliar_skill}')
    return unfamiliar_skill  # Returns the skill the user is not familiar with

# Function to send a GET request to the specified URL and get the HTML content
def get_html_text(url):
    """

    :param url:
    :return:
    """
    return requests.get(url, timeout=20).text  # Returns the HTML content of the webpage

# Function to find jobs that do not require the unfamiliar skill
def find_jobs(unfamiliar_skill, html_text):
    """

    :param unfamiliar_skill:
    :param html_text:
    :return:
    """

    # Parse the HTML content using BeautifulSoup with lxml parser
    soup = BeautifulSoup(html_text, 'lxml')

    # Find all the job postings in the HTML
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # Loop through all the job postings
    for index, job in enumerate(jobs):

        # Find the publication date of the job posting
        published_date = job.find('span', class_='sim-posted').span.text

        # Only consider job postings that were posted recently
        if 'few' in published_date:

            # Extract the company name and the required skills from the job posting
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            # Only consider job postings that do not require the unfamiliar skill
            if unfamiliar_skill not in skills:

                # Save the job posting details to a text file
                with open(f'posts/{index}.txt', 'w', encoding='UTF-8') as f_file:
                    f_file.write(f"Company Name: {company_name.strip()} \n")
                    f_file.write(f"Required Skills: {skills.strip()} \n")
                    f_file.write(f"More Info: {more_info}")

                print(f'file saved {index}')

if __name__ == '__main__':
    while True:
        # Ask user for an unfamiliar skill
        UNFAMILIAR_SKILL = get_unfamiliar_skill()

        # Get the HTML text of the job search webpage
        HTML_TEXT = get_html_text('https://www.timesjobs.com/candidate/job-search.html?'
                                  'searchType=personalizedSearch&from=submit&txtKeywords='
                                  'Python&txtLocation=')

        # Find jobs that do not require the unfamiliar skill
        find_jobs(UNFAMILIAR_SKILL, HTML_TEXT)

        # Wait for a specified amount of time before repeating the process
        WAIT_TIME = 30
        print(f'Waiting {WAIT_TIME} minutes...')
        time.sleep(WAIT_TIME * 60)
