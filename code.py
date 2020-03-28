# G-Mail auto trash clear Bot
from selenium import webdriver
from time import sleep 

class mailbot:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        sleep(2)
        
    def keys(self,path,keys):
        self.driver.find_element_by_xpath(path)\
        .send_keys(keys)
        sleep(1)
    
    def click(self,path):
        self.driver.find_element_by_xpath(path)\
        .click()
        sleep(5)
        
bot=mailbot()
# login
bot.keys(MAILID,PASSWORD) # pass mail id and password as arguments...
bot.click('//*[@id="identifierNext"]/span/span')
bot.keys('//*[@id="password"]/div[1]/div/div[1]/input','*password') # type password as arguments...
bot.click('//*[@id="passwordNext"]/span/span')
sleep(3)
# more
bot.click('//*[@id=":jt"]/div/div[2]/div/div/div[2]')
sleep(3)
# trash
bot.click('//*[@id=":jw"]/div[1]/div/div[6]')
sleep(3)
# select all
bot.click('//*[@id=":4"]/div[2]/div[1]/div[1]/div/div/div[1]')
sleep(3)
# delete forever
bot.click('//*[@id=":4"]/div[2]/div[1]/div[1]/div/div/div[2]')
