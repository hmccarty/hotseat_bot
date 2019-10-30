from selenium import webdriver
import selenium.webdriver.support.ui as ui
import re
import os
import spam

def start():
    #Opening firefox
    driver = webdriver.Firefox()

    #Grabbing and opening link
    link = input('Link to Hotseat Topic: ')
    driver.get(link)

    #Setting up waiter
    wait = ui.WebDriverWait(driver, 10)

    #Hotseat Login Screen
    purdue_login = driver.find_elements_by_class_name('hover-shadow')
    purdue_login[0].click()

    #Purdue Login Screen
    username = driver.find_element_by_id('username')
    password = driver.find_element_by_id('password')
    submit_btn = driver.find_element_by_name('submit')

    userCreds = input('Purdue Account Username: ')
    userPass = input('Purdue Account Password (Boilerkey): ')

    username.send_keys(userCreds)
    password.send_keys(userPass)
    submit_btn.click()

    print('\nPlease confirm your duo mobile request!')

    #Grab Topic ID from Given Link
    topic_id = re.findall('[0-9]{5}', link)[0]

    #Open Requested Topic
    wait.until(lambda driver: driver.find_element_by_id('private'))
    topic = driver.find_element_by_xpath(f'//a[@href="/Topic/View/{topic_id}"]')
    topic.click()

    #Topic Screen
    wait.until(lambda driver: driver.find_element_by_id('PostDescription'))
    
    if os.name == 'nt': 
        os.system('cls')
    else:
        os.system('clear')

def run():
    print('1. Spam')
    choice = input('\nWhat would you like the bot to do? ')
    if choice == '1':
        spam.run(["re","apple"])

def printToTopic(msg):
    input_box = driver.find_element_by_id('PostDescription')
    input_box.send_keys(msg) 
    submit_btn = driver.find_element_by_id('btnSubmit')
    submit_btn.click()

if __name__ == "__main__":
    start()
    run()
