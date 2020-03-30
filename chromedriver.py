from selenium import webdriver
import time




driver = webdriver.Chrome()
driver.get(
    "https://google.com/covid19-map/?hl=en") #open up the site ...
for n in range(182):


    country = driver.find_element_by_xpath(f'//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div[2]/div[2]/c-wiz/div/div[2]/div/div[1]/table/tbody/tr[{n+1}]/td[1]') # go to the price section
    cases = driver.find_element_by_xpath(
        f'//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div[2]/div[2]/c-wiz/div/div[2]/div/div[1]/table/tbody/tr[{n + 1}]/td[2]')
    Recovered = driver.find_element_by_xpath(
        f'//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div[2]/div[2]/c-wiz/div/div[2]/div/div[1]/table/tbody/tr[{n + 1}]/td[4]')
    Deaths = driver.find_element_by_xpath(
        f'//*[@id="yDmH0d"]/c-wiz/div/div/div/div/div[2]/div[2]/c-wiz/div/div[2]/div/div[1]/table/tbody/tr[{n + 1}]/td[5]')
    print(n + 1)
    print(country.text)
    print('cases')
    print(cases.text)
    print('Recovered')
    print(Recovered.text)
    print('Deaths')
    print(Deaths.text)


driver.close()
'''priceinstring =""

for n in price.text : # converting the string to a readable intager
    if n == "," :
        break
    elif n == ".":
        pass
    else:
        priceinstring = priceinstring + n

priceinfloat = int(priceinstring) #to convert the price to int number .....
if priceinfloat < 1300 :   # to find out if the price is good or not  ....
    print("good price")
    print(priceinstring)
else:
    print("still expencive")
    print(f"the price is : {priceinstring}")
time.sleep(15) # sleeping 5 seconds to reopen the site
driver.close() # close the tab'''