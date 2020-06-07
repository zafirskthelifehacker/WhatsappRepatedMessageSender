# Imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
# Initalises the Chrome driver
driver = webdriver.Chrome('./chromedriver')
# Initialises the Whatsapp Web Page
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
# Initialises the person name or group name
personOrGroup = '"Confinement"'
string = sys.argv[1]
# Initialises the XPath for the Whatsapp Conversation
conversationXPath = '//span[contains(@title,' + personOrGroup + ')]'
# Searches for the Whatsapp Conversation and Initialises it
personOrGroupTitle = wait.until(EC.presence_of_element_located((By.XPATH, conversationXPath)))
# Clicks on the person name or group name
personOrGroupTitle.click()
# Loops the message # Change value in Rounded Bracket
for x in range(500):
    # Finds the Message Box
    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    # Enters Message in Message Box
    message.send_keys(string)
    # Finds the Send Message Button
    sendButton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    # Clicks the Send Message Button
    sendButton.click()
# Closes/Destroys the Whatsapp Web Page
driver.close()