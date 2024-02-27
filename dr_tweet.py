from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver and navigate to the Twitter page
driver = webdriver.Chrome()
driver.get("https://twitter.com/lexfridman")
# Use WebDriverWait to wait for tweet elements to load
wait = WebDriverWait(driver, 20)
# Since Twitter's actual structure is complex and dynamic, the selector here is just an example
# You need to inspect the Twitter page and find a unique and stable selector for tweets
tweets_selector = "article"  # This is an example; you need to find the correct selector
tweets = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, tweets_selector)))

# Extract the text from each tweet
tweet_texts = [tweet.text for tweet in tweets]

driver.quit()

from docx import Document

# Create a new Document
doc = Document()

# Add each tweet as a new paragraph
for tweet in tweet_texts:
    doc.add_paragraph(tweet)

# Save the document
doc.save('Lex_Tweets.docx')
