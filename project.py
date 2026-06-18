import requests, csv
from bs4 import BeautifulSoup

job_list = []

def main():
    html = get_html()
    job = save_job(html)
    return write_file(job)


def get_html():  # get the URL from the website
    response = requests.get("https://realpython.github.io/fake-jobs/", timeout=1)
    status = response.status_code
    print("status: ", status)   
    if not status == 200:  # handle the error
        if status == 404:
            raise ValueError("Page not found")
        elif status == 500:
            raise ValueError("Server error")
        elif status == 403:
            raise ValueError("Access denied")
        else:
            raise ValueError("The status of the url is not ok...")
        
    return response.text
    

def save_job(html):
    soup = BeautifulSoup(html, features='html.parser')  # getting the html text from the website
    
    for card in soup.find_all("div", class_="card-content"):
        job_name_tag = card.find("h2", class_="title is-5")
        job_name = job_name_tag.get_text(strip=True) if job_name_tag else ""
        
        company_tag = card.find("h3", class_="subtitle is-6 company")
        company = company_tag.get_text(strip=True) if company_tag else ""

        location_tag = card.find("p", class_="location")
        location = location_tag.get_text(strip=True)

        url_tag = card.find("a")
        url = url_tag["href"]

        job_card = {"job name": job_name, 
                    "company": company, 
                    "location": location,
                    "url": url
                    }
        
        job_list.append(job_card)
        
    return job_list


def write_file(s): # write the file from the variable "job"
    with open("job.csv", "w") as file:
        fieldnames = ["job name", "company", "location", "url"]
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=",")
        writer.writeheader()
        
        for line in s:
            writer.writerow(line)

if __name__ == "__main__":
    main()