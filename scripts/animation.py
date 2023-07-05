import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('http://the-internet.herokuapp.com/dynamic_loading/1')

# Find and click the Start button
start_button = driver.find_element(By.CSS_SELECTOR, '#start button')
start_button.click()

# Wait for the loading animation to finish and the text to be displayed
text_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#finish h4'))
)

# Print the displayed text
logging.debug(text_element.text)

# Close the browser
driver.quit()
