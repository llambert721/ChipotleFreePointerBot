import sys
import time
import os
import undetected_chromedriver as uc
from py_imessage import imessage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def clean_text(tweet: str) -> tuple[str, bool]:
    try:
        tweet = tweet.lower()
        tweet = tweet.split("text", 1)[1]
        tweet = tweet.split(" ")[1]
        tweet = tweet.strip()
        tweet = tweet.upper()
    except(IndexError):
        return "No code found", False
    return tweet, True

def get_current_time() -> str:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

def get_latest_tweet(driver: uc.Chrome, TWEET_XPATH: str) -> str:
    WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, TWEET_XPATH)))
    tweet_element = driver.find_element(By.XPATH, TWEET_XPATH)
    return tweet_element.text

def loop_twitter_page(driver: uc.Chrome, TWEET_XPATH: str, last_tweet: str) -> str:
    i = 1
    while True:
        driver.refresh()
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.XPATH, TWEET_XPATH)))
        tweet_element = driver.find_element(By.XPATH, TWEET_XPATH)
        print(f"DRIVER IS RUNNING, TIMES REFRESHED: {i}", end='\r')
        sys.stdout.flush()
        i += 1
        
        if tweet_element.text != last_tweet:
            print("")
            last_tweet = tweet_element.text
            resp, code_found = clean_text(tweet_element.text)

            if code_found:
                print(f"Code found at {get_current_time()}")
                return resp
            else:
                print(resp)

def countdown(i = 25):
    for _ in range(i):
        print(f"Restarting in {i} seconds, CTRL + V to cancel ", end='\r')
        sys.stdout.flush()
        i -= 1
        time.sleep(1)
    os.system("clear")
    

def send_text(code: str) -> str:
    imessage.send("888222", code)
    return f"Text sent at {get_current_time()}! ({code})\nPlease check your phone"
