[![linting: pylint](https://ci.appveyor.com/api/projects/status/kayjdh5qtgymhoxr/branch/master?svg=true)](https://github.com/drummondsk/webscraping-jobsearch/actions/workflows/pylint.yml)
# Job Scraper

## Description

This project is a simple Python script that scrapes job postings from the TimesJobs website. It specifically looks for Python jobs that do not require a certain skill specified by the user.

## Installation

1. Clone this repository:
2. pip install -r requirements.txt

The script will scrape the job postings and create a text file for each job that doesn't require the specified skill. The files are saved in the 'posts' directory.

The script runs in an infinite loop and repeats the process every 30 minutes.

## License

MIT License. See the `LICENSE` file for more details.
