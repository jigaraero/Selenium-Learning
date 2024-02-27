from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def search_jobs(job_title, job_location):
    # Specify the path to chromedriver if it's not in your PATH
    driver = webdriver.Chrome()  
    driver.get("https://www.indeed.com/")

    # Use explicit waits to wait for elements to be present
    wait = WebDriverWait(driver, 10)

    # Find and enter search terms
    search_title = wait.until(EC.presence_of_element_located((By.ID, "text-input-what")))
    search_title.send_keys(job_title)

    search_location = wait.until(EC.presence_of_element_located((By.ID, "text-input-where")))
    search_location.clear()  # Clearing the default text in the location field
    search_location.send_keys(job_location)
    search_location.send_keys(Keys.RETURN)  # Use RETURN to submit the search

    # Example usage within the function should be commented out or removed
    # search_jobs("Additive Manufacturing", "Boston, MA")
    
    # Pause for debugging (adjust time as needed)
    time.sleep(60)

    # Quit the driver session
    driver.quit()

# Call the function with your desired parameters
search_jobs("Additive Manufacturing", "Boston, MA")
search_jobs("3d printing", "Boston, MA")
search_jobs("Senior product engineer", "Boston, MA")



