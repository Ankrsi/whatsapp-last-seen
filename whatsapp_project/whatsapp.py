from selenium import webdriver
import time
import winsound
on="offline"
off=None
i=0
web=webdriver.Chrome("D:/chromedriver.exe")
web.get("https://web.whatsapp.com/")
time.sleep(20)
#f1=web.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[16]/div/div/div[2]/div[1]/div[1]/span').click()
f1=web.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[18]/div/div/div[2]/div[1]/div[1]/span').click()
time.sleep(3)
while(True):
    f2=web.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]').text
    if(f2=="online"):
        on="Online"
        print(on)
        while(i<1):
            winsound.Beep(1000,300)
            i+=1
    else:
        on=f2
        print(on)
        i=0

