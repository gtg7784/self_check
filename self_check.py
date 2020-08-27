from selenium import webdriver
from datetime import date
import json
import chromedriver_autoinstaller

try:
  chromedriver_autoinstaller.install()

  options = webdriver.ChromeOptions()
  options.add_argument("start-maximized")
  options.add_argument("lang=ko_KR")
  options.add_argument('headless')
  options.add_argument('window-size=375,900')
  options.add_argument("disable-gpu")
  options.add_argument("--no-sandbox")

  driver = webdriver.Chrome(options=options)
  driver.implicitly_wait(3)

  with open('users.json') as json_file:
    users = json.load(json_file)

  
  for i in users:
    driver.get(i['url'])

    driver.find_element_by_id('rspns011').click()
    driver.find_element_by_id('rspns02').click()
    driver.find_element_by_id('rspns070').click()
    driver.find_element_by_id('rspns080').click()
    driver.find_element_by_id('rspns090').click()

    driver.find_element_by_id('btnConfirm').click()

    datenow = date.today().strftime("%y-%m-%d")

    driver.save_screenshot(f"./images/{datenow}/{i['no']}.png")
  
except Exception as e:
  print(e)    
  driver.quit()

finally:
  print("finally...")
  driver.quit()