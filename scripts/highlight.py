import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the challenging DOM page
driver.get("http://the-internet.herokuapp.com/challenging_dom")


def highlight_element(element):
    original_style = element.get_attribute("style")
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, "background-color: yellow; border: 2px solid red;")
    time.sleep(2)
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, original_style)


mytable = driver.find_element(By.CSS_SELECTOR, '#content > div > div > div > div.large-10.columns > table')
targets = ["Diceret", "Apeirian7", "Apeirian2", "Definiebas7", "Iuvaret7"]


for target in targets:
    if target == "Diceret":
        columns = mytable.find_elements(By.CSS_SELECTOR, 'tr')[0].text.split(" ")
        row = mytable.find_elements(By.TAG_NAME, 'tr')[3]
        cell = row.find_elements(By.TAG_NAME, 'td')[columns.index("Diceret")]
        highlight_element(cell)
    elif target == "Apeirian7":
        for row in mytable.find_elements(By.TAG_NAME, 'tr'):
            if "Apeirian7" in row.text:
                element = row.find_element(By.XPATH, ".//*[text()='delete']")
                highlight_element(element)
    elif target == "Apeirian2":
        for row in mytable.find_elements(By.TAG_NAME, 'tr'):
            if "Apeirian2" in row.text:
                element = row.find_element(By.XPATH, ".//*[text()='edit']")
                highlight_element(element)
    elif target == "Definiebas7":
        for row in mytable.find_elements(By.TAG_NAME, 'tr'):
            if "Definiebas7" in row.text:
                element = row.find_element(By.XPATH, ".//*[text()='Definiebas7']")
                highlight_element(element)
    elif target == "Iuvaret7":
        for row in mytable.find_elements(By.TAG_NAME, 'tr'):
            if "Iuvaret7" in row.text:
                element = row.find_element(By.XPATH, ".//*[text()='Iuvaret7']")
                highlight_element(element)


while True:
    try:
        container = driver.find_element(By.XPATH, "//*[text()='qux']")
        container.click()
        break
    except NoSuchElementException:
        driver.refresh()


# Close the browser
driver.quit()
