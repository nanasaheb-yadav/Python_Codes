from __future__ import annotations

from typing import Generator

import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.co.in/jobs?q=Pharmacovigilance&l=mumbai"
soup = BeautifulSoup(requests.get(url).content, "html.parser")
print(soup)

all = soup.find_all("div", attrs={"data-tn-component": "organicJob"})
print(all)


def fetch_jobs(location: str = "mumbai") -> Generator[tuple[str, str], None, None]:
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    # This attribute finds out all the specifics listed in a job
    for job in soup.find_all("div", attrs={"data-tn-component": "organicJob"}):
        print(job)
        job_title = job.find("a", attrs={"data-tn-element": "jobTitle"}).text.strip()
        company_name = job.find("span", {"class": "company"}).text.strip()
        yield job_title, company_name


