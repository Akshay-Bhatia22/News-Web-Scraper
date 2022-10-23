import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
from transformers import pipeline

url = "https://www.cnbc.com/search/?query=green%20hydrogen&qsearchterm=green%20hydrogen"

def Cnbc():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(20)
    result = driver.find_elements_by_class_name("Card-title")
    print(len(result))
    result_list = [i.text for i in result]
    return result_list
    # driver.quit()

def Google_rss():
    request = requests.get(url)
    soup = BeautifulSoup(request, 'xml')
    result = soup.findAll('item')
    print(result.text)

# Google_rss()

result_list = Cnbc()


sentiment_pipeline = pipeline("sentiment-analysis")

x = sentiment_pipeline(result_list)
y = [i['label'] for i in x]
df = DataFrame({
    "Source":"CNBC",
    "Headline":result_list,
    })

def sentiment(x):
    return sentiment_pipeline(x['Headline'])
df["sentiment"] = df.apply(sentiment, axis=1)
print(df)

df.to_csv("test.csv")
