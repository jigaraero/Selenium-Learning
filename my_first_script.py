from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver
driver = webdriver.Chrome()  

# Navigate to Google
driver.get("http://www.google.com")

# Find the search box
search_box = driver.find_element(By.NAME, "q")

# Enter your search term
search_box.send_keys("Gemini AI")
search_box.send_keys(Keys.RETURN)

# Pause for 1 minute (60 seconds)
time.sleep(60) 

# Close the browser 
driver.quit()
