# vnnewsbot
This is a very simple bot to scrape interested news from Vietnamese websites. Follow the guideline to install scrapy firstly http://doc.scrapy.org/en/latest/intro/tutorial.html

The input can be configured from setting.json file with the below template.

	{
	  "site1": {
	    "name": "VnExpress Kinh Doanh",
	    "url": "https://kinhdoanh.vnexpress.net",
	    "keyword": "(Samsung.*|Apple.*|Huawei.*|Oppo.*|Vivo.*|Qualcomm.*|Nokia.*|LG.*|Amazon.*|Nikkei.*|FPT.*|BKAV.*|PetroVietnam.*)",
	    "num_of_xpaths": "3",
	    "title": "//h3[@class=\"title_news\"]/a/@title",
	    "description": "//h4[@class=\"description\"]/text()",
	    "link": "//h3[@class=\"title_news\"]/a/@href"
	  }
	}

## How it works
This simple bot will read the website information from setting.json file and store scraping sites in a list. Then it uses XPath expression to extract data from the response. If a value is given in "keyword" field, it will return only interested information related to that value.

For example, the above template will scrape https://kinhdoanh.vnexpress.net and return only interested information related to Samsung, Apple, Huawei...

## Field Description
Following guideline to add more sites to scrape
	"name": The title of website to scrape
	"url": The URL of website to scrape
	"keyword": Keyword to filter out from the scraping result. 
	"num_of_xpaths": Number of XPath to extract.
	"title": The XPath title format
	"description": The XPath description format
	"link": The XPath description link format

## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl -o quotes.json
