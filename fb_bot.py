from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class fb:
    def __init__(self, username, password, msg):
        self.username = username
        self.password = password
        self.msg = msg
       
        #this code below is used to diable the annoying popup permission notification on google. IT TOOK ME FUCKING 3 HOURS 
        #TO FIGURE IT OUT
        
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        self.driver = driver = webdriver.Chrome(chrome_options=chrome_options) 
        driver.get("https://www.facebook.com/")                          
        time.sleep(5)          
        
# this shit is used to find the email/password box and fill them
    def login(self):       
        driver = self.driver
        #
        email = driver.find_element_by_name("email")
        mdp = driver.find_element_by_name("pass")        
        try:
            email.clear()
            mdp.clear()
            email.send_keys(self.username)
            mdp.send_keys(self.password)
            
            
        except Exception as ex:
            print("we got zucced, RETREAT")
        mdp.send_keys(Keys.ENTER)
        time.sleep(5)

    def search_and_send(self): 
        driver = self.driver
        #put you're friends profile url here. this is the easiest and most lazy way to do it so whatever
        driver.get("friends url here")
        time.sleep(3)
        #put you're friends messages url here.DONT JUDGE ME
        driver.get('friens message url here')
        time.sleep(5)
        # looks for the text input
        driver.find_element_by_xpath("//*[@data-editor]").click()
        actions = ActionChains(driver)
        actions.send_keys(self.msg)
        actions.perform()
    

a = fb("you're username here","you're password", """you' re message """)
a.login()
time.sleep(5)
a.search_and_send()