from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd

# Task 6

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Old link didn't have the top 10, but rather links to the new page with the top 10. This is that link
driver.get("https://owasp.org/Top10/2025/")

top_10_title = driver.find_element(By.CSS_SELECTOR, "[id=top-102025-list]")
top_10 = []

if top_10_title:
    ordered_list = top_10_title.find_element(By.XPATH, 'following-sibling::ol')

    if ordered_list:
        for risk in ordered_list.find_elements(By.CSS_SELECTOR, 'li'):
            a_tag = risk.find_element(By.XPATH, 'child::a')

            href = a_tag.get_attribute("href")
            title = a_tag.text

            top_10.append({"Vulnerability Title":title, "href":href})

driver.quit()

for item in top_10:
    print(item)

df = pd.DataFrame(top_10)
print(df)


# Task 4

df.to_csv("owasp_top_10.csv")