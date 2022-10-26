# News-Web-Scraper
News web scraping from various web sites and applying sentimental analysis on the content

## 1. Getting news headlines from various sources
Using web scraping tools like beautiful soup and selenium news websites are used to get data.

### Google News RSS
This return simple XML which can be parsed using beautiful soup

### CNBC 
This returns a a dynamic website which cannot be web scraped directly using beautiful soup. Selenium is used instead. In future API call can be made to get the data from the source directly.

## 2. Sentimental Analysis
Sentiment analysis is done on the headlines using a pre-trained sentiment analysis model on huggingface [Sentimental analysis using python](https://huggingface.co/blog/sentiment-analysis-python)

## 3. Result
The result is stored in pandas dataframe and finally exported to csv.
