import csv
from pyclbr import Function
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def configure_driver():
    
    chrome_options = Options()
    
    chrome_options.add_argument("--headless")
    
    # For linux/Mac
    # driver = webdriver.Chrome(options = chrome_options)

    # For windows
    driver = webdriver.Chrome(executable_path="C:/bin/chromedriver.exe", options = chrome_options)
    return driver


def Scraper(driver):
    driver.get(f"https://stats.espncricinfo.com/ci/engine/records/individual/list_captains.html?class=2;id=6;type=team")

    # try:
    #     WebDriverWait(driver, 5).until(lambda s: s.find_element_by_id("results").is_displayed())
    # except TimeoutException:
    #     print("TimeoutException: Element not found")
    #     return None

    soup = BeautifulSoup(driver.page_source, "html")

    for maincontainer in soup.select("table.engineTable"):      # main container 
        for targettag in maincontainer.select("tbody tr.data1"):           #targeted block

            title_selector = "td.left a"        #required data
            author_selector = "td.left b"
            obj =({
                "Name": targettag.select_one(title_selector).text,
                "Year": targettag.select_one(author_selector).text, 
            })
            list.append(obj)

# Main Function
list = []
driver = configure_driver()
search_keyword = "Web Scraping"
Scraper(driver, search_keyword)
print(list)

keys = list[0].keys()
with open('list.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(list)


# close the driver.
driver.close()