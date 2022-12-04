from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)




# driver.get('http://github.com')
# print(driver.title)
# with open('./GitHub_Action_Results.txt', 'w') as f:
#     f.write(f"This was written with a GitHub action {driver.title}")


driver.get('https://www.nepalstock.com.np/floor-sheet')
print(driver.title)
with open('./GitHub_Action_Results.txt', 'w') as f:
    f.write(f"This was written with a GitHub action {driver.title}")
    
    
    element = driver.find_element(
    'xpath', "/html/body/app-root/div/main/div/app-floor-sheet/div/div[3]/div/div[5]/div/select")
driver.execute_script("arguments[0].click();", element)
time.sleep(2)

print('Click')


def total_turnover():
    total_turnover = driver.find_element(by= By.XPATH, value= '/html/body/app-root/div/main/div/app-floor-sheet/div/div[5]/div[1]/table/tbody/tr/td[1]').text
    return total_turnover

try:
    select = Select( driver.find_element(by=By.XPATH, value="//select[@class='ng-untouched ng-pristine ng-valid']"))
    select.select_by_visible_text('500')
except:
    pass 
driver.find_element(by=By.XPATH, value=" //button[normalize-space()='Filter']").click()
time.sleep(1) 
end_of_page = driver.find_element(by= By.XPATH, value='/html/body/app-root/div/main/div/app-floor-sheet/div/div[5]/div[2]/pagination-controls/pagination-template/ul/li[9]/a/span[2]').text
print(end_of_page)

with open('./GitHub_Action_Results.txt', 'w') as f:
    f.write(f"end_of_page {end_of_page}")


turnover = total_turnover()
print(turnover)

with open('./GitHub_Action_Results.txt', 'w') as f:
    f.write(f"turnover = {turnover }")



