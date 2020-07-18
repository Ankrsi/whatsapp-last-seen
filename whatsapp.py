from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import winsound
import time
on="offline"
off=None
i=0
j=0
ont=[]
oft=[]
web=webdriver.Chrome("chromedriver.exe")
web.get("https://web.whatsapp.com/")
web.implicitly_wait(15)
web.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div').click()
web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]').send_keys("Rahul Vya 2")
web.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/span').click()
time.sleep(3)
while(True):
    f2=web.find_element_by_xpath('//*[@id="main"]/header/div[2]/div[2]').text
    if(f2=="online"):
        on="Online"
        print(on+ time.strftime("%H:%M:%S"))
        while(i<1):
            winsound.Beep(1000,300)
            ont.append(time.strftime("%H:%M:%S"))
            i+=1
        j=0
    else:
        on=f2
        while(j<1):
            oft.append(on)
            j+=1
        i=0
    time.sleep(5)
    print(ont)
    print(oft)
