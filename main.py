# Import the necessary libraries
from bs4 import BeautifulSoup
import requests
import time

# Function to get the unfamiliar skill from user
def get_unfamiliar_skill():
    print('Please enter an unfamiliar skill')
    unfamiliar_skill = input('>')
    print(f'filtering out {unfamiliar_skill}')
    return unfamiliar_skill  # Returns the skill the user is not familiar with

# Function to send a GET request to the specified URL and get the HTML content
def get_html_text(url):
    return requests.get(url).text  # Returns the HTML content of the webpage

# Function to find jobs that do not require the unfamiliar skill
def find_jobs(unfamiliar_skill, html_text):

    # Parse the HTML content using BeautifulSoup with lxml parser
    soup = BeautifulSoup(html_text, 'lxml')

    # Find all the job postings in the HTML (assuming they are represented as list items with a specific class)
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # Loop through all the job postings
    for index, job in enumerate(jobs):

        # Find the publication date of the job posting (assuming it's represented by a specific span tag)
        published_date = job.find('span', class_='sim-posted').span.text

        # Only consider job postings that were posted recently (denoted by the string 'few' in the publication date)
        if 'few' in published_date:

            # Extract the company name and the required skills from the job posting (assuming they are represented by specific tags)
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            # Only consider job postings that do not require the unfamiliar skill
            if unfamiliar_skill not in skills:

                # Save the job posting details to a text file
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info}")

                print(f'file saved {index}')

if __name__ == '__main__':
    while True:
        # Ask user for an unfamiliar skill
        unfamiliar_skill = get_unfamiliar_skill()

        # Get the HTML text of the job search webpage
        html_text = get_html_text('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=')

        # Find jobs that do not require the unfamiliar skill
        find_jobs(unfamiliar_skill, html_text)

        # Wait for a specified amount of time before repeating the process
        wait_time = 30
        print(f'Waiting {wait_time} minutes...')
        time.sleep(wait_time * 60)  # Pause execution for the wait_time (in minutes)
