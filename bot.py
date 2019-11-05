from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from botdict import BotDictionary
import re
import os
import getpass

class Bot():
    def __init__(self):
        options = Options()
        #options.headless = True
        self.driver = webdriver.Firefox()#options=options)
        self.waiter = ui.WebDriverWait(self.driver, 60)
        self.timeout = None 
        self.type = None

    def start(self):
        # Grabbing and opening link
        link = input('Link to Hotseat Topic: ')
        self.driver.get(link)

        # Hotseat login screen
        purdue_login = self.driver.find_elements_by_class_name('hover-shadow')
        purdue_login[0].click()

        # Purdue login screen
        username = self.driver.find_element_by_id('username')
        password = self.driver.find_element_by_id('password')
        submit_btn = self.driver.find_element_by_name('submit')

        userCreds = input('Purdue Account Username: ')
        # Hides user's password as it's typed 
        userPass = getpass.getpass(prompt='Purdue Account Password (Boilerkey): ')

        username.send_keys(userCreds)
        password.send_keys(userPass)
        submit_btn.click()

        print('\nPlease confirm your duo mobile request!')

        # Grab topic id from given url 
        topic_id = re.findall('[0-9]{5}', link)[0]

        driver = self.driver
        # Open requested topic 
        self.waiter.until(lambda driver: driver.find_element_by_id('private'))

        if (input("\nIs this a public topic (Y or N): ") == 'Y'):
            self.driver.find_element_by_xpath('//a[@href="/Space/ViewPublic"]').click()

        self.driver.find_element_by_xpath(f'//a[@href="/Topic/View/{topic_id}"]').click()

        # Wait until topic screen opens
        self.waiter.until(lambda driver: self.driver.find_element_by_id('PostDescription'))
    
        # Clears console for corresponding OS
        if os.name == 'nt': 
            os.system('cls')
        else:
            os.system('clear')

    def run(self):
        self.bd = BotDictionary()
        count = int(input('\nNumber of total posts: '))
        self.timeout = int(input('\nPeriod to wait between posts (in seconds): '))
        print_val = [count]
        if self.type == 'post':
            for n in range(count):
                self.postNewThought(self.bd.getRandomThought())
        elif self.type == 'reply':
            for n in range(count):
                self.replyToRecent(self.bd.getRandomThought())


    def postNewThought(self, msg):
        self.driver.find_element_by_id('PostDescription').send_keys(msg) 
        self.driver.find_element_by_xpath('//label[@title="Post Anoymous"]').click()
        self.driver.find_element_by_id('btnSubmit').click()
        if self.timeout != 0:
            self.driver.manage().timeouts().implicitlyWait(self.timeout, TimeUnit.SECONDS)

    def replyToRecent(self, msg):
        #//div[@id="questions"]/div[0]/div[0]/div[0]/
        self.driver.find_element_by_xpath('//div[@id="questions"]/div[0]/div[0]/div[0]/a/span[class="reply-num"]').click()
        self.waiter.until(lambda driver: self.driver.find_element_by_xpath('//div[@id="questions"]/div[0]/div[0]/ul/li[@class="reply-form"]'))
        self.driver.find_element_by_xpath('//div[@id="questions"]/div[0]/div[0]/ul/li[@class="reply-form"]/textarea[0]').send_keys(msg)
        self.driver.find_element_by_xpath('//div[@id="questions"]/div[0]/div[0]/ul/li[@class="reply-form"]/label[0]').click()
        self.driver.find_element_by_xpath('//div[@id="questions"]/div[0]/div[0]/ul/li[@class="reply-form"]/input[0]').click()

    def close(self):
        self.driver.close()    

def chooseType():
    print('---------------------')
    print('Cheddar bot modes:')
    print('1. Post random thoughts')
    print('2. Reply to others')
    print('---------------------')
    choice = input("\nSelect your bot mode: ")
    if choice == '1':
        bot.type = 'post'
    elif choice == '2':
        bot.type = 'reply'
    else:
        print('Invalid option')
        sys.exit()

if __name__ == "__main__":
    bot = Bot()
    bot.start()
    chooseType()
    bot.run()
    bot.close()
