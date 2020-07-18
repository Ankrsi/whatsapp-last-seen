from selenium import webdriver
import winsound
import time
on="offline"
off=None
i=0
t=[]
web=webdriver.Chrome("chromedriver.exe")
web.get("https://web.whatsapp.com/")
web.implicitly_wait(15)
web.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div').click()
web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[2]/div/div/div[17]/div/div/div[2]/div[1]/div/span').click()
#web.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[12]/div/div').click()
web.implicitly_wait(3)
while(True):
    f2=web.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]').text
    if(f2=="online"):
        on="Online"
        print(on+ time.strftime("%H:%M:%S"))
        while(i<1):
            winsound.Beep(1000,300)
            i+=1
    else:
        on=f2
        print(on)
        i=0

