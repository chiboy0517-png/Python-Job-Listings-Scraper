from project import get_html, save_job, write_file, requests
import pytest


def test_get_webpage_type_confirm():
    html = get_html()
    assert isinstance(html, str)

def test_job_type_confirm():
    html = get_html()
    job = save_job(html)
    assert isinstance(job, list)

def test_status_error():
    response = requests.get("https://realpython.github.io/fake-jobs/", timeout=1)
    assert response.status_code == 200

def test_write_file():
    html = get_html()
    job = save_job(html)
    write_file(job)
    with open("job.csv", "r") as file:
        reader = file.readline().strip()
        assert reader == "job name,company,location,url"