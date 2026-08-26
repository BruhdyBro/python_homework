from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd

# Task 3

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

book_ul = driver.find_element(By.CSS_SELECTOR, 'ul.results')

results = [
]

if book_ul:
    for book in book_ul.find_elements(By.CSS_SELECTOR, 'li'):

        # Get book title by finding span with "class=title-content" (separates from eAudiobooks)
        book_title = book.find_element(By.CSS_SELECTOR, 'span.title-content').text

        # Get each author link into a list, then add their names from text content to separate list, and join list with ";"
        author_links = book.find_elements(By.CSS_SELECTOR, 'a.author-link')
        author_names = []

        for author in author_links:
            author_names.append(author.text)

        authors = ";".join(author_names)

        # Get format and year by finding span with "display-info-primary"
        format_year = book.find_element(By.CSS_SELECTOR, 'span.display-info-primary').text

        # Append all results in dictionary format to the results list
        results.append({"Title":book_title, "Author":authors, "Format-Year":format_year})

for result in results:
    print(result)

driver.quit()
print("\n")

df = pd.DataFrame(results)
print(df)


# Task 4

df.to_csv("get_books.csv")
df.to_json("get_books.json")
