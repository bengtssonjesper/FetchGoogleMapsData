from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.se/maps/")

acceptTerms = driver.find_element_by_xpath(
    '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div[1]/div/button')
acceptTerms.click()

directions = driver.find_element_by_xpath('//*[@id="searchbox-directions"]')
directions.click()


def enterDirectionsFrom(location):
    input_ = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="sb_ifc51"]/input'))
    )
    input_.send_keys(location)


def enterDirectionsTo(location):
    input_ = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="sb_ifc52"]/input'))
    )
    input_.send_keys(location)


# directionsFrom = input("Where do you want directions from?")
directionsFrom = "Örebro"
# directionsTo = input("Where do you want directions to?")
directionsTo = "Jönköping"

enterDirectionsFrom(directionsFrom)
enterDirectionsTo(directionsTo)

submit = driver.find_element_by_xpath(
    '//*[@id="directions-searchbox-1"]/button[1]')
submit.click()

byCar = driver.find_element_by_xpath(
    '//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[2]/button')
byCar.click()


def clickFirstAlternative():
    firstAlternative = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="section-directions-trip-0"]/div'))
    )
    firstAlternative.click()


clickFirstAlternative()

travelTime = WebDriverWait(driver, 4).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[3]/div[1]/h1/span[1]/span[1]'))
)
print("Travel time: " + travelTime.text)


travelDistance = WebDriverWait(driver, 4).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="pane"]/div/div[1]/div/div/div[3]/div[1]/h1/span[1]/span[2]/span'))
)
print("Travel distance: " + travelDistance.text)
driver.quit()
