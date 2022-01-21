# Python Web Scraper
## Fast Web Scraper for Python

This project is made for automatic web scraping to make scraping easy. It gets a url or the html content of a web page and a list of sample data which we want to scrape from that page. This data can be text, url or any html tag value of that page. get similar content or the exact same element of those new pages.

in this we have 2 types of Scraper
<ol>
<li>API Scraper
<li>Website Scraper
</ol>

# Installation

It's compatible with Python 3

install this repository using this pip command
```
pip install git+https://github.com/itsRajatkumar/PythonWebScraper
```

or clone repository using this command
```
git clone https://github.com/itsRajatkumar/PythonWebScraper
```


##  WebSite Scrapping


### install all required python library using pip

csv for saving data in csv file
```
pip install csv
```

BeautifulSoup for parse html document
```
pip install beautifulsoup4
```

Selenium is a powerful tool for controlling web browsers through programs and performing browser automation
```
pip install selenium 
```

after installation of all library 
change url of wbsite that you want to scrape

place all of the tag name in correct order and place

<ol>
<li> enter main container class or tag name that contains all desired data.
<li>Enter subcontainer class or tag name that contains each single data
<li>Enter the tag name that contains the actual data
</ol>

after this run pyton file:
```
python pyscraper.py
```

## API WebScraper

### install all required python library using pip

csv for saving data in csv file
```
pip install csv
```

requests for handling api requests
```
pip install requests
```

after installation all required libbrary put api url in url path
add all headers correctly
and all params value

add all keys and values properly to get data

and then run python file

apiScraper.py

```
python apiScraper.py
```

After success full Run you will get an CSV file that contains all data in csv formet.
