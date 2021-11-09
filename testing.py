from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime

def month_to_num(long_month):
    return {
        "January": "1",
        "February": "2",
        "March": "3",
        "April": "4",
        "May": "5",
        "June": "6",
        "July": "7",
        "August": "8",
        "September": "9",
        "October": "10",
        "November": "11",
        "December": "12"
    }[long_month]

current_date = datetime.datetime.now()


driver = webdriver.Firefox()
driver.get("https://locator.wizards.com/store/12723")


myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "dayOfWeek.text-center")))


event_names = driver.find_elements(By.CSS_SELECTOR, "span.event-name")
months = driver.find_elements(By.CSS_SELECTOR, "div.month.text-center")
days_of_the_month = driver.find_elements(By.CSS_SELECTOR, "div.dayOfMonth.text-center")
descriptions = driver.find_elements(By.CSS_SELECTOR, "div[itemprop='location performer'] > div:nth-child(1)")


for i in range(len(event_names)):
    print(event_names[i].text)
    print(f"{current_date.year}-{month_to_num(months[i].text)}-{days_of_the_month[i].text}")
    print(descriptions[i].text)


driver.close()