from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import date
import json
import os
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

  datenow = date.today().strftime("%y%m%d")
  
  project_dir = os.path.dirname(os.path.abspath(__file__))
  
  for i in users:
    driver.get(i['url'])

    try:
      driver.find_element_by_class_name("ui-dialog-titlebar-close").click()
    except NoSuchElementException:
      pass

    driver.find_element_by_id('rspns011').click()
    driver.find_element_by_id('rspns02').click()
    driver.find_element_by_id('rspns070').click()
    driver.find_element_by_id('rspns080').click()
    driver.find_element_by_id('rspns090').click()

    driver.find_element_by_id('btnConfirm').click()

    driver.save_screenshot(f"{project_dir}/images/{datenow}-{i['no']}.png")

except Exception as e:
  print(e)
  driver.quit()

finally:
  print("finish all self check")
  driver.quit()
