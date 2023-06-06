import os
from functions import get_latest_tweet, loop_twitter_page, send_text, countdown
import undetected_chromedriver as uc

if __name__ == "__main__":
        TWEET_XPATH = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[2]/div/span'
        
        while True:
                print("Starting...")
                driver = uc.Chrome(headless=True)
                driver.get("https://twitter.com/ChipotleTweets")

                latest_tweet = get_latest_tweet(driver, TWEET_XPATH)
                os.system("clear")
                code = loop_twitter_page(driver, TWEET_XPATH, latest_tweet)
                resp = send_text(code)
                driver.quit()

                print(resp)
                countdown()
