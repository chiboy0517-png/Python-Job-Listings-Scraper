Project name: Job scrapper

Idea from: https://roadmap.sh/projects/job-listings-scraper

Description:
    This code use the fake Job list for training the ability to do the scrapper. In here I have learned how to use request, and csv libraries to search and write the Job it has, from the website.

TODO:

    1:
    In this file, the code start with using the request library to get the info from the website, also the website is made by the HTML.
    On the other hand, the request.get() will get the HTML.

    2:
    passing the html text into the function which using the BS4 library. The BS4 makes the HTML text looks more beutiful.
    We need to find the correspond element with using [find_all(), or find()] to find the element we want to extract.
    We extract the text of the element by using the dictionary, each job has there own "Tittle", "Company", "location", "datail URL"
    after put the each catagory inside one dict, each Job has there own dict, for instance: {job1} {job2}....
    the best way to collect all the dict is to put all the dict into the list.

    3:
    after getting the "job-card", we're ready to write it into the new file. The write method we're using is Dictwriter from the csv library.
    using     with open("new_file.csv, "w") as file    to open a whole new file.
    and      fieldnames = ["the fieldname you want to collect"]
    afterall it's the usual way to write the file. Which is writeheader() and looping the writerow()

    4:
    finally we could test the code if it's valid!
