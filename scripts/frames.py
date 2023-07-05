from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("http://the-internet.herokuapp.com")

# Click on the "Frames" link
frames_link = driver.find_element(By.LINK_TEXT, "Frames")
frames_link.click()

# Click on the "Nested Frames" link
nested_frames_link = driver.find_element(By.LINK_TEXT, "Nested Frames")
nested_frames_link.click()

# Switch to the top frame
driver.switch_to.frame("frame-top")

# Switch to the middle frame
driver.switch_to.frame("frame-middle")

# Print the text in the middle frame
middle_frame_text = driver.find_element(By.TAG_NAME, "body").text
print("MIDDLE:", middle_frame_text)

# Switch back to the top frame
driver.switch_to.default_content()

# Switch to the bottom frame
driver.switch_to.frame("frame-bottom")

# Print the text in the bottom frame
bottom_frame_text = driver.find_element(By.TAG_NAME, "body").text
print("BOTTOM:", bottom_frame_text)

# Switch back to the top frame
driver.switch_to.default_content()

# Switch to the left frame
driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")

# Print the text in the left frame
left_frame_text = driver.find_element(By.TAG_NAME, "body").text
print("LEFT:", left_frame_text)

driver.switch_to.default_content()
driver.switch_to.frame("frame-top")
# Switch to the right frame
driver.switch_to.frame("frame-right")

# Print the text in the right frame
right_frame_text = driver.find_element(By.TAG_NAME, "body").text
print("RIGHT:", right_frame_text)

# Close the browser
driver.quit()
