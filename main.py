import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import requests
from bs4 import BeautifulSoup
from pandas import DataFrame, concat
from transformers import pipeline

cnbc_url = "https://www.cnbc.com/search/?query=green%20hydrogen&qsearchterm=green%20hydrogen"
rss_url = "https://news.google.com/rss/search?q=green+hydrogen"

def Cnbc(url : str) -> list:
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(20)
    result = driver.find_elements_by_class_name("Card-title")
    return [i.text for i in result]

def Google_rss(url : str) -> list:
    request = requests.get(url)
    soup = BeautifulSoup(request.text, features='xml')
    return [i.text for i in soup.find_all('title')]

def create_df(source : str, result_list : list) -> list:    
    df = DataFrame({
        "Source":source,
        "Headline":result_list,
        })
    return df


df_list = [create_df("CNBC", Cnbc(cnbc_url)), create_df("Google RSS", Google_rss(rss_url))]
result_df = concat(df_list, axis=0)
# print(result_df)

sentiment_pipeline = pipeline("sentiment-analysis")

def sentiment_analysis(row) -> str:
    sentiment = sentiment_pipeline(row['Headline'])[0]
    return f"{sentiment['label']} ({sentiment['score']})"

result_df["sentiment"] = result_df.apply(sentiment_analysis, axis=1)

# writing data to csv file
result_df.to_csv("test.csv")
