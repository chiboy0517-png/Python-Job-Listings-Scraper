## Plan: Fake Python Jobs Scraper

TL;DR - Build a small Python script that fetches the Fake Python Jobs page, parses each job card with Beautiful Soup, extracts title/company/location/detail-url, and writes the results to a CSV file.

**Steps**
1. Add a new Python file for the scraper, for example `fake_jobs_scraper.py` in the workspace root.
2. Import the needed libraries: `requests`, `bs4` (Beautiful Soup), and `csv`.


3. Write a function to download the page:
   - Use `requests.get` with the URL `https://realpython.github.io/fake-jobs/`.
   - Check the response status and handle errors.


4. Write a function to parse the HTML:
   - Create a Beautiful Soup object from the response text.
   - Find all job postings on the page by their container element.
   - For each posting, extract job title, company, location, and the relative or absolute URL for details.
   - Handle missing fields safely by substituting an empty string or placeholder.
   
5. Normalize the job detail URL:
   - If the link is relative, join it with the base URL to make a complete URL.
   
6. Write a function to save the extracted data to a CSV file:
   - Use `csv.DictWriter` with headers `title`, `company`, `location`, and `link`.
   - Write the header row and then each job record.
7. Add a `main` function to call download, parse, and save in order.
8. Optionally, add a simple CLI behavior:
   - Accept an output filename or use a default like `jobs.csv`.
9. Run the script and verify the resulting CSV contains all scraped jobs.

**Relevant files**
- `fake_jobs_scraper.py` — create this new script.

**Verification**
1. Run `python fake_jobs_scraper.py` and confirm it completes without errors.
2. Open the generated `jobs.csv` and verify it has columns for title, company, location, and link.
3. Confirm the number of rows matches the number of job postings on the Fake Python Jobs page.
4. Test one or two URLs from the CSV in a browser to ensure the links are valid.

**Decisions**
- Use the static page at `https://realpython.github.io/fake-jobs/` so scraping is simple and reliable.
- Store results in CSV with one row per job.
- Keep code readable, with clear function separation for downloading, parsing, and saving.

**Further Considerations**
1. If you want, I can also give you the exact function structure and a sample of how each step should look.
2. If you want to support command-line output filename input, I can add that as a small extra step.
