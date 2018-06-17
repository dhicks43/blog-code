import requests
from bs4 import BeautifulSoup

job_urls = []
page_multiplier = 10

for pages in range(4):
    indeed_search = 'https://www.indeed.com/jobs?q=Python+Data+Engineer&start=' + str(pages * page_multiplier)

    response = requests.get(indeed_search)
    soup = BeautifulSoup(response.content, "html.parser")
    job_titles = soup.findAll('a', class_="turnstileLink")

    for job in job_titles:
        job_urls.append(job['href'])


print("Url list has", len(job_urls), "urls")

with open("indeed_data_python.txt", "a") as f:
    for job_page in job_urls:
        try:
            job_url = 'https://www.indeed.com' + job_page
            response = requests.get(job_url)
            soup = BeautifulSoup(response.content, "html.parser")
            output = soup.find(class_="summary").text

            f.write(output)

        # captures ill-formed job page listings (usually ad related)
        except AttributeError:
            print("Something wrong with url:", job_page)


print("Completed the scrape!")




